import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Colour Tint Converter")
root.geometry('450x400')

tab_control = ttk.Notebook()
main = ttk.Frame(tab_control, borderwidth=5)
main_content_1 = ttk.Frame(main, borderwidth=10, relief="groove")

tab_control.add(main, text='Main')
main_content_1.grid(column=1, row=2)

tab_control.pack(side="left", expand="yes", fill='both')

Colour_Tint_Name = tk.Entry(main_content_1, width=18, font="Calibri")
Colour_Tint_Name.grid(column=1, row=2)

R_SV = tk.StringVar()

root.wm_attributes("-topmost", 1)
root.mainloop()