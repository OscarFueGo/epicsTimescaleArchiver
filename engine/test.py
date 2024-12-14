import subprocess
def executeCommand(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command output:", result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e.stderr.decode())
if __name__ == "__main__":
    executeCommand("python3 ./engine.py softIoc:heartbeat 1")
