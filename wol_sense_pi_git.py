from wakeonlan import send_magic_packet
import grovepi
import time
import paho.mqtt.client as mqtt
import math



def on_connect(client, userdata, flags, rc):
    print("Connected to home server/broker with result code " + str(rc))


def main():

    grovepi.set_bus("RPI_1")
    ultrasonic_ranger = 4
    
    temp_sensor = 3
    blue = 0
    white = 1

    sound_sensor = 0
    grovepi.pinMode(sound_sensor, "INPUT")

    #light_sensor = 1
    #grovepi.pinMode(light_sensor, "INPUT")

    client = mqtt.Client()
    client.on_connect = on_connect
    
    
    client.connect(host='192.168.0.19', port=1883, keepalive=60)
    client.loop_start()
    flag = 0
    
    while (True):
        try:
            
            distance = grovepi.ultrasonicRead(ultrasonic_ranger)
            client.publish("home/leos_room/wol_sense", distance)
            if distance < 100 and flag == 0:
                send_magic_packet('80-45-DD-71-D5-CC')
                flag = flag+1 
            
            [temp,humidity] = grovepi.dht(temp_sensor, blue)
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                 client.publish("home/leos_room/temp", temp)
                 client.publish("home/leos_room/humidity", humidity)
            
            sound_value = grovepi.analogRead(sound_sensor)
            client.publish("home/leos_room/sound", sound_value) 
            
            #sensor_value = grovepi.analogRead(light_sensor)
            #client.publish("room_data/light", sensor_value)

        except Exception as e:
            print("Error:{}".format(e))
        
        except KeyboardInterrupt:
            break
        
        except IOError:
            print("Error")


        time.sleep(0.1)
        

if __name__ == "__main__":
    main()
