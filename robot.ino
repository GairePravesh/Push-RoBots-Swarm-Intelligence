
int motor1h = 10, motor1l = 8, motor2h = 7, motor2l = 5;    // Motors direction controll pins
int irLL = A4, irL = A5, irR = A6, irRR = A7;   // IR input pins
int motor1sp = 6, motor2sp = 9; // Motors speed control pins
String command;
int threshold = 350;
unsigned int timer = 0;
int count = 0;

void calibrateSpeed(int m1, int m2){
  analogWrite(motor1sp, m1);
  analogWrite(motor2sp, m2);
}

void wait(){
  digitalWrite(motor1h, LOW);
  digitalWrite(motor1l, LOW);
  digitalWrite(motor2h, LOW);
  digitalWrite(motor2l, LOW);
}

void forward(){
  digitalWrite(motor1h, HIGH);
  digitalWrite(motor1l, LOW);
  digitalWrite(motor2h, HIGH);
  digitalWrite(motor2l, LOW);
}

void backward(){
  digitalWrite(motor1h, LOW);
  digitalWrite(motor1l, HIGH);
  digitalWrite(motor2h, LOW);
  digitalWrite(motor2l, HIGH);
}

void right(){
  digitalWrite(motor1h, LOW);
  digitalWrite(motor1l, HIGH);
  digitalWrite(motor2h, HIGH);
  digitalWrite(motor2l, LOW);
}

void left(){
  digitalWrite(motor1h, HIGH);
  digitalWrite(motor1l, LOW);
  digitalWrite(motor2h, LOW);
  digitalWrite(motor2l, HIGH);
}

bool IRLL(){
  return analogRead(irLL) < threshold ? 0 : 1;
}

bool IRL(){
  return analogRead(irL) < threshold ? 0 : 1;
}

bool IRRR(){
  return analogRead(irRR) < threshold ? 0 : 1;
}

bool IRR(){
  return analogRead(irR) < threshold ? 0 : 1;
}

bool nodeT(){
  if (IRR() && IRL() && IRLL() && IRRR())
  {
    return true;
  }
  else {
    return false;
  }
}

bool nodeL(){
  if(IRRR() && IRR()){
    if(IRL() == 0 && IRLL() == 0){
      return true;
    }
  }
  if(IRLL() && IRL()){
    if(IRR() == 0 && IRRR() == 0){
      return true;
    }
  }
  else{
    return false;
  }
}

void anticlockwise(){
  forward();
  delay(150);
  do{
    left();
  }while(IRL() == 0);
}

void clockwise(){
  forward();
  delay(150);
  do{
    right();
  }while(IRR() == 0);
}

void turn(){
  backward();
  delay(350);
  do{
    right();
  }while(IRR() == 0);
}

void choice(){
  switch (command.charAt(count)){
    case 97:
      anticlockwise();
      break;
    case 99:
      clockwise();
      break;
    case 116:
      turn();
      break;
    default:
      forward();
      delay(100);
  }
  count ++;
}

void setup(){
    pinMode(motor1h, OUTPUT);
    pinMode(motor1l, OUTPUT);
    pinMode(motor2h, OUTPUT);
    pinMode(motor2l, OUTPUT);
    
    pinMode(motor1sp, OUTPUT);
    pinMode(motor2sp, OUTPUT);

    calibrateSpeed(200,160);

    Serial.begin(9600);

    while(Serial.available() <= 0){
      Serial.write("I need direction");
      wait();
    }
    command = Serial.read();    
    choice();
}

void loop(){
  if (millis() - timer > 1000){
    if(nodeL() || nodeT()){
      timer = millis();
      choice();
    }
  }
  if(IRR()){
    right();
  }
  else if(IRL()){
    left();
  }    
  else{
    forward();
  }
}
