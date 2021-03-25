import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")

root.title("Colour Tint Converter")
root.geometry('450x400')

# Initialise Tab Parent Notebook
tab_parent = ttk.Notebook(root)

# Define Tabs - MAIN TABS TO REFERENCE
home_frame = ttk.Frame(tab_parent, borderwidth=5, relief="groove")
settings_frame = ttk.Frame(tab_parent, borderwidth=5, relief="groove")
about_frame = ttk.Frame(tab_parent, borderwidth=5, relief="groove")

# Add Tabs to Tab Parent
tab_parent.add(home_frame, text="Home")
tab_parent.add(settings_frame, text="Settings")
tab_parent.add(about_frame, text="About")

# Pack Tabs into Layout
tab_parent.pack(expand=1, fill="both")


class RemovableTint(tk.Frame):
    instances = []

    def __init__(self, parent_frame):
        RemovableTint.instances.append(self)

        tk.Frame.__init__(self, parent_frame, height=5, pady=1)
        self.hex_entry_var = tk.StringVar()
        self.colour_tint_name = tk.Entry(self, width=15, font="Calibri")
        self.r_spin = tk.Entry(self, width=4, font="Calibri")
        self.g_spin = tk.Entry(self, width=4, font="Calibri")
        self.b_spin = tk.Entry(self, width=4, font="Calibri")
        self.hex_spin = tk.Entry(self, width=10, font="Calibri", textvariable=self.hex_entry_var)
        self.update = tk.Button(self, text="Update", font="Calibri", command=self.hex_conversion)
        self.remove = tk.Button(self, font="Calibri", text="X", command=self.remove)

        self.colour_tint_name.pack(fill="both", side="left", expand=True)
        self.r_spin.pack(fill="both", side="left")
        self.g_spin.pack(fill="both", side="left")
        self.b_spin.pack(fill="both", side="left")
        self.hex_spin.pack(fill="both", side="left")
        self.update.pack(fill="both", side="left")
        self.remove.pack(fill="both", side="left")

    def hex_conversion(self):
        # TODO: Combine with Alex's function
        hex_value = "DUMMYFFFFFFF"
        self.hex_entry_var.set(hex_value)

    def remove(self):
        RemovableTint.instances.remove(self)
        self.destroy()
        print(self.instances)


# Add frame instance (dynamic addition of widgets)
def add_frame():
    RemovableTint(home_frame).pack(fill=tk.X)
    print(RemovableTint.instances)


def fetch_all():
    # TODO: loop through instances to fetch all data
    for i in RemovableTint.instances:
        print(i)
    pass


btn = tk.Button(home_frame, text="Add Entry", width=50, command=add_frame)


btn.pack(side="bottom", fill=tk.X)
home_frame.mainloop()