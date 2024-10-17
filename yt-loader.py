import os
import time
from yt_dlp import YoutubeDL

# App Version and Developer Credit
VERSION = "1.0.0"
DEVELOPER = "HACKINTER"

# ASCII Art
ascii_art = """
  ██    ██ ████████       ██       ██████   █████  ██████  ███████ ██████  
   ██  ██     ██          ██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
    ████      ██    █████ ██      ██    ██ ███████ ██   ██ █████   ██████  
     ██       ██          ██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
     ██       ██          ███████  ██████  ██   ██ ██████  ███████ ██   ██   
"""

# File Save Location Picker
def choose_save_location():
    folder_path = input("📂 Enter the folder path to save (Press Enter to use current directory): ").strip()
    if not folder_path or not os.path.isdir(folder_path):
        print("⚠️ Invalid path. Using current directory.")
        folder_path = os.getcwd()
    return folder_path

# Download YouTube video or audio
def download_youtube(link, format_choice, resolution):
    save_location = choose_save_location()
    ydl_opts = {
        'outtmpl': f'{save_location}/%(title)s.%(ext)s',
        'format': resolution,
    }

    with YoutubeDL(ydl_opts) as ydl:
        print("📥 Downloading... [", end="")
        for i in range(10):  # Animation loop
            time.sleep(0.2)  # Delay for animation effect
            print("█", end="")
        print("]")  # End of animation
        ydl.download([link])

if __name__ == "__main__":
    print(ascii_art)  # Print ASCII Art
    print("🌐 Welcome to LOADER!")
    print(f"⚙️ Tool Version: {VERSION}")
    print(f"👤 Created by: {DEVELOPER}\n")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    link = input("🔗 Enter the YouTube link: ")

    # Format selection: Video or Audio
    format_choice = input("🎥 Video or 🎵 Audio format? (video/v, audio/a): ").strip().lower()
    if format_choice in ['video', 'v']:
        format_choice = 'bestvideo'
    elif format_choice in ['audio', 'a']:
        format_choice = 'bestaudio'
    else:
        print("⚠️ Invalid format selected.")
        exit(1)

    # Resolution selection
    resolution = input("🔍 Choose resolution (480p, 720p, 1080p, 1440p): ").strip()

    # Mapping resolution input to yt-dlp format
    resolution_map = {
        "480p": "best[height<=480]",
        "720p": "best[height<=720]",
        "1080p": "best[height<=1080]",
        "1440p": "best[height<=1440]",
    }

    if resolution in resolution_map:
        download_youtube(link, format_choice, resolution_map[resolution])
    else:
        print("⚠️ Invalid resolution selected.")

print("© 2024 HACKINTER. All rights reserved.")
