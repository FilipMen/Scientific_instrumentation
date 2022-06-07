void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // If the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      if (inputString == "Start") {
        state = 1;
        Serial.println("Receive");
      }
      if (inputString == "Stop") {
        Serial.println("Stop");
        state = 0;
      }
      if (state == 1) {
        json = inputString;
        DeserializeObject();
        if (rx) {
          state = 2;
        }
      }
      //json = inputString;
      //DeserializeObject();
      inputString = "";
    }
    else { // Else add it to the inputString:
      inputString += inChar;
    }
  }
}

void DeserializeObject()
{
  StaticJsonDocument<300> doc;
  DeserializationError error = deserializeJson(doc, json);
  if (error) {
    return;
  }
  //sp = doc["sp"];
  rx = doc["rx"];
  num_i = doc["i"];
  res = doc["r"];
}
