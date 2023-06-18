from socket import socket, AF_INET, SOCK_STREAM
import argparse
HOST = "localhost"
PORT = 10000


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    parser.add_argument("infile", type=str)
    parser.add_argument("outfile", type=str)
    args = parser.parse_args()
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect((args.host, args.port))
        with open(args.infile, 'rb') as f:
            payload = bytes([len(args.outfile)])+args.outfile.encode() + f.read()
            client_socket.sendall(payload)
        # data = client_socket.recv(2048)
        # print(f"Received: {data}")


if __name__ == '__main__':
    main()

