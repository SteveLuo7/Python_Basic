import socket

server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind('192.168.31.199', 9090)
server_socket.listen(128)

client_socket, client_addr = server_socket.accept()
data = client_socket.recv(1024).decode('utf8')


print('接受了来自{}地址，{}端口的数据，内容为{}'.format(client_addr[0], client_addr[1], data))