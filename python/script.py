# -*- coding: utf-8 -*-
import webiopi

GPIO = webiopi.GPIO

# GPIO 17 BCM���뷽ʽ
LIGHT = 17 

# ��ʼ������webiopi��ʼ��ʱ�Զ�����
def setup():
    # ����GPIO 17Ϊ���״̬
    GPIO.setFunction(LIGHT, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():

    # ��CPU����ʱ��
    webiopi.sleep(1)

# ���ճ���webiopiֹͣ����ʱ���ã��ǳ�ʵ��
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
