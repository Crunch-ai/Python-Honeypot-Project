#  Simple Python Honeypot

A basic TCP honeypot written in Python to simulate a listening service, detect unauthorized connection attempts, and log received data for analysis.

##  Overview

This honeypot is designed to act as a dummy server that listens on a specified port (default: `9999`). It accepts incoming connections, logs any data received, and then closes the connection. This can be useful for detecting scanning behavior, logging unauthorized access attempts, or conducting security research in a controlled environment.

 **Warning:** This honeypot is not a production-level security solution. It should be run in isolated environments or for educational purposes only.

---

##  Features

- Listens for incoming TCP connections
- Logs data received from clients
- Records logs to a file (`honeypot_log.txt`)
- Handles keyboard interruption (Ctrl+C) gracefully
- Includes basic error handling
- Lightweight and easy to deploy

---

##  Requirements

- Python 3.6 or higher
- No external libraries required

---

## Getting Started

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/python-honeypot.git
   cd python-honeypot
3. Run the script:
   python honeypot.py
You should see:
   Honeypot listening on port 9999....

##  Example Output 

    Honeypot listening on port 9999...
    Connection from ('192.168.1.100', 54321) has been established.
    Received data: GET /index.html HTTP/1.1

And in honeypot_log.txt : 

    INFO:root:data received: GET /index.html HTTP/1.1

## File Structure: 

    .
    ├── honeypot.py         # Main honeypot script
    ├── honeypot_log.txt    # Log file generated during runtime
    └── README.md           # Project documentation

# How It Works

The script creates a TCP socket and binds it to all available interfaces on port 9999.

It waits for incoming connections using listen().

Once a client connects, it accepts the connection and receives up to 1024 bytes of data.

The data is decoded (ignoring errors) and logged using Python’s logging module.

After handling each client, the connection is closed.

# Configuration
To change the listening port, edit the line:

    honeypot_socket.bind(('0.0.0.0', 9999)) # Change 9999 to your desired port number.
