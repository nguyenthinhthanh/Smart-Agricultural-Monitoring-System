from mqtt import *
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from aiot_lcd1602 import LCD1602
from machine import RTC
import ntptime
import time
from event_manager import *
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20

def on_mqtt_message_receive_callback__bbc_time_start_(server_time_start):
  global server_mode, server_manual_watering, server_manual_temperature, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
  display.scroll(server_time_start)
  display.scroll((int((server_time_start[3 : 5]))))
  time_start = (int((server_time_start[ : 2]))) * 60
  time_start = (time_start if isinstance(time_start, (int, float)) else 0) + (int((server_time_start[3 : 5])))

def on_mqtt_message_receive_callback__bbc_time_end_(server_time_end):
  global server_mode, server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold
  time_end = (int((server_time_end[ : 2]))) * 60
  time_end = (time_end if isinstance(time_end, (int, float)) else 0) + (int((server_time_end[3 : 5])))

# Mô tả hàm này...
def schedule_watering():
  global server_time_start, server_mode, server_manual_watering, server_manual_temperature, server_time_end, frame_mode, temperatue, time2, time_end, temperature_threshold, humidity, time_start, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold, aiot_lcd1602, aiot_dht20
  mqtt.on_receive_message('bbc-time-start', on_mqtt_message_receive_callback__bbc_time_start_)
  mqtt.on_receive_message('bbc-time-end', on_mqtt_message_receive_callback__bbc_time_end_)

def on_mqtt_message_receive_callback__bbc_server_mode_(server_mode):
  global server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
  frame_mode = int(server_mode)

# Mô tả hàm này...
def mode_selection():
  global server_time_start, server_mode, server_manual_watering, server_manual_temperature, server_time_end, frame_mode, temperatue, time2, time_end, temperature_threshold, humidity, time_start, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold, aiot_lcd1602, aiot_dht20
  mqtt.on_receive_message('bbc-server-mode', on_mqtt_message_receive_callback__bbc_server_mode_)

def on_mqtt_message_receive_callback__bbc_manual_watering_(server_manual_watering):
  global server_mode, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
  if frame_mode == 0:
    if server_manual_watering == '1':
      pin14.write_analog(round(translate(70, 0, 100, 0, 1023)))
    else:
      pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))

# Mô tả hàm này...
def manual_watering():
  global server_time_start, server_mode, server_manual_watering, server_manual_temperature, server_time_end, frame_mode, temperatue, time2, time_end, temperature_threshold, humidity, time_start, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold, aiot_lcd1602, aiot_dht20
  mqtt.on_receive_message('bbc-manual-watering', on_mqtt_message_receive_callback__bbc_manual_watering_)

def on_mqtt_message_receive_callback__bbc_manual_temperature_(server_manual_temperature):
  global server_mode, server_manual_watering, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
  if frame_mode == 0:
    if server_manual_temperature == '1':
      pin10.write_analog(round(translate(50, 0, 100, 0, 1023)))
    else:
      pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))

# Mô tả hàm này...
def manual_temperature():
  global server_time_start, server_mode, server_manual_watering, server_manual_temperature, server_time_end, frame_mode, temperatue, time2, time_end, temperature_threshold, humidity, time_start, soil_threshold, light, soil_moisture, server_temp_threshold, server_soil_threshold, aiot_lcd1602, aiot_dht20
  mqtt.on_receive_message('bbc-manual-temperature', on_mqtt_message_receive_callback__bbc_manual_temperature_)

aiot_lcd1602 = LCD1602()

def on_mqtt_message_receive_callback__bbc_temperature_threshold_(server_temp_threshold):
  global server_mode, server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_soil_threshold, server_time_end
  temperature_threshold = int(server_temp_threshold)

def on_mqtt_message_receive_callback__bbc_soil_moisture_threshold_(server_soil_threshold):
  global server_mode, server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_time_end
  soil_threshold = int(server_soil_threshold)

event_manager.reset()

aiot_dht20 = DHT20()

def on_event_timer_callback_Q_F_l_q_Y():
  global server_mode, server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
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

event_manager.add_timer_event(10000, on_event_timer_callback_Q_F_l_q_Y)

def on_event_condition_callback_R_d_t_i_X():
  global server_mode, server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
  if (aiot_dht20.dht20_temperature()) > temperature_threshold:
    pin10.write_analog(round(translate(50, 0, 100, 0, 1023)))
    mqtt.publish('bbc-manual-temperature', '1')
  else:
    pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))
    mqtt.publish('bbc-manual-temperature', '0')
  if (round(translate((pin0.read_analog()), 0, 4095, 0, 100))) < soil_threshold:
    pin14.write_analog(round(translate(70, 0, 100, 0, 1023)))
    mqtt.publish('bbc-manual-watering', '1')
  else:
    pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))
    mqtt.publish('bbc-manual-watering', '0')

event_manager.add_condition_event(lambda:(frame_mode == 1), on_event_condition_callback_R_d_t_i_X)

def on_event_timer_callback_u_T_F_l_M():
  global server_mode, server_manual_watering, server_manual_temperature, server_time_start, frame_mode, temperatue, time2, temperature_threshold, humidity, soil_threshold, light, time_start, soil_moisture, time_end, server_temp_threshold, server_soil_threshold, server_time_end
  if frame_mode == 1:
    time2 = (int(('%0*d' % (2, RTC().datetime()[4])))) * 60
    time2 = (time2 if isinstance(time2, (int, float)) else 0) + (int(('%0*d' % (2, RTC().datetime()[5]))))
    if time2 > time_start:
      pin14.write_analog(round(translate(70, 0, 100, 0, 1023)))
      mqtt.publish('bbc-manual-watering', '1')
    if time2 > time_end:
      pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))
      mqtt.publish('bbc-manual-watering', '0')
  else:
    display.scroll(frame_mode)

event_manager.add_timer_event(5000, on_event_timer_callback_u_T_F_l_M)

if True:
  aiot_lcd1602.clear()
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('Smart Agricultural Monitoring')
  temperature_threshold = 30
  soil_threshold = 0
  frame_mode = 0
  time_start = 1439
  time_end = 1439
  display.scroll('SAMS')
  mqtt.connect_wifi('ACLAB', 'ACLAB2023')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='nguyenthinhthanh', password='aio_ncvb01rNvHwY2qgnDZm9JBHzq6gE')
  display.scroll('Ok')
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  mqtt.on_receive_message('bbc-temperature-threshold', on_mqtt_message_receive_callback__bbc_temperature_threshold_)
  mqtt.on_receive_message('bbc-soil-moisture-threshold', on_mqtt_message_receive_callback__bbc_soil_moisture_threshold_)
  mode_selection()
  manual_watering()
  manual_temperature()
  schedule_watering()

while True:
  mqtt.check_message()
  event_manager.run()
  time.sleep_ms(1000)
  time.sleep_ms(10)
