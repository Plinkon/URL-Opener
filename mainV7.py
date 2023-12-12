import webbrowser
import time
import subprocess
import configparser
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def open_url_in_browser(url, count):
    for _ in range(count):
        webbrowser.open_new_tab(url)

def close_browser(browser_process_name):
    try:
        subprocess.run(["taskkill", "/F", "/IM", browser_process_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Unable to close tabs for {browser_process_name}. Please close them manually.")

def run_script():
    url_to_open = url_entry.get()
    count = int(count_entry.get())
    browser_process_name = browser_entry.get()
    wait_time = int(wait_time_entry.get())

    open_url_in_browser(url_to_open, count)

    # Wait for specified time before closing the browser
    time.sleep(wait_time)

    close_browser(browser_process_name)

def load_config():
    global config_filename
    config_filename = 'config.ini'

    if os.path.exists(config_filename):
        config = configparser.ConfigParser()
        config.read(config_filename)

        # Check if auto_load is set to true in config.ini
        auto_load = config.getboolean('Settings', 'auto_load', fallback=False)

        if auto_load:
            url_entry.delete(0, tk.END)
            url_entry.insert(0, config.get('Settings', 'url_to_open', fallback=''))
            count_entry.delete(0, tk.END)
            count_entry.insert(0, config.get('Settings', 'count', fallback=1))
            browser_entry.delete(0, tk.END)
            browser_entry.insert(0, config.get('Settings', 'browser_process_name', fallback=''))
            wait_time_entry.delete(0, tk.END)
            wait_time_entry.insert(0, config.get('Settings', 'wait_time', fallback=5))

def load_config_from_file():
    global config_filename
    config_filename = filedialog.askopenfilename(filetypes=[("INI files", "*.ini")])
    if config_filename:
        config = configparser.ConfigParser()
        config.read(config_filename)

        url_entry.delete(0, tk.END)
        url_entry.insert(0, config.get('Settings', 'url_to_open', fallback=''))
        count_entry.delete(0, tk.END)
        count_entry.insert(0, config.get('Settings', 'count', fallback=1))
        browser_entry.delete(0, tk.END)
        browser_entry.insert(0, config.get('Settings', 'browser_process_name', fallback=''))
        wait_time_entry.delete(0, tk.END)
        wait_time_entry.insert(0, config.get('Settings', 'wait_time', fallback=5))

# Set initial config filename
config_filename = 'config.ini'

# Create the main window
root = tk.Tk()
root.title("URL Opener by Plinkon")

# Create and place widgets
frame = ttk.Frame(root, padding=(20, 10))
frame.grid(row=0, column=0, padx=10, pady=10)

url_label = ttk.Label(frame, text="Enter the URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")

url_entry = ttk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="W")

count_label = ttk.Label(frame, text="Enter the count:")
count_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")

count_entry = ttk.Entry(frame, width=10)
count_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")

browser_label = ttk.Label(frame, text="Enter the browser process name:")
browser_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")

browser_entry = ttk.Entry(frame, width=20)
browser_entry.grid(row=2, column=1, padx=5, pady=5, sticky="W")

wait_time_label = ttk.Label(frame, text="Enter the wait time (seconds):")
wait_time_label.grid(row=3, column=0, padx=5, pady=5, sticky="E")

wait_time_entry = ttk.Entry(frame, width=10)
wait_time_entry.grid(row=3, column=1, padx=5, pady=5, sticky="W")

load_config_button = ttk.Button(frame, text="Load Config", command=load_config)
load_config_button.grid(row=4, column=0, pady=10)

load_config_from_file_button = ttk.Button(frame, text="Load Config from File", command=load_config_from_file)
load_config_from_file_button.grid(row=4, column=1, pady=10)

run_button = ttk.Button(frame, text="Run Script", command=run_script)
run_button.grid(row=4, column=2, pady=10)

# Information label at the bottom
info_label = tk.Label(root, text="This is a URL opener project developed by Plinkon. "
                                "There are different options to open a specific URL in different ways. "
                                "There is also an 'auto-close' feature that will automatically close the browser. "
                                "Those options are the last two parameters; you can leave them blank if you want to close the browser manually. "
                                "If you want to know more, check out the GitHub page.",
                     wraplength=700, justify="left")
info_label.grid(row=1, column=0, padx=10, pady=(0, 10))

# Start the GUI event loop
root.mainloop()
