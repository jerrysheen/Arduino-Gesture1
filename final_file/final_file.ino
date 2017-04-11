#include <Wire.h>
#include "paj7620.h"
int value = 0; 
int x_ray=3;
int y_ray=2;
int press_ray=1;

void setup() {
   // put your setup code here, to run once:
    paj7620Init();
    Serial.begin(9600);
}

void loop() {
    uint8_t data = 0;
    paj7620ReadReg(0x43, 1, &data);
    if (data == GES_UP_FLAG) {                           // When up gesture be detected,the variable 'data' will be set to GES_UP_FLAG.
        Serial.println("UP");
    }// turn the LED on (HIGH is the voltage level)
   
    else if (data == GES_DOWN_FLAG)  {                    // When down gesture be detected,the variable 'data' will be set to GES_DOWN_FLAG.
        Serial.println("DOWN");  
    }
    else if (data == GES_FORWARD_FLAG){
        Serial.println("CLICK");
    }
    else {
        Serial.print('(');
        Serial.print(analogRead(x_ray)); 
        Serial.print(",");
        Serial.print(analogRead(y_ray));
        Serial.print(")\n");
        delay(50);
    }
  // put your main code here, to run repeatedly:

}
