int LED = 10;

void setup() {
    pinMode(LED, OUTPUT);
}
void loop() {
    int readVal = analogRead(A0);
    int brightVal = readVal / 4;
    analogWrite(LED, brightVal);
    delay(10);
}