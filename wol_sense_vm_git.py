import paho.mqtt.client as mqtt
import time 


def custom_callback_ult(client, userdata, message):
    ult_read = str(message.payload.decode("utf-8"))
    print("Ultrasonic Distance : " + ult_read + "cm")
    

def custom_callback_hum(client, userdata, message):
    hum_read = str(message.payload.decode("utf-8"))
    print("Humidity: " + hum_read + "%")
    

def custom_callback_temp(client, userdata, message):
    temp_read = str(message.payload.decode("utf-8"))
    print("Temperature " + temp_read + "C")

def custom_callback_sound(client, userdata, message):
    sound_read = str(message.payload.decode("utf-8"))
    print("Relative Sound Value ", sound_read)

#def custom_callback_light(client, userdata, message):
    #light_read = str(message.payload.decode("utf-8"))
    #print("Light Value: " + light_read)
    #print(" ")

def on_connect(client, userdata, flags, rc):
    print("Connected to home server/broker with result code " + str(rc))

    client.subscribe("home/leos_room/wol_sense")
    client.message_callback_add("home/leos_room/wol_sense", custom_callback_ult)

    client.subscribe("home/leos_room/temp")
    client.message_callback_add("home/leos_room/temp", custom_callback_temp)
    
    client.subscribe("home/leos_room/humidity")
    client.message_callback_add("home/leos_room/humidity", custom_callback_hum)
    
    client.subscribe("home/leos_room/sound")
    client.message_callback_add("home/leos_room/sound", custom_callback_sound)

    #client.subscribe("room_data/light")
    #client.message_callback_add("room_data/light", custom_callback_light)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host='192.168.0.19', port=1883, keepalive=60)
    client.loop_start()

    while(True):
        
        time.sleep(1)








