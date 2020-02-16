from tkinter import *
import PIL.Image
import PIL.ImageTk

root = Toplevel()

im = PIL.Image.open("PNG/2H.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()


Image.geometry("100x100")
root.mainloop()
