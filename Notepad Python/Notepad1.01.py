import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def create_notepad(parent):
    notepad = tk.Text(parent)
    notepad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    return notepad

def save_notepad_changes(notepad, file_path):
    text_content = notepad.get("1.0", tk.END)
    with open(file_path, "w") as file:
        file.write(text_content)

def save_file(notepad):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        save_notepad_changes(notepad, file_path)

def main():
    root = tk.Tk()
    root.title("Four Notepads")

    notepad_frame1 = ttk.Frame(root)
    notepad_frame1.pack(fill=tk.BOTH, expand=True)

    notepad_frame2 = ttk.Frame(root)
    notepad_frame2.pack(fill=tk.BOTH, expand=True)

    notepads = []
    for _ in range(2):
        notepad1 = create_notepad(notepad_frame1)
        notepads.append(notepad1)

        notepad2 = create_notepad(notepad_frame2)
        notepads.append(notepad2)

    save_button_frame = ttk.Frame(root)
    save_button_frame.pack()

    save_button = ttk.Button(save_button_frame, text="Save", command=lambda: save_file(notepads[0]))
    save_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
