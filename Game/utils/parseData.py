import pygame
from .config import *

def parseKeyData(data):
    pressed_keys = set()
    if data["Button"]:
        pressed_keys.add(BUTTON_BUTTON)
    if data["LIS"]["x"] > LIS_X_SENSITIVITY or data["LIS"]["x"] < -LIS_X_SENSITIVITY:
        pressed_keys.add(SHAKE_BUTTON)
    if data["LIS"]["y"] > LIS_Y_SENSITIVITY or data["LIS"]["y"] < -LIS_Y_SENSITIVITY:
        pressed_keys.add(SHAKE_BUTTON)
    if data["LIS"]["z"] > LIS_Z_SENSITIVITY or data["LIS"]["z"] < -LIS_Z_SENSITIVITY:
        pressed_keys.add(SHAKE_BUTTON)
    if data["Sound"] > SOUND_SENSITIVITY:
        pressed_keys.add(CLAP_BUTTON)
    return pressed_keys
