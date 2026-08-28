import socket

HOST = "TARGET_HOST" #CHANGE THIS
PORT = 8000
WORDLIST = "WORDLSIT" #CHANGE THIS

with open(WORDLIST, "r", errors="ignore") as file:
    for line in file:
        word = line.strip()

        if not word:
            continue

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        try:
            sock.connect((HOST, PORT))

            sock.sendall((word + "\n").encode())

            response = sock.recv(1024).decode(errors="ignore")

            # Only display responses that don't look like normal failures
            if "is not defined" not in response:
                print(f"[+] {word:<20} -> {response.strip()}")

        except Exception:
            pass

        finally:
            sock.close()

print("---FUZZING COMPLETED---")
