Sizy – Disk Usage Analyzer

Sizy is a simple Python app that scans a folder and lists the largest items inside. Works on Windows, macOS, and Linux. Free and open for everyone.

Features
Shows the top 10 largest files and folders in a folder.
Handles files and directories recursively.
Human-readable sizes (B, KB, MB, GB, TB).
Ignores files/folders you don’t have permission to access.
Cross-platform: Works on Windows, macOS, and Linux with Python 3.8+.
Installation
Make sure Python 3.8 or higher is installed:
Windows: Python Download
macOS/Linux: Usually pre-installed; or install via your package manager.
Download sizy.py (your script file).
Usage
Open a terminal or command prompt.
Navigate to the folder where sizy.py is saved.

Run the script:

python sizy.py

(On macOS/Linux, you may need python3 sizy.py)

Paste the folder path you want to analyze when prompted.
Wait for the scan to finish – the top 10 largest items will be displayed.
Notes
If a folder contains protected files, they will be skipped automatically.
Works best on folders with readable permissions.

Optional: On macOS/Linux, make it directly executable:

chmod +x sizy.py
./sizy.py
License

This app is free to use, share, and modify. No payment required.
