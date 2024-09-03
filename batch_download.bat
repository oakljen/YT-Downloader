@echo off
set /p format="Download as MP3? (y/n): "

for /f "tokens=*" %%A in (urls.txt) do (
    echo Downloading %%A...
    if /i "%format%"=="y" (
        python youtube_downloader.py "%%A" mp3
    ) else (
        python youtube_downloader.py "%%A"
    )
)

echo All downloads complete.
pause
