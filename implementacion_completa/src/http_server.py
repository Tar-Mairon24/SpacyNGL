from sys import exception
from flask import Flask, request, jsonify
from use_model import predict_intent
import serial
import time

app = Flask(__name__)
# Configure the serial connection
arduino_port = "/dev/cu.usbserial-130"  # Replace with your Arduino's port (e.g., COM3 on Windows or /dev/ttyUSB0 on Linux/Mac)
baud_rate = 9600       # Make sure this matches the baud rate in your Arduino sketch
# Open the serial port
ser = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

def send_message(message):
    try:
        # Send a string to the Arduino
        command = message # Command to send; include newline (\n) if Arduino expects it
        ser.write(command.encode())  # Send the command as bytes
        print(f"Sent: {command.strip()}")

    except serial.SerialException as e:
        print(f"Error: {e}")

@app.route('/raw', methods=['POST'])
def raw_text():
    raw_data = request.data  # This retrieves the raw body of the request
    response = ""
    code = 200

    try:
        state = False
        type = ""
        message = ""
        query = raw_data.decode('utf-8')
        result = predict_intent(query)

        if result == "FARO0": 
            state = False
            type = "Faros"
            message = "Faros apagados"
        elif result == "FARO1":
            state = False
            type = "Faros"
            message = "Faros encendidos en luz baja"
        elif result == "FARO2":
            state = True
            type = "Faros"
            message = "Faros encendidos en luz alta"

        try: 
            send_message(result)
        except:
            state = False
            type = "Error"
            message = "Hubo un error al conectarse con el arduino"
            code = 500

        # Succesful prediction
        response = {
            "state": state,  # Set state to True for a successful prediction
            "type": type,
            "message": message
        }
    except:
        # to -do
        response = {
            "state": False,  # Set state to False for errors
            "type": "Error",
            "message": "Lo siento no entendí lo que quieres decir"
        }
        code = 400
    
    return jsonify(response), code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
