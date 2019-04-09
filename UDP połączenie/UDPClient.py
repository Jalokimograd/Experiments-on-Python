from socket import *
serverName = '192.168.0.17'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Podaj napis małymi literami aby serwer zamienił je na wielkie:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
