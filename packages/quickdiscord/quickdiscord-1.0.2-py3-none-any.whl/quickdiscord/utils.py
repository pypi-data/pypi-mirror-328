from os import makedirs
from subprocess import run
from sys import executable

def create_folder(path):
    makedirs(path, exist_ok=True)

def create_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def install_requirements(packages, path):
    if not executable:
        print("❌ Python executable not found! Make sure Python is installed.")
        return

    print("📦 Installing dependencies...")
    run([executable, "-m", "pip", "install"] + packages, cwd=path)
    print("✅ Dependencies installed!")
