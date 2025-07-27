Welcome to Slappy-Bird, a cool twist on one of your favorite games. Rather than control the bird using a standard keyboard, the bird jumps by slapping an accelerometer back and forth. The game also features a two player mode and persistent high scores.

Configure the following ports on your arduino:
```
    D2 - Ultrasonic Range Detector
    D6 - Button

    A0 - Rotary Potentiometer
    A2 - Sound Sensor
    A6 - Light Sensor

    I2C. - 3-Axis Accelerometer
    I2C.. - BMP Air Pressure Sensor
```

Run this command `platformio run --target upload --upload-port /dev/cu.usbserial-0001` (change `/dev/cu.usbserial-0001` to the correct port).

Adjust the SERIAL_PATH variable in `Game/utils/config.py`.

Run the main.py file while the Arduino is connected.

Additional config options in `Game/utils/config.py`.

### Demos
[![Watch the Demo Video](https://img.youtube.com/vi/BHG4vx1beZA/hqdefault.jpg)](https://www.youtube.com/watch?v=BHG4vx1beZA)

