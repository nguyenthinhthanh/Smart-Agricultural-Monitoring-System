from aiot_lcd1602 import LCD1602
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from mqtt import *
from event_manager import *
import time
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20

aiot_lcd1602 = LCD1602()

def on_mqtt_message_receive_callback__bbc_temperature_threshold_(server_temp_threshold):
  global temperatue, temperature_threshold, humidity, soil_threshold, light, soil_moisture, server_soil_threshold
  temperature_threshold = int(server_temp_threshold)

def on_mqtt_message_receive_callback__bbc_soil_moisture_threshold_(server_soil_threshold):
  global temperatue, temperature_threshold, humidity, soil_threshold, light, soil_moisture, server_temp_threshold
  soil_threshold = int(server_soil_threshold)

event_manager.reset()

aiot_dht20 = DHT20()

def on_event_timer_callback_Q_F_l_q_Y():
  global temperatue, temperature_threshold, humidity, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold
  aiot_dht20.read_dht20()
  temperatue = aiot_dht20.dht20_temperature()
  humidity = aiot_dht20.dht20_humidity()
  light = light_level()
  soil_moisture = round(translate((pin0.read_analog()), 0, 4095, 0, 100))
  mqtt.publish('bbc-temperature', temperatue)
  mqtt.publish('bbc-humidity', humidity)
  mqtt.publish('bbc-light', light)
  mqtt.publish('bbc-soil-moisture', soil_moisture)
  aiot_lcd1602.clear()
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('Temp:')
  aiot_lcd1602.move_to(5, 0)
  aiot_lcd1602.putstr(temperatue)
  aiot_lcd1602.move_to(9, 0)
  aiot_lcd1602.putstr(' Lig:')
  aiot_lcd1602.move_to(14, 0)
  aiot_lcd1602.putstr(light)
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('Hum:')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr(humidity)
  aiot_lcd1602.move_to(9, 1)
  aiot_lcd1602.putstr('Soil:')
  aiot_lcd1602.move_to(14, 1)
  aiot_lcd1602.putstr(soil_moisture)

event_manager.add_timer_event(5000, on_event_timer_callback_Q_F_l_q_Y)

def on_event_condition_callback_F_N_C_q_O():
  global temperatue, temperature_threshold, humidity, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold
  pin10.write_analog(round(translate(50, 0, 100, 0, 1023)))

event_manager.add_condition_event(lambda:((aiot_dht20.dht20_temperature()) > temperature_threshold), on_event_condition_callback_F_N_C_q_O)

def on_event_condition_callback_J_g_a_U_d():
  global temperatue, temperature_threshold, humidity, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold
  pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))

event_manager.add_condition_event(lambda:((aiot_dht20.dht20_temperature()) <= temperature_threshold), on_event_condition_callback_J_g_a_U_d)

if True:
  aiot_lcd1602.clear()
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('Smart Agricultural Monitoring')
  temperature_threshold = 30
  soil_threshold = 0
  display.scroll('SAMS')
  mqtt.connect_wifi('ACLAB', 'ACLAB2023')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='nguyenthinhthanh', password='aio_ncvb01rNvHwY2qgnDZm9JBHzq6gE')
  display.scroll('Ok')
  mqtt.on_receive_message('bbc-temperature-threshold', on_mqtt_message_receive_callback__bbc_temperature_threshold_)
  mqtt.on_receive_message('bbc-soil-moisture-threshold', on_mqtt_message_receive_callback__bbc_soil_moisture_threshold_)

while True:
  mqtt.check_message()
  event_manager.run()
  display.scroll(temperature_threshold)
  time.sleep_ms(1000)
  time.sleep_ms(10)


aiot_dht20.dht20_temperature()
