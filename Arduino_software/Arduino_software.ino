// Declare the Adafruit ADC and DAC
String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete
String json = "{\"sp\":0}";
#include <Wire.h>
#include <Adafruit_MCP4725.h>
#include <ArduinoJson.h>
#include <Adafruit_ADS1X15.h>

float sp = 0;
float cellV = 0;
float cellC = 0;
uint32_t dacV = 0;
int16_t adc;
float mean = 0;

// FEM variables
byte state = 0;
boolean start = false;
boolean finish = false;
boolean rx = false;
int num_i = 1;
int res = 1;

Adafruit_MCP4725 dac;
Adafruit_ADS1115 ads;  /* Use this for the 16-bit version */


void setup(void)
{
  Serial.begin(115200);
  Serial.println("Scientific intrumentation project");


  //---------------------------- Configure the DAC ---------------------------------------
  dac.begin(0x60);
  dac.setVoltage(0, false);
  //------------------------------------------------------------------------------------


  //---------------------------- Configure the ADC ----------------------------------------
  // The ADC input range (or gain) can be changed via the following
  // functions, but be careful never to exceed VDD +0.3V max, or to
  // exceed the upper and lower limits if you adjust the input range!
  // Setting these values incorrectly may destroy your ADC!
  //                                                                ADS1015  ADS1115
  //                                                                -------  -------
  // ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  // ads.setGain(GAIN_ONE);        // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  // ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);       // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  // ads.setGain(GAIN_EIGHT);      // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN);    // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
  if (!ads.begin()) {
    Serial.println("Failed to initialize ADS.");
    while (1);
  }
  //------------------------------------------------------------------------------------

  //-----------------Set timer1 interrupt at 10Hz----------------------------------------
  cli();//stop interrupts
  //set timer1 interrupt at 1Hz
  TCCR1A = 0;// set entire TCCR1A register to 0
  TCCR1B = 0;// same for TCCR1B
  TCNT1  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  OCR1A = 6249;// = (16*10^6) / (1*1024) - 1 (must be <65536)
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS10 CS11 and CS12 bits
  //TCCR1B |= (0 << CS12) | (0 << CS11) | (1 << CS10); // No prescaling
  //TCCR1B |= (0 << CS12) | (1 << CS11) | (0 << CS10); // 8 prescaler
  //TCCR1B |= (0 << CS12) | (1 << CS11) | (1 << CS10); // 64 prescaler
  TCCR1B |= (1 << CS12) | (0 << CS11) | (0 << CS10); // 256 prescaler
  //TCCR1B |= (1 << CS12) | (0 << CS11) | (1 << CS10); // 1024 prescaler
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);
  sei();//allow interrupts
  //--------------------------------------------------------------------------------------
}

void loop(void)
{
  // print the string when a newline arrives:
  //  if (stringComplete) {
  //    //SetP = inputString.toFloat();
  //    voltage = inputString.toFloat();
  //    dacV = voltage * 4091 / 5.02;
  //    dac.setVoltage(dacV, false);
  //  }

  //  adc0 = ads.readADC_SingleEnded(0);
  //  adc1 = ads.readADC_SingleEnded(1);
  //  volts0 = ads.computeVolts(adc0);
  //  volts1 = ads.computeVolts(adc1);
  FEM();
}
