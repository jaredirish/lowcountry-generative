/* 
  LCG: Hive Node - ESP32-S3 Firmware (Draft v0.1)
  Handles: HX711 Load Cell + Stepper Motor Pulse
*/

#include <Arduino.h>
#include <ArduinoJson.h>

// PIN DEFINITIONS (Adjust these for your custom PCB/Breakout)
const int HX711_DOUT = 4;
const int HX711_SCK = 5;
const int MOTOR_STEP_PIN = 12;
const int MOTOR_DIR_PIN = 13;

void setup() {
  Serial.begin(115200);
  pinMode(MOTOR_STEP_PIN, OUTPUT);
  pinMode(MOTOR_DIR_PIN, OUTPUT);
  
  Serial.println("{\"status\": \"ready\", \"node\": \"weaving_arm_01\"}");
}

void loop() {
  // 1. LISTEN FOR COMMANDS FROM RASPBERRY PI
  if (Serial.available()) {
    StaticJsonDocument<200> doc;
    DeserializationError error = deserializeJson(doc, Serial);

    if (!error) {
      float target_x = doc["x"];
      float target_y = doc["y"];
      const char* action = doc["action"];

      // Logic to move motors would go here
      // digitalWrite(MOTOR_DIR_PIN, HIGH);
      // pulse(MOTOR_STEP_PIN);
      
      // 2. SEND TELEMETRY BACK (Simulated Tension)
      StaticJsonDocument<100> telemetry;
      telemetry["tension"] = random(2, 8); // Simulate real-time Newtons from HX711
      telemetry["step"] = "ack";
      serializeJson(telemetry, Serial);
      Serial.println();
    }
  }
}
