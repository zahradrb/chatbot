import socket
import selectors

HOST = "localhost"
PORT = 8003

def main():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)
        except KeyboardInterrupt:
            print("Bye")
            break

if __name__ == '__main__':
    main()