import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import random

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Bus_voltage")
client.connect(mqttBroker)

while True:
    randNumber1 = randrange(10)
    randNumber2 = random.uniform(0.9, 1.08)
    randNumber3 = randrange(30, 40)
    randNumber4 = random.uniform(40, 50)

    # multiple topics
    client.publish("Voltage/1", randNumber1)  # Voltage/1 is the Topic and randNumber1 is the payload/message
    client.publish("Voltage/2", randNumber2)
    client.publish("Voltage/3", randNumber3)
    client.publish("Voltage/4", randNumber4)

    print("Published ", round(randNumber1, 2), " to Topic Voltage/1")
    print("Published ", round(randNumber2, 2), " to Topic Voltage/2")
    # print("Published ", round(randNumber3, 2), " to Topic Voltage/3")
    # print("Published ", round(randNumber4, 2), " to Topic Voltage/4")
    print("")
    time.sleep(3)
