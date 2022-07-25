import socket

HOST = "localhost"
PORT = 8003

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((HOST, PORT))

    sock.sendall(b"1,2,3")

    buf = sock.recv(2000)

    print(buf)


if __name__ == '__main__':
    main()
