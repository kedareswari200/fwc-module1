#include <Arduino.h>
int A=1, B=1;    // Input Variables
int x0,x1,x2,x3; //Intermediate Variables
void setup()
{
  pinMode(13,OUTPUT);

}

void loop() {
  digitalRead(A);
  digitalRead(B);
  x0=!(A || B);   // Boolean Logic Expressions
  x1=!(A || x0);
  x2=!(B || x2);
  x3=!(x1 || x2);
  digitalWrite(13,x3);
  delay(1000);

}

