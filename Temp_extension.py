import serial
import numpy as np

def set_temp_rate(serial, temp_target, temp_rate):
    T_tar = temp_target * 100
    T_tar_low = np.uint8(T_tar & 255)
    T_tar_high = np.uint8(T_tar >> 8)
    rate_low = np.uint8(temp_rate & 255)
    rate_high = np.uint8(temp_rate >> 8)
    serial.flushOutput()
    control_data = ([6, 1, rate_high, rate_low, T_tar_high, T_tar_low])
    serial.write(control_data)


def connect(com_port_name):
    ser_obj = serial.Serial(com_port_name, baudrate=115200, timeout=30)
    ser_obj.flushInput()
    return ser_obj

