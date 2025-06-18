# Version Bump Utility for MufiZ Homebrew Formulas

This utility automates the process of updating version numbers and SHA256 hashes in the MufiZ Homebrew formula files.

## Features

- Updates version numbers in both formula files (`mufiz.rb` and `mufiz-next.rb`)
- Fetches new SHA256 hashes from the GitHub releases
- Updates all URLs in the formula files
- Updates the `hashes.py` script with the new version
- Creates backups of modified files

## Requirements

- Python 3.6 or higher
- Required packages:
  - `requests`

Install the required packages with:
```
pip install requests
```

## Usage

Run the script with the new version as a command-line argument:

```
python version_bump.py <new_version>
```

Example:

```
python version_bump.py 0.9.1
```

## Important Notes

1. Make sure the releases for the new version already exist on GitHub before running the script:
   - For regular releases: `https://github.com/Mustafif/MufiZ/releases/tag/v{new_version}`
   - For experimental releases: `https://github.com/Mustafif/MufiZ/releases/tag/next-experimental`

2. The script creates backup files (`*.bak`) before modifying any file. If something goes wrong, you can restore from these backups.

3. Always verify the changes after running the script to ensure everything was updated correctly.

## Flow

1. Script creates backups of all files to be modified
2. Updates version numbers in formula files
3. Downloads release files to calculate SHA256 hashes
4. Updates hashes in formula files
5. Updates `hashes.py` with new version information

## Troubleshooting

If the script fails to fetch the new hashes, make sure:
- The release files actually exist on GitHub
- You have a working internet connection
- The GitHub API rate limits have not been exceeded

In case of failure, the script will automatically restore files from backups.