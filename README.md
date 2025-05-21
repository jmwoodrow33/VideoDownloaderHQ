# YouTube Video Downloader (High Quality)

This is a simple Python application with a graphical interface that allows you to download high quality YouTube videos. It uses `yt-dlp` to fetch and combine the best video and audio streams, and `ffmpeg` to merge them into a single file.

## Features

- Downloads the best available video and audio quality
- Combines streams into a single `.mp4` file
- Simple Tkinter-based GUI
- Files are saved to a local `downloads/` folder

## Requirements

- Python 3.8 or later
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://www.gyan.dev/ffmpeg/builds/) (must be in system PATH)

## Installation

1. Clone this repository
```sh
git clone https://github.com/jmwoodrow33/VideoDownloaderHQ.git
```
```sh
cd VideoDownloaderHQ
```
2. Install dependencies
```sh
pip install yt-dlp
```
4. Download and extract ffmpeg to the root folder then add it to your system PATH variables
```sh
https://www.gyan.dev/ffmpeg/builds/
'ffmpeg-7.0.2-essentials_build.zip'
```
## Usage

Run the script:
```sh
python ytDownloader.pyw
```
Alternatively you can right click this file in the file explorer and create a desktop shortcut to run the script.

Paste the YouTube URL into the input field and click "Download."  
The video will be saved to the `downloads/` folder as a `.mp4` file.

## Notes

- Only single video URLs are supported (no playlists)
- A list of supported sites can be found at https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md
- The GUI shows download progress and status
- `downloads/` folder is ignored in version control

## License

This project is licensed under the MIT License.

