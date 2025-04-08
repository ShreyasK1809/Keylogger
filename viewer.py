# viewer.py
import os

def list_logs():
    print("\n📄 Available Logs:")
    files = os.listdir("logs")
    if not files:
        print("No logs found.")
        return None
    for i, file in enumerate(files):
        print(f"[{i}] {file}")
    return files

def view_log(file):
    with open(f"logs/{file}", "r") as f:
        content = f.read()
    print("\n--- Log Content ---\n")
    print(content)

if __name__ == "__main__":
    files = list_logs()
    if files:
        choice = int(input("Select a file number to view: "))
        if 0 <= choice < len(files):
            view_log(files[choice])
        else:
            print("Invalid selection.")
