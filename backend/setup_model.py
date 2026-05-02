"""
setup_model.py – Download YOLOv8n weights automatically.

Usage:
    python setup_model.py

This script:
1. Creates the `weights/` directory if it doesn't exist.
2. Downloads yolov8n.pt from the official Ultralytics GitHub releases.
3. Saves it as `weights/best.pt`.
4. Skips the download if `weights/best.pt` already exists.
"""

import os
import sys
from pathlib import Path

import requests

WEIGHTS_DIR = Path(__file__).resolve().parent / "weights"
TARGET_PATH = WEIGHTS_DIR / "best.pt"
DOWNLOAD_URL = "https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt"


def download_model() -> None:
    if TARGET_PATH.exists():
        print(f"[✓] Model already exists at {TARGET_PATH}. Skipping download.")
        return

    WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[↓] Downloading YOLOv8n from:\n    {DOWNLOAD_URL}")
    print(f"    Saving to: {TARGET_PATH}")

    try:
        response = requests.get(DOWNLOAD_URL, stream=True, timeout=120)
        response.raise_for_status()

        total = int(response.headers.get("content-length", 0))
        downloaded = 0

        with open(TARGET_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded / total * 100
                    print(f"\r    Progress: {pct:5.1f}%  ({downloaded:,} / {total:,} bytes)", end="", flush=True)

        print(f"\n[✓] Download complete! Model saved to {TARGET_PATH}")

    except requests.RequestException as exc:
        # Clean up partial download
        if TARGET_PATH.exists():
            os.remove(TARGET_PATH)
        print(f"\n[✗] Download failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    download_model()
