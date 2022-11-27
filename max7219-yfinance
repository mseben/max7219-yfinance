#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>

#define USE_USE_PAROLA_HW 1
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 16

#define CLK_PIN   13
#define DATA_PIN  11
#define CS_PIN    10

MD_Parola P = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);

void setup(void)
{
  P.begin();
  P.setTextAlignment(PA_CENTER);
  P.print("(-.-) ..zzZZ");
  Serial.begin(9600);
}

void loop(void)
{
  while(Serial.available() > 0 ){
    String str = Serial.readString();
    str.trim();
    P.print(str);
  }
}
