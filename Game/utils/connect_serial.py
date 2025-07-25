import serial

def connect_serial(device, baud, timeout, state_machine):
    try:
        state_machine.ser = serial.Serial(device, baud, timeout=timeout)
        print(f"Connected to Arduino on {device} at {baud} baud.")
    except Exception as e:
        print(f"Could not connect to Arduino: {e}")
        ser = None