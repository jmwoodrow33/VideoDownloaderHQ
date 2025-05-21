import os
import tkinter as tk
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Ensure downloads folder exists
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        status_label.config(text=f"Downloading: {downloaded} at {speed} (ETA: {eta})")
        root.update_idletasks()
    elif d['status'] == 'finished':
        status_label.config(text="Download finished, finalizing...")
        root.update_idletasks()

def download_video():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return

    download_button.config(state="disabled")
    status_label.config(text="Downloading... Please wait.")

    ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    'noplaylist': True,
    'progress_hooks': [progress_hook],
    'quiet': True,
    'no_warnings': True
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\n{str(e)}")
        status_label.config(text="Download failed.")
    finally:
        download_button.config(state="normal")

# Set up GUI
root = tk.Tk()
root.title("YouTube Downloader (High Quality)")
root.geometry("500x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Enter YouTube Video URL:").pack(anchor="w")
url_entry = tk.Entry(frame, width=60)
url_entry.pack(pady=5)

download_button = tk.Button(frame, text="Download", command=download_video, width=20)
download_button.pack(pady=10)

status_label = tk.Label(frame, text="", anchor="w", wraplength=460, justify="left")

status_label.pack()

root.mainloop()
