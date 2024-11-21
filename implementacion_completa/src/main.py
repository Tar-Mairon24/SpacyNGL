import serial
import time

# Configure the serial connection
arduino_port = "/dev/cu.usbserial-130"  # Replace with your Arduino's port (e.g., COM3 on Windows or /dev/ttyUSB0 on Linux/Mac)
baud_rate = 9600       # Make sure this matches the baud rate in your Arduino sketch
# Open the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Wait for the connection to initialize
print(f"Connected to Arduino on {arduino_port}")

def send_message(message):
    try:
        # Send a string to the Arduino
        command = message # Command to send; include newline (\n) if Arduino expects it
        ser.write(command.encode())  # Send the command as bytes
        print(f"Sent: {command.strip()}")

    except serial.SerialException as e:
        print(f"Error: {e}")

def main():
    send_message("FARO0")

    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")

# Entry point
if __name__ == "__main__":
    main()
