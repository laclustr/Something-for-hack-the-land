from .config import *

def parseKeyData(data, state_machine):
    
    facets = state_machine.facets

    pressed_keys = set()

    if SHAKE_ENABLED:
        is_shaking = (
            abs(data["LIS"]["x"]) >= LIS_X_SENSITIVITY or
            abs(data["LIS"]["y"]) >= LIS_Y_SENSITIVITY or
            abs(data["LIS"]["z"]) >= LIS_Z_SENSITIVITY
        )

        if is_shaking and not facets["shake"]:
            facets["shake"] = True
            pressed_keys.add(SHAKE_BUTTON)
        elif not is_shaking:
            facets["shake"] = False

    if BUTTON_ENABLED:
        if data["Button"] and not facets["button"]:
            facets["button"] = True
            pressed_keys.add(BUTTON_BUTTON)
        elif facets["button"] and not data["Button"]:
            facets["button"] = False
    
    if CLAP_ENABLED:
        if data["Sound"] > SOUND_SENSITIVITY and not facets["clap"]:
            facets["clap"] = True
            pressed_keys.add(CLAP_BUTTON)
        elif facets["clap"] and data["Sound"] <= SOUND_SENSITIVITY:
            facets["clap"] = False

    
    _adjust_game_vars(data, state_machine)

    return pressed_keys

def _adjust_game_vars(data, state_machine):
    if DIAL_ENABLED:
        state_machine.speed = SCROLL_SPEED * (data["Rotary"] / ROTARY_SCALE)

    if TEMPERATURE_ENABLED:
        state_machine.gravity = BIRD_GRAVITY * (data["Temp"] / BASE_TEMP)

    if USE_DISTANCE and DISTANCE_ENABLED:
        state_machine.opacity = max(0, min(255, int(MAX_OPACITY * (data["Distance"] / BASE_DISTANCE))))
    elif LIGHT_ENABLED:
        state_machine.opacity = max(0, min(255, 255 - int(MAX_OPACITY * (data["Light"] / BASE_LIGHT))))
    
    if PRESSURE_ENABLED:
        state_machine.vignette_strength = min(255, int(VIGNETTE_STRENGTH * (data["Pressure"] / BASE_PRESSURE) * 3))

