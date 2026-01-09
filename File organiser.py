import os
import shutil
from tkinter import filedialog, messagebox
from tkinter import *

file_types ={
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".svg", ".heic"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".flv", ".wmv", ".webm", ".3gp", ".mpeg"],
    "Documents": [".xls", ".xlsx", ".csv", ".ods",".ppt", ".pptx", ".odp"],
    "Archives": [".zip", ".rar", ".gz"],
    "Audios": [".mp3",".wav",".ogg",".aac",".flac",".m4a",".wma",".opus"],
    "Software files": [".exe", ".msi", ".apk", ".dmg", ".pkg", ".app", ".bat", ".sh"],
    "Files": [".txt", ".pdf", ".doc", ".docx", ".rtf", ".odt", ".md", ".tex"],
    "Code files": [".py", ".js", ".ts", ".html", ".css", ".scss",".c", ".cpp", ".h", ".java", ".cs", ".go",
".php", ".rb", ".swift", ".kt", ".rs"],
    "Sql Database files": [".sql", ".sqlite", ".db", ".mdb", ".accdb", ".dbf"]
}

path = ""

def select_path():
    global path
    path = filedialog.askdirectory()

def organise_files():
    global path
    if not path:
        messagebox.showwarning("Warning", "Please select a folder first")
        return

    moved_files = 0
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            continue

        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                folder_path = os.path.join(path, folder)

                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                moved_files += 1
                break

    messagebox.showinfo("Success", f"{moved_files} files organised successfully")

def end_app():
    root.destroy()

root = Tk()
root.title("File Organiser")
root.geometry("600x400")
root.configure(bg="lightgray")

Label(root, text="File Organiser",bg="lightgray", font=("Segoe UI", 25)).pack(pady=10)
Label(root, text="Organise your files in one go ",bg="lightgray", font=("Segoe UI", 13)).pack(pady=10)
Button(root, text="Select Path", command=select_path, width=20,bg="skyblue",fg="white").pack(pady=10)
Button(root, text="Organise Files", command=organise_files, width=20).pack(pady=10)
Button(root, text="End the App", command=end_app, width=20,bg="skyblue",fg="white").pack(pady=10)

root.mainloop()




