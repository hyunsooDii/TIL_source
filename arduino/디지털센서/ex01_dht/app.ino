#include <DHT.h> // DHT.h 라이브러리를 포함한다
#include "MiniCom.h"
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE); // DHT설정 - dht (디지털3, dht11)

MiniCom com;

void checkHumiTemp(){
    // lcd에서는 float출력이 안됨, 문자열로 변환하여 출력해야 함
    float h = dht.readHumidity(); // 변수 h에 습도 값을 저장
    float t = dht.readTemperature(); // 변수 t에 온도 값을 저장

    com.print(0, "Humi", h);
    com.print(1, "Temp", t);
}

void setup() {
    com.init();
    com.setInterval(2000, checkHumiTemp);
    com.print(0, "MiniCom start...");
    com.print(1, "Humi/Temp Ex");
    dht.begin();
}

void loop() {
    com.run();
}
