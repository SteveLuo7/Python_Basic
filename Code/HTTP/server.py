import socket

port = int(input('请输入端口号：'))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.2.238', port))
server_socket.listen(128)
print('server is running at 192.168.2.238:{}'.format(port))

while True:
    client_socket, client_addr = server_socket.accept()

    data = client_socket.recv(1024).decode('utf8')

    print('接收到{}的数据{}'.format(client_addr[0], data))
    response_header = 'HTTP/1.1 OK\n' + 'content-type:text/html\n'
    response_header += '\n'
    client_socket.send(response_header.encode('utf8'))


    # client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    # client_socket.send('\n'.encode('utf8'))

    client_socket.send(client_addr[0].encode('utf8 '))
    client_socket.send('<h1 style="color:red">Hello WORLD LUOSHIBIN</h1>'.encode('utf8 '))








