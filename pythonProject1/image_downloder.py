import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import requests
from PIL import Image
from io import BytesIO
import base64


def Browse():
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Image")
    if download_directory:
        download_Path.set(download_directory)


def Download():
    try:
        image_url = image_Link.get()
        download_folder = download_Path.get()
        if image_url.strip() == "":
            raise ValueError("Please enter an image URL")

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(image_url, headers=headers)
        # Decode base64 string into bytes


        print(response.status_code)

        if response.status_code != 200:
            raise ValueError("Failed to download image: HTTP Status Code " + str(response.status_code))
        # print(response.content)

        image_data_bytes = base64.b64decode(response.content)
        image_data = BytesIO(image_data_bytes)
        # Open the image from bytes
        image = Image.open(image_data)

        # Save the image
        image_filename = "downloaded_image.png"
        image.save(download_folder + "/" + image_filename)

        messagebox.showinfo("Success", "Downloaded Image Saved in\n" + download_folder)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        print(e)


def Widgets():
    head_label = Label(root, text="Image Downloader Using Tkinter ",
                       padx=15, pady=15, font="SegoeUI 14",
                       bg="palegreen1", fg="red")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    link_label = Label(root, text="Image URL :", bg="salmon", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=35, textvariable=image_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Destination", bg="salmon", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Browse", command=Browse, width=10, bg="bisque", relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    Download_B = Button(root, text="Download Image", command=Download, width=20, bg="thistle", pady=10, padx=15)
    Download_B.grid(row=4, column=1, pady=20, padx=20)


root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("Image Downloader")
root.config(background="PaleGreen1")
image_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
