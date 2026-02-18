# Photo slideshow project
import tkinter as tk
import time
from PIL import Image, ImageTk

# Main application windwow
root=tk.Tk()
root.title("Photo slideshow album")
root.geometry("900x600")

# List of image paths
image_paths = [
    r"C:\s21photos\20240218_183234.jpg",
    r"C:\s21photos\20240218_183308.jpg",
    r"C:\s21photos\20240218_183345.jpg",
    r"C:\s21photos\20240428_133727.jpg",
    r"C:\s21photos\20240516_213741.jpg" 
]
image_size = (800,800)
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img) # adding each image in the list 

#convert PIL images into tkinter compatible image 
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

#Slideshow function
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

    # button

play_button = tk.Button(
    root,
    text="Play the slideshow",
    font=("Arial",17),
    command=start_slideshow
)
play_button.pack()
root.mainloop()