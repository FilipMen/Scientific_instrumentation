void Json(){
  DynamicJsonDocument doc(256);
  doc["rx"] = rx;
  doc["V"] = cellV;
  doc["C"] = cellC;
  serializeJson(doc, Serial);
  Serial.println();
}
