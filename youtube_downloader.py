import sys
import yt_dlp
import os
import uuid

def download_video(url, download_audio=False, download_dir=None):
    if not download_dir:
        download_dir = str(uuid.uuid4())  # Create a new folder with a UUID
        os.makedirs(download_dir)

    ydl_opts = {'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s')}

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
        ydl_opts.update({'format': 'bestvideo+bestaudio'})

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Downloaded to: {os.path.abspath(download_dir)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube URL> [mp3] [optional: download directory]")
    else:
        url = sys.argv[1]
        download_audio = len(sys.argv) > 2 and sys.argv[2].lower() == 'mp3'
        download_dir = sys.argv[3] if len(sys.argv) > 3 else None
        download_video(url, download_audio, download_dir)
