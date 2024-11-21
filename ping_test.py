import subprocess

def ping_test():
    ip = "8.8.8.8"
    try:
        response = subprocess.run(["ping", "-c", "1", ip] if not subprocess.os.name == "nt" else ["ping", "-n", "1", ip],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        if response.returncode == 0:
            print("The program is working online!")
        else:
            print("The program is offline!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ping_test()
