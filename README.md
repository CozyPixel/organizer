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

## ⚙️ How to set up Auto-Run (Windows)

If you want Windows to clean up your Downloads folder automatically every time you turn on your PC:

1. Press the **Win** key and type `Task Scheduler`. Open it.
2. In the right panel, click **Create Basic Task...**
3. **Name:** Enter `Downloads Organizer` and click *Next*.
4. **Trigger:** Select **When I log on** and click *Next*.
5. **Action:** Select **Start a program** and click *Next*.
6. **Program/script:** Click *Browse* and select your `organizer.py` file.
7. Click *Next* and then *Finish*.

Now, the script will run silently in the background every time you start your computer!
