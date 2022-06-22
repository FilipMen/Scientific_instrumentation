void FEM1() {
  switch (state) {
    case 0:
      break;
    case 1:
      break;
    case 2:
      dac.setVoltage(4091, false);
      delay(10);
      cellC = getCurrent();
      cellV = getVoltage();
      Json();
      dacV = 1000;
      float maxC = cellC;
      for (int i = res - 1; i >= 1; i--) {
        sp = maxC * (i / (res * 1.0));
        if (sp < 0.12) {
          break;
        }
        float error = sp - cellC;
        float cError = 0;
        while (abs(error) > 0.05) {
          cellC = getCurrent();
          error = sp - cellC;
          cError += error;
          Serial.print(sp);
          dacV += 2 * error + 0.01* cError;
          Serial.print(" ");
          Serial.print(dacV);
          Serial.print(" ");
          Serial.println(cellC);
          dac.setVoltage(dacV, false);
        }
        cellV = getVoltage();
        Json();
      }
      dac.setVoltage(0, false);
      delay(10);
      cellC = getCurrent();
      cellV = getVoltage();
      rx = false;
      Json();
      state = 0;
      break;
  }
}
