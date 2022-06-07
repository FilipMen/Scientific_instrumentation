void FEM() {
  switch (state) {
    case 0:
      break;
    case 1:
      break;
    case 2:
      dac.setVoltage(0, false);
      delay(10);
      cellC = getCurrent();
      cellV = getVoltage();
      Json();
      dacV = 1000;
      float maxV = cellV;
      for (int i = res - 1; i >= 1; i--) {
        sp = maxV * (i / (res * 1.0));
        if (sp < 0.1) {
          break;
        }
        float error = sp - cellV;
        float cError = 0;
        while (abs(error) > 0.05) {
          cellV = getVoltage();
          error = sp - cellV;
          cError += error;
          Serial.print(sp);
          dacV -= 5 * error + 5 * cError;
          Serial.print(" ");
          Serial.print(dacV);
          Serial.print(" ");
          Serial.println(cellV);
          dac.setVoltage(dacV, false);
        }
        cellC = getCurrent();
        Json();
      }
      dac.setVoltage(4091, false);
      delay(10);
      cellC = getCurrent();
      cellV = getVoltage();
      rx = false;
      Json();
      state = 0;
      break;
  }
}
