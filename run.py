import os
import subprocess

pwd = os.getcwd()

UI_REPO_PATH = os.path.join(pwd, "grid-sim-ui-client")
SERVER_REPO_PATH = os.path.join(pwd, "grid-simulator")

if __name__ == "__main__":
    subprocess.run(["npm", "install"], cwd=UI_REPO_PATH)
    subprocess.run(["npm", "run", "build"], cwd=UI_REPO_PATH)
    subprocess.Popen(["npm", "run", "preview"], cwd=UI_REPO_PATH)

    subprocess.run(["python", "server.py"], cwd=SERVER_REPO_PATH)
