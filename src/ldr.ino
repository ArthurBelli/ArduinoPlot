short ldr = 0; //analog 0
short ldr_value;
short brightness;
unsigned long time_measure = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  //analog value varies from 0 to 1024
  ldr_value = analogRead(ldr);
  time_measure = millis();
  //lower the reading -> higher the instensity
  brightness = map(ldr_value, 0, 1024, 100, 0); //Converts the value from 0-1024 to 0-100 switching the bounds so it becomes intuitive
  Serial.print(time_measure);
  Serial.print(",");
  Serial.println(brightness);
  delay(300);
}
