# Mufi Homebrew Tap

## Installation

`brew install mustafif/mufi/MufiZ`

Or `brew tap mustafif/mufi` and then `brew install MufiZ`.

## Experimental Installation (UNSTABLE)

`brew install mustafif/mufi/MufiZ-Next`

Or `brew tap mustafif/mufi` and then `brew install MufiZ-Next`.

## Managing Versions

This repository includes a version bump script to help automate updating formula versions:

```
python version_bump.py <new_version> [options]
```

### Options:
- `--skip-verification`: Use when the release files don't exist yet. This creates placeholder hashes.
- `--fixes`: Apply syntax fixes to formula files if needed.
- `--no-next-bump`: Disable automatic next minor version bump for experimental formula.

### Examples:
```
# Update to version 0.9.1 with verification (requires files to exist on GitHub)
python version_bump.py 0.9.1

# Update to version 0.9.1 without verification (for preparing PRs)
python version_bump.py 0.9.1 --skip-verification

# Update to 0.9.1 but keep next-experimental at 0.9.1 instead of 0.10.0
python version_bump.py 0.9.1 --no-next-bump
```

### Version Handling:
- For the standard formula (`mufiz.rb`), the version is set exactly as specified.
- For the experimental formula (`mufiz-next.rb`), the version is automatically bumped to the next minor version.
  - Example: If you specify `0.9.1`, the experimental version becomes `0.10.0`.
  - This behavior can be disabled with the `--no-next-bump` option.

The script will:
1. Create backups of all modified files (*.bak)
2. Update version numbers in formula files (with automatic next minor bump for experimental)
3. Update SHA256 hashes (or use placeholders)
4. Update `hashes.py` script with new version

## Documentation

`brew help`, `man brew` or check [Homebrew's documentation](https://docs.brew.sh).
