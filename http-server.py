import socket

host = 'localhost'
port = 8080
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
my_socket.bind((host, port))
my_socket.listen(2)

print ("Serving HTTP on port " + str(port) + " ...")

while True:
	client_connection, client_address = my_socket.accept()
	request = client_connection.recv(1024)
	print(request.decode('utf-8'))
	http_response = """
HTTP/1.1 200 OK

							Response Message
"""
	client_connection.sendall(http_response)
	client_connection.close()

