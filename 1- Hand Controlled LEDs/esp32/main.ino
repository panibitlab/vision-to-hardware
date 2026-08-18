int leds[] = {13, 14, 25, 26, 27};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {pinMode(leds[i], OUTPUT);}
}

void loop() {
  if (Serial.available() >= 5) {
    for (int i = 0; i < 5; i++) {
      int fingerState = Serial.read();
      digitalWrite(leds[i], fingerState == 1 ? HIGH : LOW);
    }
  }
}
