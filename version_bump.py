#!/usr/bin/env python3
"""
Version Bump Script for MufiZ Homebrew Formulas

This script automates the process of updating version numbers and SHA256 hashes
in Homebrew formula files for MufiZ.

Usage:
    python version_bump.py <new_version> [--skip-verification]

Example:
    python version_bump.py 0.9.1
    python version_bump.py 0.9.1 --skip-verification
"""

import sys
import os
import re
import hashlib
import requests
import shutil
import argparse


def get_sha256(url, skip_verification=False):
    """Download a file and compute its SHA256 hash."""
    try:
        response = requests.get(url, timeout=30, allow_redirects=True)
        response.raise_for_status()
        return hashlib.sha256(response.content).hexdigest()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        if skip_verification:
            print("Skip verification enabled. Using placeholder hash.")
            return "0" * 64  # Return placeholder hash
        return None


def update_formula_file(file_path, new_version, is_next=False, skip_verification=False, disable_next_bump=False):
    """Update version and hashes in formula file."""
    print(f"Updating {file_path}...")

    # Read the current formula
    with open(file_path, 'r') as f:
        content = f.read()

    # Make a backup
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)
    print(f"Backup created: {backup_path}")

    # If this is the next-experimental formula, calculate the next minor version
    if is_next and not disable_next_bump:
        # Split the version into parts (e.g., "0.9.1" -> ["0", "9", "1"])
        version_parts = new_version.split(".")
        if len(version_parts) >= 2:
            # Increment the minor version (middle number)
            minor_version = int(version_parts[1])
            version_parts[1] = str(minor_version + 1)
            # Reset patch version to 0 if it exists
            if len(version_parts) >= 3:
                version_parts[2] = "0"
            # Create the next minor version string
            next_version = ".".join(version_parts)
            print(f"For next-experimental, using next minor version: {next_version}")
            new_version = next_version

    # Update the version
    version_pattern = r'version\s*=\s*"([^"]+)"'
    content = re.sub(version_pattern, f'version = "{new_version}"', content)

    # Determine the correct GitHub org and repo
    # Check if we should use Mufi-Lang org instead of Mustafif
    if "Mufi-Lang" in content:
        org = "Mufi-Lang"
    else:
        org = "Mustafif"

    # Determine tag based on formula type
    if is_next:
        tag = "next-experimental"
        # Update the URL and hashes
        url_prefix = f"https://github.com/{org}/MufiZ/releases/download/{tag}/mufiz_{new_version}"
    else:
        tag = f"v{new_version}"
        # Update the URL and hashes
        url_prefix = f"https://github.com/{org}/MufiZ/releases/download/{tag}/mufiz_{new_version}"

    # Get the new hashes
    linux_url = f"{url_prefix}_x86_64-linux.zip"
    arm_mac_url = f"{url_prefix}_aarch64-macos.zip"
    intel_mac_url = f"{url_prefix}_x86_64-macos.zip"

    print("Fetching new hashes...")
    linux_hash = get_sha256(linux_url, skip_verification)
    arm_mac_hash = get_sha256(arm_mac_url, skip_verification)
    intel_mac_hash = get_sha256(intel_mac_url, skip_verification)

    if not skip_verification and not all([linux_hash, arm_mac_hash, intel_mac_hash]):
        print("Failed to get all hashes. Restoring backup...")
        shutil.copy2(backup_path, file_path)
        return False

    # Update the main URL and hash
    linux_url_pattern = r'url\s+"https://github\.com/Mustafif/MufiZ/releases/download/[^/]+/mufiz_[^_]+_x86_64-linux\.zip"'
    linux_hash_pattern = r'sha256\s+"[a-f0-9]{64}"'

    # Update the main URL
    content = re.sub(linux_url_pattern, f'url "{linux_url}"', content, count=1)
    # Update the main hash (first occurrence only)
    content = re.sub(linux_hash_pattern, f'sha256 "{linux_hash}"', content, count=1)

    # Find and replace the ARM Mac URL and hash
    arm_mac_section = re.search(
        r'if Hardware::CPU\.arm\?.*?end',
        content,
        re.DOTALL
    )

    if arm_mac_section:
        arm_section_content = arm_mac_section.group(0)
        # Replace URL in the ARM Mac section
        arm_section_content = re.sub(
            r'url\s+"[^"]+"',
            f'url "{arm_mac_url}"',
            arm_section_content
        )
        # Replace hash in the ARM Mac section
        arm_section_content = re.sub(
            r'sha256\s+"[a-f0-9]{64}"',
            f'sha256 "{arm_mac_hash}"',
            arm_section_content
        )
        # Replace the entire section
        content = content.replace(arm_mac_section.group(0), arm_section_content)

    # Find and replace the Intel Mac URL and hash
    intel_mac_section = re.search(
        r'else.*?# URL and SHA256 hash for Intel Mac.*?end',
        content,
        re.DOTALL
    )

    if intel_mac_section:
        intel_section_content = intel_mac_section.group(0)
        # Replace URL in the Intel Mac section
        intel_section_content = re.sub(
            r'url\s+"[^"]+"',
            f'url "{intel_mac_url}"',
            intel_section_content
        )
        # Replace hash in the Intel Mac section
        intel_section_content = re.sub(
            r'sha256\s+"[a-f0-9]{64}"',
            f'sha256 "{intel_mac_hash}"',
            intel_section_content
        )
        # Replace the entire section
        content = content.replace(intel_mac_section.group(0), intel_section_content)

    # URLs are already updated in the code above

    # Write the updated content back
    with open(file_path, 'w') as f:
        f.write(content)

    print(f"Successfully updated {file_path}")
    return True


