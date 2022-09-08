#include <avr/io.h>
#include<stdbool.h>
#include <util/delay.h>
void sevenseg(int);
int main (void)
{
  bool x=1,y=1;
  bool p,q,r,s;
  while(1)
  {
     DDRB =0b00100000;
     p=!(x|y);
     q=!(x|p);
     r=!(y|p);
     s=!(q|r);
     PORTD|=(s<<4);
  }
  return 0;
}
