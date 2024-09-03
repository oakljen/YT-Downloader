@echo off
set /p url="Enter the YouTube URL (or leave blank to use urls.txt): "
set /p format="Download as MP3? (y/n): "
set /p download_dir="Enter the download directory (leave blank for auto-generated): "

if "%url%"=="" (
    for /f "tokens=*" %%A in (urls.txt) do (
        echo Downloading %%A...
        if /i "%format%"=="y" (
            python youtube_downloader.py "%%A" mp3 "%download_dir%"
        ) else (
            python youtube_downloader.py "%%A" "%download_dir%"
        )
    )
) else (
    echo Downloading %url%...
    if /i "%format%"=="y" (
        python youtube_downloader.py "%url%" mp3 "%download_dir%"
    ) else (
        python youtube_downloader.py "%url%" "%download_dir%"
    )
)

echo All downloads complete.
pause
