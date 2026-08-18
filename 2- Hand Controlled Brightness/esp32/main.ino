const int LED_PIN = 13;

void setup() {
  Serial.begin(9600);

  pinMode(LED_PIN, OUTPUT);
}

void loop() {

  if (Serial.available()) {

    int brightness = Serial.read();

    analogWrite(LED_PIN, brightness);
  }
}
