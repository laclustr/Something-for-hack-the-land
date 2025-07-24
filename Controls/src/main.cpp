#include <Arduino.h>
#include "LIS3DHTR.h"
#ifdef SOFTWAREWIRE
    #include <SoftwareWire.h>
    SoftwareWire myWire(3, 2);
    LIS3DHTR<SoftwareWire> LIS;
    #define WIRE myWire
#else
    #include <Wire.h>
    LIS3DHTR<TwoWire> LIS;
    #define WIRE Wire
#endif

const int sensitivity = 3;

const int buttonPin = 6;
const int ledPin = 4;
const int soundPin = A2;
int buttonState = 0;
int soundState = 0;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  pinMode(soundPin, INPUT);
  Serial.begin(9600);

  while (!Serial) {};
  LIS.begin(WIRE, 0x19);
  delay(100);
  LIS.setOutputDataRate(LIS3DHTR_DATARATE_50HZ);
}

void loop() {
  if (!LIS) {
    Serial.println("LIS3DHTR didn't connect.");
    while (1);
    return;
  }

  int x = LIS.getAccelerationX();
  int y = LIS.getAccelerationY();
  int z = LIS.getAccelerationZ();
  if (x >= 3 || y >= 3 || z >= 3) {
    Serial.println("x: " + String(x) + " y: " + String(y) + " z: " + String(z));
  }
  if (x >= 3 || y >= 3 || z >= 3 || x <= -3 || y <= -3 || z <= -3) {
    Serial.println("UP");
    delay(100);
  }

  buttonState = digitalRead(buttonPin);
  soundState = analogRead(soundPin);

  if (soundState > 600) {
    digitalWrite(ledPin, HIGH);
    Serial.println("SPACE");
    delay(100);
  }
  if (buttonState == HIGH) {
    Serial.println("UP");
    delay(100);
  }
  if (soundState < 600 && buttonState == LOW) {
    digitalWrite(ledPin, LOW);

  }
}