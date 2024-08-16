import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog

## p/ digitar a descrição do commit
def get_commit_message():
    root = tk.Tk()
    root.withdraw()
    
    commit_message = simpledialog.askstring("Commit description", "Enter your description:")
    
    if commit_message is None or commit_message.strip() == "":
        print("No description provided - Aborting the commit.")
        sys.exit(1)
    
    return commit_message

## p/ selecionar a pasta
def select_directory():
    root = tk.Tk()
    root.title("Select a folder")

    user_name = os.getlogin()  # testar tbm com os.environ['USERNAME']
    base_dir = f'C:\\Users\\{user_name}\\GitLab'
    
    if not os.path.isdir(base_dir):
        messagebox.showerror("Error", f"The directory {base_dir} not exist.")
        sys.exit(1)
    
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    folders.insert(0, 'Select a folder')
    selected_folder = tk.StringVar(value='Select a folder')
    # menu suspenso com as pastas
    tk.Label(root, text="Choose a folder:").pack(padx=10, pady=5)
    tk.OptionMenu(root, selected_folder, *folders).pack(padx=10, pady=5)

    def confirm_selection():
        folder = selected_folder.get()
        if folder == 'Select a folder':
            messagebox.showwarning("WARNING", "You must select a folder.")
        else:
            root.destroy()
            return folder

    tk.Button(root, text="Confirm", command=confirm_selection).pack(padx=10, pady=10)
    root.mainloop()
    
    return selected_folder.get()

## roda os comandos do git em sequencia
def run_git_commands():
    user_name = os.getlogin()
    folder = select_directory()
    
    repo_dir = f'C:\\Users\\{user_name}\\GitLab\\{folder}'
    commit_message = get_commit_message()
    
    git_commands = [
        'Set-Location', '-Path', repo_dir,
        ';', 'git', 'fetch', 'origin', 'main',
        ';', 'git', 'merge', '--strategy-option=ours', 'origin/main'
        ';', 'git', 'add', '.',
        ';', 'git', 'commit', '-m', f'"{commit_message}"',
        ';', 'git', 'push'
    ]
    terminal_command = ['powershell', '-NoExit', '-Command'] + [' '.join(git_commands)]
    
    try:
        subprocess.run(terminal_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_git_commands()
