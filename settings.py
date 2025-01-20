# Pyino Tool 2025, webbrowser11
# Run Python Code From Your Arduino.

import serial # IGNORE
import time # IGNORE

arduino = serial.Serial(port='', baudrate=9600, timeout=1) # In the port section enter your arduino's port.

time.sleep(3) # IGNORE

def run_python_code(): # IGNORE
    # YOUR PYTHON CODE GOES HERE!
    return "Executed." # IGNORE

command = arduino.readline().decode("utf-8").strip() # IGNORE
if command == "run_python_code": # IGNORE
    print("Looks like the arduino is to run your code!") # IGNORE
    result = run_python_code() # IGNORE
    arduino.write((result + '\n').encode('utf-8')) # IGNORE

arduino.close() # IGNORE
