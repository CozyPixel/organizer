# Downloads Organizer 🧹

A simple and effective Python script that automatically keeps your PC clean by moving files from your **Downloads** folder to the standard Windows user folders based on their file extensions.

## ✨ Features
* **Automatic Sorting:** No more messy Downloads folder.
* **Native Windows Integration:** Moves files directly to your official `Pictures`, `Documents`, `Videos`, and `Music` folders.
* **Safe Execution:** Skips unknown file types (like `.exe` or `.zip`) to keep your main system folders clutter-free.

## 🚀 How to Use

### 1. Prerequisites
Make sure you have Python installed on your computer. If not, download it from [python.org](https://www.python.org/). 
*⚠️ Don't forget to check the **"Add python.exe to PATH"** box during installation!*

### 2. Setup
1. Download or copy the `organizer.py` file to your computer.
2. Open the file in any text editor (like Notepad or VS Code).
3. Find the lines with folder paths and replace `'YourUsername'` with your actual Windows account name:
```python
DOWNLOADS_DIR = r'C:\Users\YourUsername\Downloads'
PICTURES_DIR  = r'C:\Users\YourUsername\Pictures'
# ... and so on for other paths# organizer
