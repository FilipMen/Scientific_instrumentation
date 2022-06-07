float getCurrent() {
  mean = 0;
  ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  for (int i = 0; i < 10; i++) {
    adc = ads.readADC_SingleEnded(0);
    mean += ads.computeVolts(adc);
    delay(1);
  }
  return mean / 10;
}

float getVoltage() {
  mean = 0;
  ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  for (int i = 0; i < 10; i++) {
    adc = ads.readADC_SingleEnded(1);
    mean += ads.computeVolts(adc);
    delay(1);
  }
  return mean / 10;
}
