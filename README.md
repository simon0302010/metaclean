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

## Demo

[Watch Demo](https://raw.githubusercontent.com/simon0302010/metaclean/main/demo.mp4)

## Requirements

*   A Computer
*   Python 3.8+

# Installation

MetaClean can be installed using several methods depending on your operating system and preferences.

## Quick Install

### Windows
**Recommended for most Windows users**

Download the pre-built executable from the [Releases page](https://github.com/simon0302010/metaclean/releases). This bundle includes ExifTool, so no additional setup is required.

1. Download the latest `.exe` file
2. Run the executable directly - no installation needed

### Arch Linux
**For Arch-based distributions**

Install directly from the AUR using your preferred AUR helper:

```bash
# Using yay
yay -S metaclean-git

# Using paru
paru -S metaclean-git
```

## Universal Install (PyPI)

### Prerequisites
MetaClean requires [ExifTool](https://exiftool.org/) to function. Install it first:

**Linux (Ubuntu/Debian):**
```bash
sudo apt install libimage-exiftool-perl
```

**Linux:**
```bash
# Use your distribution's package manager
sudo apt install libimage-exiftool-perl      # Debian/Ubuntu
sudo dnf install perl-Image-ExifTool         # Fedora/RHEL
sudo pacman -S perl-image-exiftool           # Arch Linux
```

**macOS:**
```bash
# Using Homebrew
brew install exiftool

# Using MacPorts
sudo port install p5-image-exiftool
```

**Windows:**
1. Download ExifTool from the [official website](https://exiftool.org/)
2. Extract and add the folder to your system PATH

### Install MetaClean
Once ExifTool is installed and accessible from your command line:

```bash
pip install metaclean-gui
```

## Verify Installation

To confirm MetaClean is installed correctly:

```bash
metaclean --version
```

If you encounter issues, ensure ExifTool is properly installed and accessible:

```bash
exiftool -ver
```

## Usage

After installation, run:

```bash
metaclean
```
> You can also run it from the start menu if you installed it from the AUR.

## License

This project is licensed under the GNU General Public License 3 - see the [LICENSE](LICENSE) file for details.
