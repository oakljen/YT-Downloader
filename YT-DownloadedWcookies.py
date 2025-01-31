import sys
import yt_dlp
import os
import re

# Path to your cookies.txt file
COOKIES_PATH = "cookies.txt"

def clean_url(url):
    """Removes the 't=' parameter from the URL if present."""
    return re.sub(r'&?t=\d+', '', url)

def download_video(url, download_audio=False, download_dir=None, batch_mode=False, quality=None):
    # Clean the URL to remove the 't' parameter
    url = clean_url(url)

    if not download_dir:
        download_dir = os.getcwd()  # Use current directory if no folder is provided

    # Ensure the directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Setting the format options based on quality
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'cookies': COOKIES_PATH  # Add cookies support
    }

    if download_audio:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        if quality:
            ydl_opts.update({'format': f'bestvideo[height<={quality}]+bestaudio/best'})
        else:
            ydl_opts.update({'format': 'bestvideo+bestaudio'})

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Downloaded to: {os.path.abspath(download_dir)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube URL> [mp3] [optional: download directory] [optional: batch_mode] [optional: quality]")
    else:
        url = sys.argv[1]
        download_audio = len(sys.argv) > 2 and sys.argv[2].lower() == 'mp3'
        download_dir = sys.argv[3] if len(sys.argv) > 3 else None
        batch_mode = len(sys.argv) > 4 and sys.argv[4].lower() == 'batch'
        quality = sys.argv[5] if len(sys.argv) > 5 else None
        download_video(url, download_audio, download_dir, batch_mode, quality)
