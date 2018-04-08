#include <Adafruit_BMP085.h>
#include "DHT.h"
#include <Wire.h>

#define DHTPIN 2
#define DHTTYPE DHT22
Adafruit_BMP085 bmp;
DHT dht(DHTPIN, DHTTYPE);

int ledPin = 11;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  bmp.begin();
  dht.begin();
}

void loop() {
  if(Serial.available()) {
    char serialListener = Serial.read();
    if(serialListener == 'D') {
        getDHT22();
    }
  }
}

void getDHT22() {
  delay(2000);
  digitalWrite(ledPin, HIGH);
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  Serial.println(temp);
  Serial.println(humi);
  digitalWrite(ledPin, LOW);
  getBMP180();
}

void getBMP180() {
  delay(1000);
  float pres = bmp.readPressure();
  Serial.println(pres);
}

void blink() {
  for(int i=0; i<1; i++) {
    for (int i=0; i<1; i++) {
      digitalWrite(ledPin, HIGH);
      delay(50);
      digitalWrite(ledPin, LOW);
      delay(50);
    }
    delay(500);
  }
}