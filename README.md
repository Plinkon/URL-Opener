# How to Run and Properly Use the URL Opener

## 1. Open url-opener.exe

## 2. Input Variables or Use a Config File

### Variable Name/ Meanings:

| Enter the URL:                    | Type in a URL like https://google.com                           |
| ---------------------------------- | --------------------------------------------------------------- |
| Enter the count:                   | Type in the amount of tabs you want to open                     |
| Enter the browser process name:    | Enter the browser process name, for example: chrome.exe         |
|                                    | (Scroll down for a tutorial on how to find the process name)   |
| Enter the wait time (seconds):     | Enter the amount of seconds before the browser closes          |
|                                    | (Leave blank if you want to close manually)                     |

## 3. Load Config

- Basically looks for an INI file named "config.ini" and tries to find values automatically.

## 4. Load Config from File

- Choose a file to load a config.

## 5. Run Script

- Runs the script.

---

## Tutorial for How to Find Browser Process Name:

1. Open your default browser.
2. Go into the task manager.
3. Navigate to the "Details" tab.
4. Find your browser icon and look at the name next to it.

### List of Browser Process Names:

- Google Chrome: `chrome.exe`
- Opera/OperaGX: `opera.exe`
- Microsoft Edge: `msedge.exe`
- Brave: `brave.exe`
- Mozilla Firefox: `firefox.exe` (Not Checked)
- Tor: `firefox.exe` (Not Checked, Might be something like: `tor.exe`)
