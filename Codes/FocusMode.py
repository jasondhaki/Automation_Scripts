import webbrowser
import os
import time
import platform

# --- CONFIGURATION ---

# 1. Websites to open
URLS = [
    "https://gemini.google.com/",
    "https://classroom.google.com/",
    "https://github.com/",
    "https://www.linkedin.com/"
]

# 2. Apps to CLOSE (Distractions)
DISTRACTIONS = [
    "discord.exe",
    "spotify.exe",
    "steam.exe",
    "netflix.exe",
    "whatsapp.exe"
]

# ---------------------

def close_distractions():
    print("🔪 Closing distracting apps...")
    system_name = platform.system()
    
    for app in DISTRACTIONS:
        try:
            if system_name == "Windows":
                # /F = force close, /IM = image name
                os.system(f"taskkill /F /IM {app} >nul 2>&1")
            else:
                # Mac/Linux
                os.system(f"pkill -x {app.replace('.exe', '')}")
        except Exception:
            pass # If the app isn't open, just ignore the error

def open_work_environment():
    print("🚀 Launching VS Code...")
    # This command works if VS Code is installed normally
    if platform.system() == "Windows":
        os.system("code") 
    else:
        os.system("code .")

    print("🌐 Opening tabs in Opera...")
    # Since Opera is default, we just loop through and open them
    for url in URLS:
        webbrowser.open(url) 
        # Small delay to ensure the browser registers the request
        time.sleep(0.5) 

if __name__ == "__main__":
    print("--- STARTING FOCUS MODE ---")
    close_distractions()
    time.sleep(1) 
    open_work_environment()
    print("--- READY TO WORK ---")