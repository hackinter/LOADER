import os
import requests
from yt_dlp import YoutubeDL
import instaloader

# App Version and Developer Credit
VERSION = "1.0.0"
DEVELOPER = "HACKINTER"

# ASCII Art
ascii_art = """
██       ██████   █████  ██████  ███████ ██████  
██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
██      ██    ██ ███████ ██   ██ █████   ██████  
██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
███████  ██████  ██   ██ ██████  ███████ ██   ██ 
"""

# File Save Location Picker
def choose_save_location():
    folder_path = input("📂 Enter the folder path to save (Press Enter to use current directory): ").strip()
    if not folder_path or not os.path.isdir(folder_path):
        print("⚠️ Invalid path. Using current directory.")
        folder_path = os.getcwd()
    return folder_path

# Download from YouTube
def download_youtube(link, format_choice):
    save_location = choose_save_location()
    ydl_opts = {
        'outtmpl': f'{save_location}/%(title)s.%(ext)s',
    }

    if format_choice.lower() in ['video', 'v']:
        ydl_opts['format'] = 'best'
    elif format_choice.lower() in ['audio', 'a']:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        print("⚠️ Invalid option! Please select 'video' or 'audio'.")
        return

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# Download from Instagram
def download_instagram(link):
    save_location = choose_save_location()
    L = instaloader.Instaloader()
    
    try:
        post = instaloader.Post.from_shortcode(L.context, link.split("/")[-2])
        L.download_post(post, target=save_location)
    except Exception as e:
        print(f"❌ Instagram download failed: {e}")

# Download from TikTok
def download_tiktok(link):
    save_location = choose_save_location()
    response = requests.get(f"https://api.tikmate.app/v1/video?url={link}").json()
    video_url = response.get('video_url')
    if video_url:
        video_response = requests.get(video_url)
        with open(f"{save_location}/tiktok_video.mp4", "wb") as f:
            f.write(video_response.content)
        print("✅ TikTok video downloaded successfully!")
    else:
        print("❌ TikTok download failed.")

# Download from Facebook
def download_facebook(link):
    save_location = choose_save_location()
    video_url = f"https://www.facebook.com/watch/?v={link.split('/')[-1]}"
    response = requests.get(video_url)
    
    if response.status_code == 200:
        with open(f"{save_location}/facebook_video.mp4", "wb") as f:
            f.write(response.content)
        print("✅ Facebook video downloaded successfully!")
    else:
        print("❌ Facebook download failed. Check if the video is publicly available.")

if __name__ == "__main__":
    print(ascii_art)  # Print ASCII Art
    print("🌐 Welcome to LOADER!")
    print(f"⚙️ Tool Version: {VERSION}")
    print(f"👤 Created by: {DEVELOPER}\n")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("📱 Choose platform:")
    print("  Y - YouTube")
    print("  I - Instagram")
    print("  T - TikTok")
    print("  F - Facebook")
    
    platform = input("Select a platform (Y/I/T/F): ").strip().upper()
    link = input("🔗 Enter the link: ")

    if platform == 'Y':
        format_choice = input("🎥 Video or 🎵 Audio format? (video/v, audio/a): ")
        download_youtube(link, format_choice)
    elif platform == 'I':
        download_instagram(link)
    elif platform == 'T':
        download_tiktok(link)
    elif platform == 'F':
        download_facebook(link)
    else:
        print("⚠️ Invalid platform selected.")

print("© 2024 HACKINTER. All rights reserved.")
