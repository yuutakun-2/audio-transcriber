import os
import json
import subprocess
from faster_whisper import WhisperModel
from tqdm import tqdm

SUPPORTED_EXT = (".mp3", ".wav", ".m4a", ".ogg", ".flac")

# -----------------------
# Helpers
# -----------------------

def ask(prompt, default):
    val = input(f"{prompt} [default: {default}]: ").strip()
    return val if val else default


def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def format_time_srt(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


# -----------------------
# Config
# -----------------------

def get_config_path():
    return os.path.expanduser("~/.whisper-cli/config.json")


def load_config():
    path = get_config_path()
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_config(config):
    path = get_config_path()
    print(f"Saving config to: {path}")  # DEBUG
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(config, f, indent=2)


# -----------------------
# Audio utils
# -----------------------

def get_audio_duration(file_path):
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return float(result.stdout.strip())
    except:
        return None


def get_audio_files(path):
    if os.path.isfile(path):
        return [path]

    elif os.path.isdir(path):
        files = []
        for f in os.listdir(path):
            if f.lower().endswith(SUPPORTED_EXT):
                files.append(os.path.join(path, f))
        return sorted(files)

    else:
        return []


# -----------------------
# Transcribe one file
# -----------------------

def transcribe_file(model_obj, input_path, output_path, fmt, lang, beam):
    print(f"\n--- Processing: {input_path} ---")

    total_duration = get_audio_duration(input_path)

    segments_gen, _ = model_obj.transcribe(
        input_path,
        language=None if lang == "auto" else lang,
        beam_size=beam
    )

    with open(output_path, "w", encoding="utf-8") as f:

        if total_duration:
            pbar = tqdm(total=100, desc="Progress", unit="%")
            last_percent = 0
        else:
            pbar = tqdm(desc="Transcribing", unit="segment")

        for i, seg in enumerate(segments_gen, 1):

            # progress
            if total_duration:
                percent = int((seg.end / total_duration) * 100)
                if percent > last_percent:
                    pbar.update(percent - last_percent)
                    last_percent = percent
            else:
                pbar.update(1)

            # format
            if fmt == "1":
                start = format_time(seg.start)
                end = format_time(seg.end)
                line = f"[{start} - {end}] {seg.text.strip()}"

            elif fmt == "2":
                line = seg.text.strip()

            elif fmt == "3":
                start = format_time_srt(seg.start)
                end = format_time_srt(seg.end)
                line = f"{i}\n{start} --> {end}\n{seg.text.strip()}\n"

            # write + print
            f.write(line + "\n")
            tqdm.write(line)

        pbar.close()

    print(f"Done: {output_path}")


# -----------------------
# Main CLI
# -----------------------

def main():
    print("\n=== Whisper CLI (Batch + Config) ===\n")

    config = load_config()

    model_name = ask("Model (tiny/base/small/medium/large)", config.get("model", "medium"))
    lang = ask("Language (auto/ja/en)", config.get("language", "auto"))
    device = ask("Device (cpu/auto)", config.get("device", "cpu"))
    compute = ask("Compute (int8/float32)", config.get("compute", "int8"))
    beam = int(ask("Beam size (1-5)", str(config.get("beam", 2))))

    print("\nOutput format:")
    print("1. TXT with timestamps")
    print("2. TXT only")
    print("3. SRT")
    fmt = ask("Choose (1/2/3)", config.get("format", "1"))

    skip_existing = ask("Skip already processed files? (y/n)", config.get("skip", "y")).lower() == "y"

    input_path = ask("Input file OR folder (default: current directory)", ".")
    output_dir = ask("Output folder (leave empty = same location)", config.get("output_dir", ""))

    if not os.path.exists(input_path):
        print("Error: path not found")
        return

    files = get_audio_files(input_path)

    if not files:
        print("No supported audio files found.")
        return

    if not output_dir:
        output_dir = os.path.dirname(files[0])

    os.makedirs(output_dir, exist_ok=True)

    print(f"\nFound {len(files)} file(s)")
    print(f"Skip existing: {skip_existing}")

    # Save config option
    save = ask("Save these settings as default? (y/n)", "n").lower() == "y"

    if save:
        new_config = {
            "model": model_name,
            "language": lang,
            "device": device,
            "compute": compute,
            "beam": beam,
            "format": fmt,
            "skip": "y" if skip_existing else "n",
            "output_dir": output_dir
        }
        save_config(new_config)
        print("Config saved.")

    print("\nLoading model...")
    model_obj = WhisperModel(
        model_name,
        device=device,
        compute_type=compute
    )

    processed = 0
    skipped = 0

    # -----------------------
    # Batch loop
    # -----------------------

    for file_path in files:
        base = os.path.splitext(os.path.basename(file_path))[0]

        if fmt == "3":
            output_path = os.path.join(output_dir, base + ".srt")
        else:
            output_path = os.path.join(output_dir, base + ".txt")

        # Skip logic
        if skip_existing and os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            print(f"Skipping (already exists): {output_path}")
            skipped += 1
            continue

        transcribe_file(model_obj, file_path, output_path, fmt, lang, beam)
        processed += 1

    print("\nAll files completed.")
    print(f"Processed: {processed}, Skipped: {skipped}")


if __name__ == "__main__":
    main()