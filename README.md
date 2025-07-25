Welcome to Wacky-Bird, a cool twist on one of your favorite games. Adding a multitude of sensors, you can make it feel like you're playing the game in real life.

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

Compile the Controls folder and send to your Arduino using a tool such as PIO.

Adjust the SERIAL_PATH variable in `Game/utils/config.py`.

Run the main.py file while the Arduino is connected.

Additional config options in `Game/utils/config.py`.