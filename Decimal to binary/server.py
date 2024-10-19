from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

def calculate(expression):
    try:
        result ="{0:b}".format(int(expression))
    except:
        result = "Error in calculation"
    return result

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    expression = message.decode()
    
    # Perform calculation
    result = calculate(expression)
    
    # Send the result back to the client
    serverSocket.sendto(result.encode(), clientAddress)