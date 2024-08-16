# CommandsAutomation
Gitlab commits

This script executes the commands in sequence, to pull the remote changes and then commit the local changes to the remote repository.

---

REQUIREMENTS

Have a folder with the name 'Git' directly on your user, and clone all the projects inside this folder.
The path should be C:\Users\Your_User\Git\...individual folders for each cloned project

---

HOW TO CLONE A PROJECT

From inside the Git folder, open a terminal and type the command:
git clone + SSH link

---

HOW CREATING THE EXECUTABLE FILE

- Open the terminal and install with the command:
  pip install pyinstaller
- Command to create the executable (from inside the directory where the main.py script is located):
  pyinstaller --onefile main.py
