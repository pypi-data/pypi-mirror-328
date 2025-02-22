import socket
import struct
import time

# Define Bosch panel's IP and port
HOST = '10.0.0.84'  # IP address of your Bosch intrusion panel
PORT = 7702  # Port number for Mode 2 API (this might vary based on your setup)

# Bosch Mode 2 Protocol Request Template
def build_request(command, data=b''):
    """ Build the request packet for the Bosch Mode 2 Protocol """
    packet = bytearray()
    # Header: protocol ID (2 bytes), command ID (2 bytes)
    packet.extend(struct.pack('>H', 0x0101))  # Protocol ID for Mode 2
    packet.extend(struct.pack('>H', command))  # Command ID (e.g., 0x1001 for date/time)
    packet.extend(struct.pack('>H', len(data)))  # Length of data
    packet.extend(data)  # Actual data (if any)
    
    # Calculate and append checksum (simple checksum sum of all bytes)
    checksum = sum(packet) % 256
    packet.append(checksum)
    
    return bytes(packet)

# Function to send and receive data from the Bosch panel
def send_request(command, data=b''):
    """ Send request to Bosch intrusion panel and receive response """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request_packet = build_request(command, data)
        s.sendall(request_packet)
        
        # Receive the response from the panel
        response = s.recv(1024)
        return response

# Command IDs (example: 0x1001 is used to request date/time)
DATE_TIME_COMMAND = 0x1001  # Command to get the date/time from the panel
ARM_DISARM_COMMAND = 0x1002  # Command to arm/disarm the panel
STATUS_COMMAND = 0x1003  # Command to get the status of the panel

# Function to get date and time from the panel
def get_date_time():
    return send_request(DATE_TIME_COMMAND)

# Function to arm the panel
def arm_panel():
    return send_request(ARM_DISARM_COMMAND, b'\x01')  # Assuming 0x01 is the data to arm

# Function to disarm the panel
def disarm_panel():
    return send_request(ARM_DISARM_COMMAND, b'\x00')  # Assuming 0x00 is the data to disarm

# Function to get the status of the panel
def get_status():
    return send_request(STATUS_COMMAND)

# Example usage
if __name__ == "__main__":
    print("Connecting to Bosch panel...")

    # Request date/time from the panel
    print("Requesting date and time from the Bosch panel...")
    response = get_date_time()
    print(f"Date and Time Response: {response}")

    # Arm the panel
    print("Arming the panel...")
    response = arm_panel()
    print(f"Arm Response: {response}")

    # Disarm the panel
    print("Disarming the panel...")
    response = disarm_panel()
    print(f"Disarm Response: {response}")

    # Get the status of the panel
    print("Getting the status of the panel...")
    response = get_status()
    print(f"Status Response: {response}")