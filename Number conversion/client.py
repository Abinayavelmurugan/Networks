import socket

def send_request(number, conversion_type):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connect to server

    # Send number and conversion type as comma-separated values
    message = f"{number},{conversion_type}"
    client_socket.send(message.encode('utf-8'))

    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Converted result from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    number = input("Enter a number: ")
    conversion_type = input("Enter conversion type (binary/octal/hexadecimal): ")

    send_request(number, conversion_type)
