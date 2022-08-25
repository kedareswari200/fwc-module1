#include<Arduino.h>
int A=1, B=0;    // Input Variables
int x0,x1,x2,x3; //Intermediate Variables
void setup() 
{
  pinMode(5,OUTPUT);

}

void loop() {
  digitalRead(A); 
  digitalRead(B);
  x0=!(A || B);   // Boolean Logic Expressions
  x1=!(A||(!A && !B));
  x2=!(B||(!A && !B));
  x3=(A&&B) || (!A && !B);
  digitalWrite(5,x3);
  delay(1000);

}
