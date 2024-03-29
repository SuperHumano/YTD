import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

# function called in the download button
def download():
    video_url = url.get()  # Get url from Entry field
    try:
        video = YouTube(video_url).streams.get_highest_resolution() # getting the youtube video with the highest resolution
        download_directory = filedialog.askdirectory()  # Ask user for directory
        video.download(download_directory)  # Download video to chosen directory
        download_message.set("Download completed!")
        message_label.config(fg='green')

    except:
        download_message.set("*Error: Please set a valid url")
        message_label.config(fg='red')

# creating the tkinter window
root = tk.Tk()
root.title('YTD')
root.geometry('500x300')
label = tk.Label(root, text='YouTube Downloader', font=('Arial', 18))

# Setting string objects as instances of Tkinter's StringVar, which provides an automatic update feature
url = tk.StringVar()
download_message = tk.StringVar()

# placing the location of the StringVars and setting the download button
url_entry = tk.Entry(root, textvariable=url)
download_button = tk.Button(root, text="Download", font=('Arial', 16), command=download)
message_label = tk.Label(root, textvariable=download_message)

# packing the elements in sequence
label.pack(padx=10, pady=15)
url_entry.pack(padx=10)
download_button.pack(padx=10, pady=10)
message_label.pack()

root.mainloop()
