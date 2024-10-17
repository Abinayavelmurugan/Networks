import socket

def convert_number(number, conversion_type):
    if conversion_type == 'binary':
        return bin(int(number))
    elif conversion_type == 'octal':
        return oct(int(number))
    elif conversion_type == 'hexadecimal':
        return hex(int(number))
    else:
        return "Invalid conversion type!"

# Setting up the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Bind to a port
    server_socket.listen(1)  # Listen for incoming connections
    print("Server is listening on port 12345...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")

        # Receiving data from client
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received from client: {data}")

        # Split the received data
        number, conversion_type = data.split(',')

        # Perform the number conversion
        result = convert_number(number, conversion_type.strip())

        # Send result back to the client
        conn.send(result.encode('utf-8'))

        conn.close()

if __name__ == "__main__":
    start_server()
