# Downloads Organizer 🧹

A simple Python script that automatically moves files from your **Downloads** folder to the standard Windows folders (`Pictures`, `Documents`, etc.) based on their extensions.

## ✨ Features
* **Auto-Sorting:** Cleans up your Downloads folder in one click.
* **Smart Placement:** Sends files directly to native Windows folders.
* **Safe:** Skips unknown formats (like `.zip` or `.exe`) to avoid clutter.

## 🚀 How to Use

### 1. Prerequisites
Install Python from [python.org](https://www.python.org/).  
*⚠️ Make sure to check **"Add python.exe to PATH"** during installation.*

### 2. Setup
1. Copy the `organizer.py` file to your PC.
2. Open it in a text editor and replace `'YourUsername'` with your actual Windows account name:
```python
DOWNLOADS_DIR = r'C:\Users\YourUsername\Downloads'
