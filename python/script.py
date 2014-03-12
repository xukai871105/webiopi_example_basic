# -*- coding: utf-8 -*-
import webiopi

GPIO = webiopi.GPIO

# GPIO 17 BCM编码方式
LIGHT = 17 

# 初始化程序，webiopi初始化时自动调用
def setup():
    # 设置GPIO 17为输出状态
    GPIO.setFunction(LIGHT, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():

    # 给CPU运行时间
    webiopi.sleep(1)

# 回收程序，webiopi停止运行时调用，非常实用
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
