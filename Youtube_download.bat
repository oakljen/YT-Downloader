@echo off
set /p url="Enter the YouTube URL (or leave blank to use urls.txt): "
set /p format="Download as MP3? (y/n): "
set /p download_dir="Enter the download directory (leave blank for current folder or auto-generated for batch): "

REM If no URL is provided, batch mode is activated, and a folder is created if not specified
if "%url%"=="" (
    if "%download_dir%"=="" (
        set "download_dir=%~dp0batch-downloads"
        mkdir "%download_dir%"
    )

    echo Downloading videos from urls.txt to "%download_dir%"
    for /f "tokens=*" %%A in (urls.txt) do (
        echo Downloading %%A...
        if /i "%format%"=="y" (
            python youtube_downloader.py "%%A" mp3 "%download_dir%" batch
        ) else (
            python youtube_downloader.py "%%A" "%download_dir%" batch
        )
    )
) else (
    echo Downloading single video %url%...
    if /i "%format%"=="y" (
        python youtube_downloader.py "%url%" mp3 "%download_dir%"
    ) else (
        python youtube_downloader.py "%url%" "%download_dir%"
    )
)

echo All downloads complete.
pause
