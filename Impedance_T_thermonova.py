import numpy as np
import time
import matplotlib.pyplot as plot
from drawnow import drawnow
import keyboard
import RLC_extension
import Temp_extension

# ===========================================
T_target1 = np.uint16(425)  # Первая целевая температура
T_target2 = np.uint16(30)  # Вторая целевая температура
rate = np.uint16(150)  # скорость
com_port_name = 'COM4'
log_file_name = 'log 2022_12_23_1.txt'
# ===========================================
delta_limit = T_target1 / 90


# COM port connection
ser = Temp_extension.connect(com_port_name)
# initially set temp and rate
Temp_extension.set_temp_rate(ser, T_target1, rate)

val = []
cnt = 0
plot.ion()

# создаем функцию для построения графика
def make_fig():
    plot.title('Capacity')
    plot.grid(True)
    plot.xlabel('time, s')
    plot.ylabel('C, F')
    plot.plot(val, 'ro-', label='Channel 0')
    plot.legend(loc='lower right')


# log file creation
f = open(log_file_name, 'w')
f.write('T_thermocontroller T_self C D R X\n')


# RLC device connection (E4980AL only)
E4980AL = RLC_extension.connect()


# init temp value
ser_bytes = ser.read(44)
temperature = ((ser_bytes[4] << 8) + (ser_bytes[5])) / 100

time_start = time.time()
time_pass = 0

flag_temp_phase = 0
while flag_temp_phase != 2:
    # close by q key
    if keyboard.is_pressed('q'):
        print('You Pressed q Key!')
        break  # finishing the loop

    time_pass = time.time() - time_start
    print(time_pass)

    c_d_r_x = RLC_extension.get_data(E4980AL)
    values_arr_C_D = [c_d_r_x[0], c_d_r_x[1]]
    values_arr_R_X = [c_d_r_x[2], c_d_r_x[3]]
    value = (values_arr_C_D[0])  # for plotting

    val.append(float(value))
    drawnow(make_fig)

    bytes_count = ser.in_waiting
    if bytes_count >= 44:
        ser_bytes = ser.read(44)
        temperature = ((ser_bytes[4] << 8) + (ser_bytes[5])) / 100
        print('Thermocontroller:', temperature, '\n')
        ser.flushInput()
    else:
        pass

    if temperature < T_target1 and flag_temp_phase == 0:
        Temp_extension.set_temp_rate(ser, T_target1, rate)
        delta = abs(T_target1 - temperature)
        if delta < delta_limit:
            flag_temp_phase = 1

    if flag_temp_phase == 1:
        Temp_extension.set_temp_rate(ser, T_target1, rate)
        delta = abs(T_target2 - temperature)
        if delta < delta_limit:
            flag_temp_phase = 2

    temperature_str = str(temperature)
    T_str = str(-1)
    msg = temperature_str + ' ' + T_str + ' ' + values_arr_C_D[0] + ' ' + values_arr_C_D[1] + ' ' + values_arr_R_X[
        0] + ' ' + values_arr_R_X[1]
    print(msg)
    f.write(msg)

ser.close()
print('COM port closed')
RLC_extension.disconnect(E4980AL)
print('RLC closed!')