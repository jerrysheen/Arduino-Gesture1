#include <Wire.h>
#include "paj7620.h"
  // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
 

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  paj7620Init();
  Serial.begin(9600);
}

void loop()  {
    uint8_t data = 0;  // Read Bank_0_Reg_0x43/0x44 for gesture result.

    paj7620ReadReg(0x43, 1, &data);  // When different gestures be detected, the variable 'data' will be set to different values by paj7620ReadReg(0x43, 1, &data).

    if (data == GES_UP_FLAG) {                           // When up gesture be detected,the variable 'data' will be set to GES_UP_FLAG.
        Serial.println("UP");
    }// turn the LED on (HIGH is the voltage level)
   
    if (data == GES_DOWN_FLAG)  {                    // When down gesture be detected,the variable 'data' will be set to GES_DOWN_FLAG.
        Serial.println("DOWN");  
    }// turn the LED off by making the voltage LOW
 }
