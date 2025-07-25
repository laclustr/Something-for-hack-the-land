import serial
import pygame
import json
import time
from .parseData import parseKeyData

try:
    ser = serial.Serial('/dev/tty.usbserial-0001', 115200, timeout=0.01)
except Exception as e:
    print(f"Could not connect to Arduino: {e}")
    ser = None

def getKeysDown():
    keysdown = set()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return pygame.QUIT
        if event.type == pygame.KEYDOWN:
            keysdown.add(event.key)

    if ser and ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            data = json.loads(line)
            print(data)
            keysdown.update(parseKeyData(data))
        except Exception as e:
            print(f"[Serial Read Error] {e}")

    return keysdown