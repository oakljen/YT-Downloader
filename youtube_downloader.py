import sys
import yt_dlp

def download_video(url, download_audio=False):
    ydl_opts = {}

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube URL> [mp3]")
    else:
        url = sys.argv[1]
        download_audio = len(sys.argv) > 2 and sys.argv[2].lower() == 'mp3'
        download_video(url, download_audio)
