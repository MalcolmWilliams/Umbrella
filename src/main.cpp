/*
 * Only ESP plus small LED:
 * Average power consumption: 32.5mW
 * Max: 240mW
 */

#include "ESP8266WiFi.h"
#include "BrightnessMap.h"

unsigned long start_time; // = micros();
unsigned long end_time; // = micros();
int nets;
int LEDpin = 0;


void setBrightness(int val);
void printScanResult(int networksFound);


void printScanResult(int networksFound)
{
  int val = 0;
  //Serial.println();
  Serial.printf("%d network(s) found\n", networksFound);
  for (int i = 0; i < networksFound; i++)
  {
    //Serial.printf("%d: %s, Ch:%d (%ddBm) %s\n", i + 1, WiFi.SSID(i).c_str(), WiFi.channel(i), WiFi.RSSI(i), WiFi.encryptionType(i) == ENC_TYPE_NONE ? "open" : "");
    Serial.printf("%s, (%ddBm)\n", WiFi.SSID(i).c_str(), WiFi.RSSI(i));
  
  /*  
   *  -20 is the closest 
   *  -80 is the farthest 
   *  
   *  Need to come up with an algorythm that has the desired effect
   */
    //if(WiFi.SSID(i).c_str() == "ESP-AP") val += 100 - WiFi.RSSI(i);
    //if(WiFi.SSID(i).c_str() == "ESP-AP\n") val += 100 - WiFi.RSSI(i);
    if(WiFi.SSID(i) == "ESP-AP") val += 100 + WiFi.RSSI(i);
    //if(WiFi.SSID(i) == "ESP-AP\n") val += 100 - WiFi.RSSI(i);
  }

  setBrightness(val);
}

void setBrightness(int val)
{
  if (val > 100) val = 100;
  Serial.println(val);

  val = BrightnessMap[val]; //map the brightness to make the led brightness change appear linear (normally it will look logarithmic)
  analogWrite(LEDpin, (100-val)*PWMRANGE/100);
}



void setup()
{
  Serial.begin(115200);
  Serial.println();

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  pinMode(LEDpin, OUTPUT);
  analogWrite(LEDpin, 0);
}


void loop() {
  start_time = micros();
  int nets = WiFi.scanNetworks();
  printScanResult(nets);
  end_time = micros();
  Serial.print("Run Time: ");
  Serial.println((end_time - start_time)/1000000.0);
  
  }

