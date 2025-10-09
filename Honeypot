import socket
import datetime
import logging

# Set up logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO,
    format='%(asctime)s - %(message)s')

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0' # Listen on all interfaces
port = 9999      # Choose a port (ensure it's not in use)

# Bind the socket
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Honeypot running on {host}:{port}")

while True:
        # Accept incoming connections
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        # Log the connection
        log_message = f"New connection from {addr}"
        logging.info(log_message)
        
        # Send a dummy response
        client_socket.send(b"Connected to honeypot. This is a trap!\n")
        client_socket.close()
