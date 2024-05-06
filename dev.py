import os
import subprocess

pwd = os.getcwd()

UI_REPO_PATH = os.path.join(pwd, "grid-sim-ui-client")
SERVER_REPO_PATH = os.path.join(pwd, "grid-simulator")

if __name__ == "__main__":
    subprocess.Popen(["python", "server.py"], cwd=SERVER_REPO_PATH)
    subprocess.run(["npm", "run", "dev"], cwd=UI_REPO_PATH)
