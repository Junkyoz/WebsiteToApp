import tkinter as tk
import os
import sys
import shutil
import os
from pathlib import Path

def copy_file_to_desktop(source_path, destination_filename):
    # Erstelle den Ziel-Dateipfad auf dem Desktop
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    destination_path = desktop_path / destination_filename

    try:
        # Kopiere die Datei
        shutil.copy2(source_path, destination_path)
        print(f'Datei erfolgreich nach {destination_path} kopiert.')
    except FileNotFoundError:
        print(f'Fehler: Die Quelldatei {source_path} wurde nicht gefunden.')
    except PermissionError:
        print(f'Fehler: Keine Berechtigung, um die Datei nach {destination_path} zu kopieren.')
source_file_path = './browser/Browser.lnk'  # Passe den Pfad entsprechend an
destination_filename = 'Browser.lnk'

def edit():
    copy_file_to_desktop(source_file_path, destination_filename)
    current_directory = os.getcwd()
    with open(os.path.join(current_directory, 'browser', 'name.txt'), 'w') as f1:
        f1.write(name_entry.get())
    with open(os.path.join(current_directory, 'browser', 'website.txt'), 'w') as f2:
        f2.write(website_entry.get())

    root.destroy()
    sys.exit()

root = tk.Tk()
root.geometry('300x200')
root.title('setup')
root.resizable(False, False)

label1 = tk.Label(root, text='Put the name of the website', font=("Arial", 15))
name_entry = tk.Entry(root, width=30)
label2 = tk.Label(root, text='Put in the URL of the website', font=("Arial", 15))
website_entry = tk.Entry(root, width=30)
button = tk.Button(root, text='FINISH', command=edit)

label1.pack(pady=10)
name_entry.pack()
label2.pack(pady=10)
website_entry.insert(0, 'https://www.')
website_entry.pack()
button.pack(pady=20)

root.mainloop()