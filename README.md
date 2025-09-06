![Hackatime](https://hackatime-badge.hackclub.com/U08HC7N4JJW/metaclean)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/simon0302010/metaclean/.github%2Fworkflows%2Fpython-install.yml)
![PyPI - Version](https://img.shields.io/pypi/v/metaclean-gui)
![AUR Version](https://img.shields.io/aur/version/metaclean-git)

# MetaClean

A simple and easy-to-use application to clean metadata from your images.

## Features

*   **Bulk processing:** Clean metadata from multiple images at once.
*   **Selective cleaning:** Choose which metadata to remove (Everything, GPS, EXIF).
*   **Image preview:** Double-click on an image to see a preview.
*   **Cross-platform:** Works on Linux and Windows.

## Requirements

*   Python 3.8+
*   [ExifTool](https://exiftool.org/) must be installed and available in your system's PATH.

## Installation

### From PyPI

You can install MetaClean from pip:

```bash
pip install metaclean-gui
```

### From AUR (Arch Linux)

For Arch Linux users, MetaClean is available in the AUR:

```bash
yay -S metaclean-git
```

## Usage

After installation, run:

```bash
metaclean
```
> You can also run it from the start menu if you installed it from the AUR.

## License

This project is licensed under the GNU General Public License 3 - see the [LICENSE](LICENSE) file for details.
