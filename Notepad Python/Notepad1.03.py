import tkinter as tk
from tkinter import ttk
import json

def create_notepad(parent, filename):
    notepad = tk.Text(parent)
    notepad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    load_file_content(notepad, filename)  # Load content from the predefined file
    return notepad

def load_file_content(notepad, filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            notepad.insert(tk.END, content)
    except FileNotFoundError:
        pass  # File doesn't exist yet, so nothing to load

def save_notepad_changes(notepad, filename):
    text_content = notepad.get("1.0", tk.END)
    with open(filename, "w") as file:
        file.write(text_content)

def save_all_notepads_content(notepads, filenames):
    data = {}
    for notepad, filename in zip(notepads, filenames):
        data[filename] = notepad.get("1.0", tk.END)
    with open("notepads_data.json", "w") as file:
        json.dump(data, file)

def load_all_notepads_content(notepads, filenames):
    try:
        with open("notepads_data.json", "r") as file:
            data = json.load(file)
            for notepad, filename in zip(notepads, filenames):
                if filename in data:
                    notepad.insert(tk.END, data[filename])
    except FileNotFoundError:
        pass  # File doesn't exist yet, so nothing to load

def main():
    root = tk.Tk()
    root.title("Four Notepads")

    notepad_frame1 = ttk.Frame(root)
    notepad_frame1.pack(fill=tk.BOTH, expand=True)

    notepad_frame2 = ttk.Frame(root)
    notepad_frame2.pack(fill=tk.BOTH, expand=True)

    file_names = ["notepad1.txt", "notepad2.txt", "notepad3.txt", "notepad4.txt"]
    notepads = []
    for file_name in file_names:
        notepad = create_notepad(notepad_frame1 if len(notepads) < 2 else notepad_frame2, file_name)
        notepads.append(notepad)

    load_all_notepads_content(notepads, file_names)

    save_button_frame = ttk.Frame(root)
    save_button_frame.pack()

    save_button = ttk.Button(save_button_frame, text="Save", command=lambda: save_all_notepads_content(notepads, file_names))
    save_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
