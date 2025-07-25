import pygame
import json
from .config import *
from .parseData import parseKeyData
from .connect_serial import connect_serial

def getKeysDown(state_machine):
    keysdown = set()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return pygame.QUIT
        if event.type == pygame.KEYDOWN:
            keysdown.add(event.key)

    ser = state_machine.ser
    try:
        if not ser:
            raise OSError("Serial connection not established.")
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').strip()
                data = json.loads(line)
                print(data)
                keysdown.update(parseKeyData(data, state_machine))
            except Exception as e:
                print(f"[Serial Read Error] {e}")
    except OSError as e:
        print(f"[Serial Connection Error] {e}\nRetrying...")
        connect_serial(SERIAL_PORT, SERIAL_BAUD, SERIAL_TIMEOUT, state_machine)

    return keysdown