import tkinter as tk
from tkinter import ttk

def create_notepad(parent):
    notepad = tk.Text(parent)
    notepad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    return notepad

def main():
    root = tk.Tk()
    root.title("Four Notepads")

    notepad_frame = ttk.Frame(root)
    notepad_frame.pack(fill=tk.BOTH, expand=True)

    notepads = []
    for _ in range(4):
        notepads.append(create_notepad(notepad_frame))

    root.mainloop()

if __name__ == "__main__":
    main()
