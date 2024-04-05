import tkinter as tk
from tkinter import ttk
import json

def create_notepad(parent, filename):
    notepad = tk.Text(parent)
    notepad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
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
                    notepad.delete("1.0", tk.END)  # Clear existing content before loading
                    notepad.insert(tk.END, data[filename])
    except FileNotFoundError:
        pass  # File doesn't exist yet, so nothing to load

def main():
    root = tk.Tk()
    root.title("Multiple Notepads")

    notepad_frame1 = ttk.Frame(root)
    notepad_frame1.pack(fill=tk.BOTH, expand=True)

    notepad_frame2 = ttk.Frame(root)
    notepad_frame2.pack(fill=tk.BOTH, expand=True)

    file_names = ["notepad1.txt", "notepad2.txt", "notepad3.txt", "notepad4.txt"]
    notepads = []
    for file_name in file_names:
        notepad = create_notepad(notepad_frame1 if len(notepads) < 2 else notepad_frame2, file_name)
        load_file_content(notepad, file_name)  # Load content from the predefined file
        notepads.append(notepad)

    load_all_notepads_content(notepads, file_names)

    save_button_frame = ttk.Frame(root)
    save_button_frame.pack()

    save_button = ttk.Button(save_button_frame, text="Save", command=lambda: save_all_notepads_content(notepads, file_names))
    save_button.pack()

    # Load and display the nethergear.png image
    photo = tk.PhotoImage(file="nethergear.png")
    photo = photo.subsample(10, 10)  # Resize the image by a factor of 10
    label_image = tk.Label(root, image=photo)
    label_image.image = photo  # Keep a reference to avoid garbage collection
    label_image.pack(side=tk.LEFT, padx=10, pady=10)  # Align image to the left

    # Add text labels to the right of the image
    text_label1 = tk.Label(root, text="Nethergear multi Notepad app")
    text_label1.pack(anchor=tk.W, padx=10, pady=10)
    
    text_label2 = tk.Label(root, text="Version 1.06")
    text_label2.pack(anchor=tk.W, padx=10, pady=10)
    
    text_label3 = tk.Label(root, text="23-03-2024")
    text_label3.pack(anchor=tk.W, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
