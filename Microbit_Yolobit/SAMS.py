from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import urequests
import gc
from aiot_lcd1602 import LCD1602
from yolobit_wifi import *
from mqtt import *
from machine import RTC
import ntptime
import time
from event_manager import *
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
import ujson

def auto_update_all_status():
    global http_response,aiot_dht20
    
    aiot_dht20.read_dht20()
    temperatue = aiot_dht20.dht20_temperature()
    humidity = aiot_dht20.dht20_humidity()
    light = round(translate((pin1.read_analog()), 0, 4095, 0, 100))
    soil_moisture = round(translate((pin0.read_analog()), 0, 4095, 0, 100))
    stats = f"{temperatue}-{humidity}-{light}-{soil_moisture}"
    showLCD(stats, 0)
    
    print("Sending data to server...")
    postData = {"temp":temperatue,"hum":humidity,"lig":light,"soil":soil_moisture}
    gc.collect()
    http_response = urequests.post(
        "http://ubuntu.scanfb.top:8000/yolobit_api",
        data=None,
        json=(postData),
    )
    response = ujson.loads(http_response.text)
    fan_state = [device['state'] for device in response['data'] if device['device_name'] == 'mini_fan'][0]
    pump_state = [device['state'] for device in response['data'] if device['device_name'] == 'water_pump'][0]
    
    pin10.write_analog(round(translate(fan_state * 50, 0, 100, 0, 1023)))
    pin14.write_analog(round(translate(pump_state * 70, 0, 100, 0, 1023)))
    showLCD(f"FAN:{"ON" if fan_state == 1 else "OFF"}-PUMP:{"ON" if pump_state == 1 else "OFF"}", 1)


aiot_lcd1602 = LCD1602()
aiot_lcd1602.clear()
aiot_dht20 = DHT20()
def showLCD(msg, line_idx = 0):
    print(msg)
    aiot_lcd1602.move_to(0, line_idx)
    aiot_lcd1602.putstr(f"{msg}{" " * (16-len(msg))}")

if True:
    showLCD("Init...")
    display.scroll("!")
    
    temperature_threshold = 30
    soil_threshold = 0
    frame_mode = 0
    time_start = 1439
    time_end = 1439
    mini_fan_state = 0
    water_pump_state = 0
    schedule_state = 0
    
    showLCD("Connect wifi...")
    # wifi_name = "akng - laptop"
    # wifi_pwd = "kiet2509"
    wifi_name = "ACLAB"
    wifi_pwd = "ACLAB2023"
    wifi.connect_wifi(wifi_name, wifi_pwd)
    
    showLCD("Connect ada...")
    ntptime.settime()
    (year, month, mday, week_of_year, hour, minute, second, milisecond) = (
        RTC().datetime()
    )
    RTC().init((year, month, mday, week_of_year, hour + 7, minute, second, milisecond))
    showLCD("All done!")

while True:
    auto_update_all_status()