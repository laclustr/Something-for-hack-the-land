#include <Arduino.h>
#include <ArduinoJson.h>
#include <Wire.h>

#include "LIS3DHTR.h"
#include "Seeed_BMP280.h"
#include "Ultrasonic.h"

#define WIRE Wire

// Pins
const int buttonPin = 6;
const int ledPin = 4;
const int soundPin = A2;
const int sensorPin = A6;
const int rotaryPin = A0; 
const int ultrasonicPin = 2;

// Object Instantiation
LIS3DHTR<TwoWire> LIS;
BMP280 bmp280;
Ultrasonic ultrasonic(ultrasonicPin);

// Sensitivity
const int sensitivity = 3;

// Sensor Values
int sensorValue = 0;
int buttonState = 0;
int soundState = 0;
int rotaryValue = 0;

// Functions
void initPins();
void initLIS();
void readAndSendJSON();

void setup() {
  Serial.begin(115200);
  
  initPins();
  initLIS();

  if (!bmp280.init()) {
    Serial.println("Device not connected or broken!");
  }
}

void loop() {
  readAndSendJSON();
  delay(10);
}

void initPins() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  pinMode(soundPin, INPUT);
  pinMode(sensorPin, INPUT);
  pinMode(rotaryPin, INPUT);
}

void initLIS() {
  while (!Serial) {};
  LIS.begin(WIRE, 0x19);
  delay(100);
  LIS.setOutputDataRate(LIS3DHTR_DATARATE_50HZ);
}

void readAndSendJSON() {
  StaticJsonDocument<256> doc;
  float pressure;

  doc["LIS"]["x"] = LIS.getAccelerationX();
  doc["LIS"]["y"] = LIS.getAccelerationY();
  doc["LIS"]["z"] = LIS.getAccelerationZ();

  doc["Light"] = analogRead(sensorPin);

  doc["Button"] = digitalRead(buttonPin) == HIGH ? true : false;

  doc["Sound"] = analogRead(soundPin);

  doc["Rotary"] = analogRead(rotaryPin);

  doc["Temp"] = bmp280.getTemperature();
  
  doc["Pressure"] = pressure = bmp280.getPressure();

  doc["Altitude"] = bmp280.calcAltitude(pressure);

  doc["Distance"] = ultrasonic.MeasureInCentimeters();

  serializeJson(doc, Serial);
  Serial.println();
}