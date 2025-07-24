import serial
import pygame

try:
    ser = serial.Serial('/dev/tty.usbserial-0001', 9600)
except Exception as e:
    print(f"Could not connect to Arduino: {e}")
    ser = None

def getKeysDown():
    keysdown = set()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keysdown.add(event.key)

    if ser and ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line == "SPACE":
                keysdown.add(pygame.K_SPACE)
            if line == "UP":
                keysdown.add(pygame.K_UP)
        except Exception as e:
            print(f"[Serial Read Error] {e}")

    return keysdown