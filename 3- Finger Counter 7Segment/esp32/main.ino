const int a = 13;
const int b = 14;
const int c = 16;
const int d = 17;
const int e = 18;
const int f = 19;
const int g = 21;

const int D2 = 27;
const int D3 = 26;

const int segments[] = {a, b, c, d, e, f, g};

// Common Cathode
const byte numbers[10][7] = {
  {1,1,1,1,1,1,0}, // 0
  {0,1,1,0,0,0,0}, // 1
  {1,1,0,1,1,0,1}, // 2
  {1,1,1,1,0,0,1}, // 3
  {0,1,1,0,0,1,1}, // 4
  {1,0,1,1,0,1,1}, // 5
  {1,0,1,1,1,1,1}, // 6
  {1,1,1,0,0,0,0}, // 7
  {1,1,1,1,1,1,1}, // 8
  {1,1,1,1,0,1,1}  // 9
};

int number = 0;

unsigned long previousMillis = 0;
const unsigned long refreshInterval = 3;

bool activeDigit = false;


void setup() {

  Serial.begin(9600);

  for (int i = 0; i < 7; i++) {pinMode(segments[i], OUTPUT);}

  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);

  digitalWrite(D2, LOW);
  digitalWrite(D3, LOW);
}


void showDigit(int digit) {
  for (int i = 0; i < 7; i++) {digitalWrite(segments[i], numbers[digit][i]);}
}


void clearSegments() {
  for (int i = 0; i < 7; i++) {digitalWrite(segments[i], LOW);}
}

void loop() {

  if (Serial.available()) {

    number = Serial.read();
    if (number > 10) {number = 10;}
  }

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= refreshInterval) {

    previousMillis = currentMillis;

    digitalWrite(D2, LOW);
    digitalWrite(D3, LOW);

    if (number < 10) {

      showDigit(number);
      digitalWrite(D3, HIGH);
    }
    else {

      if (activeDigit == false) {

        showDigit(1);
        digitalWrite(D2, HIGH);
        activeDigit = true;
      }

      else {

        showDigit(0);
        digitalWrite(D3, HIGH);
        activeDigit = false;
      }
    }
  }
}
