import socket
import logging

# Configure logging
logging.basicConfig(filename='honeypot_log.txt', level=logging.INFO)

def start_honeypot():
    """Starts a honeypot server that listens for incoming connections."""
    try:
        # Create a socket object
        honeypot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to a public host and port
        honeypot_socket.bind(('0.0.0.0', 9999))

        # Become a server socket
        honeypot_socket.listen(5)
        print("Honeypot listening on port 9999...")

        while True:
            # Accept connections from outside
            client_socket, address = honeypot_socket.accept()
            print(f"Connection from {address} has been established.")

            # Receive data from the client
            data = client_socket.recv(1024)
            data_decoded = data.decode('utf-8', errors='ignore')  # Decode data
            print(f"Received data: {data_decoded}")

            # Log the data
            logging.info(f"data received: {data_decoded}")

            # Close the client socket
            client_socket.close()

    except socket.error as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Shutting down honeypot...")
    finally:
        honeypot_socket.close()

if __name__ == "__main__":
    start_honeypot()
