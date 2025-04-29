import serial
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 

ser = serial.Serial('COM5',9600)
data = pd.read_csv("D:\\Python\\Green_H2\\seattle-weather.csv")
data.drop(columns=['date'],inplace=True)
mapping_dict = {'snow':"cloudy", 'rain':"cloudy", "sun":"sun", "fog":"fog"}
data["desc"] = data.weather.map(mapping_dict)
data.dropna(axis=0,inplace=True)
data.drop(columns=["weather"],inplace=True)
classifier = RandomForestClassifier(n_estimators=100,random_state=1)
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train ,x_test  , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=False)
classifier.fit(x_train,y_train)

time.sleep(2)
temp = []
while True:
  line = ser.readline().decode("utf-8")
  humuidity = line[10:15]
  temperature = line[36:41]
  humuidity_2 = line[15:20]
  temperature_2 = line[41:46]
  if temperature == "":
    continue
  else:
    float_temp = float(temperature)
    temp.sort()
    temp.append(float_temp)
    max_temp = temp[-1]
    Min_temp = temp[0]
    # print(f"Temperature = {temperature}")
    # print(f"humuidity = {humuidity}")
    # print(f"Temperature = {temperature_2}")
    # print(f"humuidity = {humuidity_2}")
    test = pd.DataFrame({"precipitation":[humuidity],"temp_max":[max_temp],"temp_min":[Min_temp],"wind":[4.166]})
    print(classifier.predict(test)[0])
    
