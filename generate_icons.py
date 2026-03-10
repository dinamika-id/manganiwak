#!/usr/bin/env python3
"""
generate_icons.py
Resizes icon_source.png into all required Android mipmap sizes
and places them in the correct res/mipmap-* directories.
Also copies a high-res version for the splash screen drawable.
"""

from PIL import Image
import os
import shutil

SOURCE = "icon_source.png"

# Android mipmap sizes for launcher icons
MIPMAP_SIZES = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}

# Splash screen image size (placed in drawable-xxhdpi for high quality)
SPLASH_SIZE = 512

RES_DIR = os.path.join("android", "app", "src", "main", "res")
DRAWABLE_DIR = os.path.join(RES_DIR, "drawable")

def main():
    if not os.path.exists(SOURCE):
        print(f"ERROR: {SOURCE} not found in project root.")
        return

    img = Image.open(SOURCE).convert("RGBA")
    print(f"Source image size: {img.size}")

    # Generate mipmap icons
    for folder, size in MIPMAP_SIZES.items():
        out_dir = os.path.join(RES_DIR, folder)
        os.makedirs(out_dir, exist_ok=True)

        resized = img.resize((size, size), Image.LANCZOS)

        # Save as ic_launcher.png
        launcher_path = os.path.join(out_dir, "ic_launcher.png")
        resized.save(launcher_path, "PNG")
        print(f"  Saved {launcher_path} ({size}x{size})")

        # Save as ic_launcher_round.png (same image, Android uses it for round icons)
        round_path = os.path.join(out_dir, "ic_launcher_round.png")
        resized.save(round_path, "PNG")
        print(f"  Saved {round_path} ({size}x{size})")

    # Generate splash screen image (512x512) into drawable
    os.makedirs(DRAWABLE_DIR, exist_ok=True)
    splash_img = img.resize((SPLASH_SIZE, SPLASH_SIZE), Image.LANCZOS)
    splash_path = os.path.join(DRAWABLE_DIR, "splash_logo.png")
    splash_img.save(splash_path, "PNG")
    print(f"\n  Saved splash logo: {splash_path} ({SPLASH_SIZE}x{SPLASH_SIZE})")

    print("\nDone! All icons generated successfully.")

if __name__ == "__main__":
    main()
