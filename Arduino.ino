#include "DHT.h"
#define DHTPIN 2 
#define DHTPIN_2 3   
#define DHTTYPE DHT11  
#define  MQ_PIN                       (4)     
#define RL_VALUE                     (10)    
#define RO_CLEAN_AIR_FACTOR          (9.21)
#define  CALIBARAION_SAMPLE_TIMES     (50)    
#define  CALIBRATION_SAMPLE_INTERVAL  (500)                                                     
#define  READ_SAMPLE_INTERVAL         (50)    
#define  READ_SAMPLE_TIMES            (5)                                                        
#define GAS_H2 (0)
float H2Curve[3]  =  {2.3, 0.93,-1.44};    
float Ro=  10;                 
DHT dht(DHTPIN, DHTTYPE);
DHT dht_2(DHTPIN_2,DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  dht_2.begin();
  // Serial.print("Calibrating...\n");                
  Ro = MQCalibration(MQ_PIN);                        //Calibrating the sensor. Please make sure the sensor is in clean air 
                                                     //when you perform the calibration                    
  // Serial.print("Calibration is done...\n"); 
  // Serial.print("Ro=");
  // Serial.print(Ro);
  // Serial.print("kohm");
  // Serial.print("\n");
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  float h_2 = dht_2.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  float t_2 = dht_2.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
  float f_2 = dht_2.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  
  }

  if (isnan(h_2) || isnan(t_2) || isnan(f_2)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  float hif_2 = dht.computeHeatIndex(f_2, h_2);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);
  float hic_2 = dht.computeHeatIndex(t_2, h_2, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(h_2);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(t_2);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(f_2);
  // Serial.print(F("°F  Heat index: "));
  // Serial.print(hic);
  // Serial.print(hic_2);
  // Serial.print(F("°C "));
  // Serial.print(hif);
  // Serial.print(hif_2);
  // Serial.print(F("°F"));
  Serial.print("H2 Concentration:"); 
  Serial.print(MQGetGasPercentage(MQRead(MQ_PIN)/Ro,GAS_H2) );
  Serial.print( "ppm" );
  Serial.print("\n");
  //delay(200);
}

float MQResistanceCalculation(int raw_adc) {
  return ( ((float)RL_VALUE*(1023-raw_adc)/raw_adc));
}

float MQCalibration(int mq_pin) {
  int i;
  float val=0;
 
  for (i=0;i<CALIBARAION_SAMPLE_TIMES;i++) {            //take multiple samples
    val += MQResistanceCalculation(analogRead(mq_pin));
    delay(CALIBRATION_SAMPLE_INTERVAL);
  }
  val = val/CALIBARAION_SAMPLE_TIMES;                   //calculate the average value
 
  val = val/RO_CLEAN_AIR_FACTOR;                        //divided by RO_CLEAN_AIR_FACTOR yields the Ro 
                                                        //according to the chart in the datasheet 
 
  return val; 
}

float MQRead(int mq_pin) {
  int i;
  float rs=0;
 
  for (i=0;i<READ_SAMPLE_TIMES;i++) {
    rs += MQResistanceCalculation(analogRead(mq_pin));
    delay(READ_SAMPLE_INTERVAL);
  }
 
  rs = rs/READ_SAMPLE_TIMES;
 
  return rs;  
}

int MQGetGasPercentage(float rs_ro_ratio, int gas_id) {
  if ( gas_id == GAS_H2) {
     return MQGetPercentage(rs_ro_ratio,H2Curve);
  }  
  return 0;
}

int  MQGetPercentage(float rs_ro_ratio, float *pcurve) {
  return (pow(10,( ((log(rs_ro_ratio)-pcurve[1])/pcurve[2]) + pcurve[0])));
}
