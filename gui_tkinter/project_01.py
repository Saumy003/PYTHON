# First project using Tkinter => Wallpaper viewer

from tkinter import * 
from PIL import ImageTk, Image
import os

def rotate_image():
    global counter
    img_label.config(image = img_array[counter%len(img_array)])
    counter += 1

counter = 1


root = Tk()

root.title("Wallpapers Viwer")
root.iconbitmap("D:\\PYTHON\\gui_tkinter\\Flipkart_logo_(2026).svg")

root.minsize(100, 100)
root.geometry("300x400")
root.configure(background="black")

files = os.listdir("D:\\PYTHON\\gui_tkinter\\wallpaper")

img_array = []
for file in files:
    img = Image.open(os.path.join("D:\\PYTHON\\gui_tkinter\\wallpaper", file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image=img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root, text="Next", bg="white", fg="black", width=25, height=2, command=rotate_image)
next_btn.pack()



root.mainloop()