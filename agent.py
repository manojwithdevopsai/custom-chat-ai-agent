import os
import subprocess
import sys

GITHUB_REPO = os.getenv("AGENT_GITHUB_REPO")
CLONE_DIR = os.getenv("AGENT_CLONE_DIR")

def run(cmd):
    subprocess.check_call(cmd, shell=True)

def setup():
    print("🚀 Setting up Custom AI Agent")

    if not os.path.exists(CLONE_DIR):
        print("📥 Cloning GitHub repository...")
        run(f"git clone {GITHUB_REPO} {CLONE_DIR}")
    else:
        print("🔄 Updating repository...")
        run(f"cd {CLONE_DIR} && git pull")

    print("📦 Installing dependencies...")
    run(f"{sys.executable} -m pip install -r {CLONE_DIR}/requirements.txt")

def start():
    sys.path.append(CLONE_DIR)
    from agent.main import start_agent
    start_agent()

if __name__ == "__main__":
    setup()
    start()
