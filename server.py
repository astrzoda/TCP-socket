from socket import socket, AF_INET, SOCK_STREAM

HOST = "localhost"
PORT = 10000

# comments from Andrew S. Tanenbaum book


def main():
    with socket(AF_INET, SOCK_STREAM) as server_socket: # create a socket (returned server_socket is a handle of
        # the created socket)
        server_socket.bind((HOST, PORT)) # bind is making an assignment of local IP address to the created socket
        server_socket.listen() # listen provides the memory allocation for queuing the connection requests.
        # The maximum number of connection requests is determined by the queue's size.
        connection, address = server_socket.accept() # accept makes the server enters standby mode for the
        # connection request. When it comes the new socket is created. This socket has the same properties as
        # the original previous socket. accept() returns a handle to the created new socket.
        print("Address", address)
        print(f"Accepted connection from {address}.")
        with connection:
            data: bytes = connection.recv(2048)
            length_of_file_name = data[0]
            file_name: bytes = data[1:length_of_file_name+1]
            content = data[length_of_file_name+1:]
            with open(file_name, 'wb') as f:
                f.write(content)
            # print(f"Received: {data}.")
            # connection.sendall(data)


if __name__ == '__main__':
    main()