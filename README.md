# room_data

Team Members:
Leonardo Martinez


Link to Demo Video:
https://drive.google.com/file/d/16qoVgToKsaQHy7I_Y3CxuR4bY09mkKTh/view?usp=sharing


Compile Instructions:
First thing you have to do is install mosquitto, mosquitto clients, paho-mqtt, inluxdb, and grafana. Run the MQTTInfluxDBBridge script on the machine you are using as your mqtt broker. Make sure the Grove module and pywakeonlan module are in the same directory as the wol_sense_pi_git.py file and then you can proceed to run the wol_sense_pi_git.py script to begin collecting sensor data and publish it to the mqtt-broker. Then run the wol_sense_vm_git.py script to subscribe to the mqtt topics and receive the sensor data also.

All Libraries Used:
GrovePi
Paho-mqtt
pywakeonlan
influxdbClient
