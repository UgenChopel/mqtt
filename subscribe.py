import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):  # rc - return/result code
    print("Connected with rc " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    value = float(message.payload)  # converting the payload into float
    print(message.topic, "=", round(value, 2))  # value rounded off to 2


client = mqtt.Client("DSO algorithm")
client.username_pw_set("username")
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io")  # directly connecting the client to online server
# client1.subscribe([("Voltage/1", 0), ("Voltage/2", 1), ("Voltage/3", 2)])  # number 0,1,&2 represent QoS

nodes = 15  # Enter the no. of nodes of a system
for i in range(0, nodes):
    client.subscribe("Voltage/{}".format(i), 1)  # number 1 is the QoS (options: 0,1 & 2)


client.loop_forever()

'''
# Error code function
def error(code):
    return {
        0: "Connection Accepted",
        -1: "Socket Error",
        1: "Unsupported MQTT version",
        2: "Client ID rejected",
        3: "Server unavailable",
        4: "Invalid username/password",
        5: "Not authorized",
    }.get(code, "Unknown error")
'''
