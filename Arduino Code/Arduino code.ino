int IRSensor = 7; // connect ir sensor to arduino pin 2
int LED = 13; // conect Led to arduino pin 13
#include <Servo.h>
Servo myservo;
int pos = 0;
#include <Wire.h>
#include <Adafruit_MLX90614.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() 
{
  myservo.attach(9);
  pinMode (IRSensor, INPUT); // sensor pin INPUT
  pinMode (LED, OUTPUT); // Led pin OUTPUT
  Serial.begin(9600);
  Serial.println("Adafruit MLX90614 test");  
  mlx.begin();
}

void loop()
{
  int statusSensor = digitalRead (IRSensor);
  while(1){
    statusSensor = digitalRead (IRSensor);
    if(statusSensor == 0){
      digitalWrite(LED, HIGH); // LED High
      Serial.println("1");
      delay(100);
      break;
    }
    else{
      digitalWrite(LED, LOW);
      Serial.println("0");
      delay(100);
    }
  }
  char a = Serial.read(); 
  int temp = int(mlx.readObjectTempF());
  Serial.println("a = ");
  Serial.print(a);
  if(a == 'm' && temp<115){
    Serial.write("Servo on\n");
    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  }
  else{
    Serial.write("Servo OFF\n");
    delay(5000);
  }
  Serial.println();
  //delay(10000);
}

/*
int IRSensor = 2; // connect ir sensor to arduino pin 2
int LED = 13; // conect Led to arduino pin 13

void setup() 
{
  pinMode (IRSensor, INPUT); // sensor pin INPUT
  pinMode (LED, OUTPUT); // Led pin OUTPUT
}

void loop()
{
  int statusSensor = digitalRead (IRSensor);
  
  if (statusSensor == 1){
    digitalWrite(LED, LOW); // LED LOW
  }
  
  else
  {
    digitalWrite(LED, HIGH); // LED High
  }
  
}*/
