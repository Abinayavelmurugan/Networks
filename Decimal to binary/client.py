from socket import *
serverName = '192.168.154.83'  # Use the actual server IP
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Take the arithmetic expression as input
expression = input('Give the number: ')

# Send the expression to the server
clientSocket.sendto(expression.encode(), (serverName, serverPort))

# Receive the result from the server
result, serverAddress = clientSocket.recvfrom(2048)

# Print the result
print('Result:', result.decode())

clientSocket.close()