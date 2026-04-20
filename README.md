# whisper-cli

Local speech-to-text CLI tool using faster-whisper.

## Features
- Fully offline transcription
- Japanese + multilingual support
- TXT / SRT output
- Timestamp support
- Beginner-friendly CLI

## Prerequisites

Before installing, ensure you have Python and pip installed on your system.

### Installing Python and pip

- **Windows**: Download and run the installer from the [official Python website](https://www.python.org/downloads/windows/). Make sure to check the box **"Add Python to PATH"** during installation.
- **macOS**: Python 3 and pip3 are usually pre-installed or can be installed via [Homebrew](https://brew.sh/): `brew install python`.
- **Linux**: Use your distribution's package manager.
  - Ubuntu/Debian: `sudo apt update && sudo apt install python3 python3-pip`
  - Fedora: `sudo dnf install python3 python3-pip`

## Install

Clone the repository and run the installation command.

**On Windows and Linux:**
```bash
pip install .
```

**On macOS:**
Use `pip3` to ensure the tool and its dependency `faster-whisper` are installed correctly:
```bash
pip3 install .
```

## Usage

Run the tool from your terminal:
```bash
whisper-cli
```
