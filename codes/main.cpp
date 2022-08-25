#include <Arduino.h>
int  ledPin=13;

//Code released under GNU GPL.  Free to use for anything.
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(13,OUTPUT);
    
}

// the loop function runs over and over again forever
void loop(){
digitalWrite(ledPin,HIGH);
delay(1000);
digitalWrite(ledPin,LOW);
delay(1000);
}
