from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("881x603")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 603,
    width = 881,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    437.5, 301.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    635.5, 135.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d3d3d3",
    highlightthickness = 0)

entry0.place(
    x = 431, y = 120,
    width = 409,
    height = 28)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    636.5, 338.5,
    image = entry1_img)

entry1 = Text(
    bd = 0,
    bg = "#d3d3d3",
    highlightthickness = 0)

entry1.place(
    x = 432, y = 202,
    width = 409,
    height = 271)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 431, y = 517,
    width = 409,
    height = 33)

window.resizable(False, False)
window.mainloop()
