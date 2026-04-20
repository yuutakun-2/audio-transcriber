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

## Installation

Follow these steps to set up the tool on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yuutakun-2/audio-transcriber.git
   cd audio-transcriber
   ```

2. **(Optional) Create a Virtual Environment**
   It is recommended to use a virtual environment to avoid dependency conflicts.
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Package**
   
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

Run the tool by typing the command in your terminal:
```bash
whisper-cli
```

The tool is interactive and will prompt you for the following settings:

### Configuration Options:
- **Model**: Choose the model size (`tiny`, `base`, `small`, `medium`, `large`). Larger models are more accurate but slower and require more memory.
- **Language**: Specify the language (e.g., `ja` for Japanese, `en` for English) or use `auto` for automatic detection.
- **Device**: Select `cpu` or `auto`. Use `auto` if you have a compatible NVIDIA GPU (CUDA) for much faster processing.
- **Compute**: Selection of precision (`int8`, `float16`, `float32`). Default `int8` is recommended for most CPUs.
- **Beam size**: Number of beams for search (1-5). Higher values might improve accuracy slightly.
- **Output format**: 
  1. `TXT with timestamps`: `[00:00:10 - 00:00:20] Transcription text`
  2. `TXT only`: Plain text output.
  3. `SRT`: Subtitle format.
- **Skip existing**: If `y`, the tool will skip files that already have a corresponding output file in the destination folder.
- **Input path**: Provide an absolute or relative path to an audio file or a folder containing multiple audio files.
- **Output folder**: Specify where to save the results. Defaults to the same location as the input.
- **Save settings**: If `y`, your choices will be saved to `~/.whisper-cli/config.json` and used as defaults for the next run.
