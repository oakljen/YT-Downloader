@echo off
set /p url="Enter the YouTube URL: "
set /p format="Download as MP3? (y/n): "

if /i "%format%"=="y" (
    python youtube_downloader.py "%url%" mp3
) else (
    python youtube_downloader.py "%url%"
)

pause
