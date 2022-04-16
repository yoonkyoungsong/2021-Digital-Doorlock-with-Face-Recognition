int in_port=12;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(in_port, OUTPUT);

}

int receivedData = 0;

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    receivedData = Serial.read();
  }
  Serial.println(receivedData);

  if(receivedData == 49){
      digitalWrite(in_port, LOW);
      delay(1000);
      digitalWrite(in_port,HIGH);
      Serial.println("open");
      delay(10000);
      digitalWrite(in_port,LOW);
      delay(1000);
      digitalWrite(in_port,HIGH);
      Serial.println("close");
  }
  receivedData=0;
  digitalWrite(in_port,HIGH);
  delay(1000);
}
