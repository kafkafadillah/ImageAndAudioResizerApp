import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import subprocess

class SimpleApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Resize Foto & Kompres Audio")

        self.label = tk.Label(master, text="Welcome!")
        self.label.pack()

        self.photo_button = tk.Button(master, text="Choose Photo", command=self.resize_photo)
        self.photo_button.pack()

        self.audio_button = tk.Button(master, text="Choose Audio", command=self.compress_audio)
        self.audio_button.pack()

    def resize_photo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                img = Image.open(file_path)
                # Konversi ke mode RGB
                img = img.convert("RGB")
                img = img.resize((200, 200), Image.LANCZOS)
                img.save("resized_image.jpg")
                self.label.config(text="Successed!")
            except Exception as e:
                self.label.config(text="Error: " + str(e))

    def compress_audio(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                # Tambahkan lokasi ffmpeg ke dalam PATH
                os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"
                subprocess.call(["ffmpeg", "-i", file_path, "-b:a", "128k", "compressed_audio.mp3"])
                self.label.config(text="Successed!")
            except Exception as e:
                self.label.config(text="Error: " + str(e))

root = tk.Tk()
app = SimpleApp(root)
root.mainloop()
