int sensorPin = 5;
int value = 0; 
int x_ray=3;
int y_ray=2;
int press_ray=1;

void setup() {
Serial.begin(9600); 
}

void loop() {
 Serial.print('(');
 Serial.print(analogRead(x_ray)); 
 Serial.print(",");
 Serial.print(analogRead(y_ray));
 Serial.print(")\n");

delay(50);
}
