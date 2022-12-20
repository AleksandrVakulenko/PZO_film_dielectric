import numpy as np
import pyvisa as visa
import serial
import time
import matplotlib.pyplot as plot
from drawnow import *

# ===========================================
T_target1 = np.uint16(350)  # Первая целевая температура
T_target2 = np.uint16(30)  # Вторая целевая температура
rate = np.uint16(720)  # скорость
# ===========================================

ser = serial.Serial('COM4', baudrate=115200, timeout=30)
ser.flushInput()

T_tar = T_target1 * 100
T_tar_low = np.uint8(T_tar & 255)
T_tar_high = np.uint8(T_tar >> 8)
rate_low = np.uint8(rate & 255)
rate_high = np.uint8(rate >> 8)
control_data = ([6, 1, rate_high, rate_low, T_tar_high, T_tar_low])
ser.write(control_data)

val = []
cnt = 0
plot.ion()


# создаем функцию для построения графика
def make_fig():
    # plt.ylim(-5000,5000)
    plot.title('Capacity')
    plot.grid(True)
    plot.xlabel('time, s')
    plot.ylabel('C, F')
    plot.plot(val, 'ro-', label='Channel 0')
    plot.legend(loc='lower right')


f = open('mylog.txt', 'w')
f.write('T_thermocontroller T_self C D R X\n')
rm = visa.ResourceManager()
E4980AL = rm.open_resource('USB0::0x2A8D::0x2F01::MY54305367::INSTR')
idn = E4980AL.query('*IDN?')
print(idn)


# init temp value
ser_bytes = ser.read(44)
temperature = ((ser_bytes[4] << 8) + (ser_bytes[5])) / 100

time_start = time.time()
time_pass = 0

flag1 = 0
while time_pass < 3600:
    time_pass = time.time() - time_start
    print(time_pass)

    Z = E4980AL.query(':FETCh:IMPedance:FORmatted?')
    values_arr_C_D = Z.split(',', 2)
    value = (values_arr_C_D[0])  # for plotting

    Z = E4980AL.query(':FETCh:IMPedance:CORrected?')
    values_arr_R_X = Z.split(',', 2)

    val.append(float(value))
    drawnow(make_fig)

    cnt = cnt + 1
    if cnt > 21600:
        val.pop(0)

    # bytes_count = 0
    # while not bytes_count:
    #     bytes_count = ser.in_waiting
    #     print(bytes_count)

    bytes_count = ser.in_waiting
    if bytes_count >= 44:
        ser_bytes = ser.read(44)
        temperature = ((ser_bytes[4] << 8) + (ser_bytes[5])) / 100
        print('Thermocontroller:', temperature, '\n')
        ser.flushInput()
    else:
        pass

    if temperature < T_target1 and flag1 == 0:
        T_tar = T_target1 * 100
        T_tar_low = np.uint8(T_tar & 255)
        T_tar_high = np.uint8(T_tar >> 8)
        rate_low = np.uint8(rate & 255)
        rate_high = np.uint8(rate >> 8)
        ser.flushOutput()
        control_data = ([6, 1, rate_high, rate_low, T_tar_high, T_tar_low])
        ser.write(control_data)
        delta = abs(T_target1 - temperature)
        print('delta=', delta)
        if delta < 1:
            flag1 = 1

    if flag1 == 1:
        T_tar = T_target2 * 100
        T_tar_low = T_tar & 255
        T_tar_high = T_tar >> 8
        rate_low = np.uint8(rate & 255)
        rate_high = np.uint8(rate >> 8)
        ser.flushOutput()
        control_data = ([6, 1, rate_high, rate_low, T_tar_high, T_tar_low])
        ser.write(control_data)
        delta = abs(T_target2 - temperature)
        print('delta=', delta)

    temperature_str = str(temperature)
    # print(value)
    T_str = str(-1)
    msg = temperature_str + ' ' + T_str + ' ' + values_arr_C_D[0] + ' ' + values_arr_C_D[1] + ' ' + values_arr_R_X[
        0] + ' ' + values_arr_R_X[1]
    print(msg)
    f.write(msg)


E4980AL.close()