import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "bbc-led"
AIO_USERNAME = "nguyenthinhthanh"
AIO_KEY = "aio_ncvb01rNvHwY2qgnDZm9JBHzq6gE"

def connected(client):
    print("Connected ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe success ...")

def disconnected(client):
    print("Disconnected ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Data receive: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    value = random.randint(0, 100)
    print("Update value:", value)
    client.publish("bbc-temp", value)
    time.sleep(30)