def update_hashes_py(new_version):
    """Update hashes.py script with new version."""
    print("Updating hashes.py...")
    hashes_path = "hashes.py"

    try:
        # Read the current hashes.py
        with open(hashes_path, 'r') as f:
            content = f.read()

        # Make a backup
        backup_path = f"{hashes_path}.bak"
        shutil.copy2(hashes_path, backup_path)
        print(f"Backup created: {backup_path}")

        # Update TAG and VERSION
        tag_pattern = r'TAG\s*=\s*"([^"]+)"'
        version_pattern = r'VERSION\s*=\s*"([^"]+)"'

        content = re.sub(tag_pattern, f'TAG = "v{new_version}"', content)
        content = re.sub(version_pattern, f'VERSION = "{new_version}"', content)

        # Write the updated content back
        with open(hashes_path, 'w') as f:
            f.write(content)

        print("Successfully updated hashes.py")
        return True
    except Exception as e:
        print(f"Error updating hashes.py: {e}")
        return False


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Bump version for MufiZ Homebrew formulas.')
    parser.add_argument('version', help='New version number')
    parser.add_argument('--skip-verification', action='store_true',
                      help='Skip hash verification and use placeholders if files not found')
    parser.add_argument('--fixes', action='store_true',
                      help='Apply syntax fixes to formula files')
    parser.add_argument('--no-next-bump', action='store_true',
                      help='Disable automatic next minor version bump for experimental formula')
    args = parser.parse_args()

    new_version = args.version
    skip_verification = args.skip_verification
    apply_fixes = args.fixes
    disable_next_bump = args.no_next_bump

    print(f"Bumping version to {new_version}")
    if skip_verification:
        print("Warning: Skip verification enabled. Placeholder hashes will be used if files are not found.")
    if disable_next_bump:
        print("Note: The next minor version bump for experimental formula is disabled.")
    else:
        print("Note: The next-experimental formula will use the next minor version automatically.")

    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Update formula files
    mufiz_path = os.path.join("Formula", "mufiz.rb")
    mufiz_next_path = os.path.join("Formula", "mufiz-next.rb")

    success = update_formula_file(mufiz_path, new_version, skip_verification=skip_verification, disable_next_bump=disable_next_bump)
    if not success:
        print("Failed to update mufiz.rb. Exiting.")
        sys.exit(1)

    success = update_formula_file(mufiz_next_path, new_version, is_next=True, skip_verification=skip_verification, disable_next_bump=disable_next_bump)
    if not success:
        print("Failed to update mufiz-next.rb. Exiting.")
        sys.exit(1)

    # Update hashes.py
    success = update_hashes_py(new_version)
    if not success:
        print("Failed to update hashes.py. Exiting.")
        sys.exit(1)

    if apply_fixes:
        print("Applying syntax fixes to formula files...")
        try:
            # Fix known syntax issues in formula files
            for formula_file in [mufiz_path, mufiz_next_path]:
                with open(formula_file, 'r') as f:
                    content = f.read()

                # Fix common syntax errors
                if 'sha256 "sha256' in content:
                    content = content.replace('sha256 "sha256', 'sha256')

                # Ensure proper end statements
                content = re.sub(r'sha256\s+"[a-f0-9]{64}"\s*(?!end)',
                                 r'sha256 "\1"\n    end',
                                 content)

                with open(formula_file, 'w') as f:
                    f.write(content)
            print("Syntax fixes applied.")
        except Exception as e:
            print(f"Error applying syntax fixes: {e}")

    print(f"Version bump to {new_version} completed successfully!")
    print("Please verify the changes and commit them.")
    if skip_verification:
        print("Note: Some hashes may be placeholders. Remember to update them when the actual files are available.")
    if not disable_next_bump:
        print("Note: The next-experimental formula now uses the next minor version automatically.")


if __name__ == "__main__":
    main()
