import time
import keyboard
import draw_lib
from RLC_extension import LCRmeter
from Temp_extension import TempController
from Log_files import LogFile

# ===========================================
T_target1 = 425  # [C] (Первая целевая температура)
T_target2 = 30  # [C] (Вторая целевая температура)
rate = 150  # [C/min] (скорость)
measurement_frequency = 1000  # [Hz]
measurement_voltage = 0.05  # [V]
com_port_name = 'COM4'
log_file_name = 'log 2022_12_XX_test.txt'
# ===========================================
delta_limit = T_target1 / 90

# connect to LCR
lcr_device = LCRmeter()
lcr_device.set_frequency(measurement_frequency)
lcr_device.set_voltage(measurement_voltage)

# connect to thermocontroller
temp_device = TempController(com_port_name)
temp_device.set_temp_rate(T_target1, rate)

# log file creation
log_file_obj = LogFile(log_file_name)

# Main cycle start
flag_temp_phase = 0  # 0 - heat, 1 - cool, 2 - cool ended
time_start = time.time()
while flag_temp_phase != 2:
    if keyboard.is_pressed('q'):  # close by q key
        print('You Pressed q Key!')
        break

    # update all variables
    time_pass = time.time() - time_start
    temperature = temp_device.get_temp()
    c_d_r_x = lcr_device.get_c_d_r_x()

    # check temperature phases
    if temperature < T_target1 and flag_temp_phase == 0:
        temp_device.set_temp_rate(T_target1, rate)
        delta = abs(T_target1 - temperature)
        if delta < delta_limit:
            flag_temp_phase = 1

    if flag_temp_phase == 1:
        temp_device.set_temp_rate(T_target2, rate)
        delta = abs(T_target2 - temperature)
        if delta < delta_limit:
            flag_temp_phase = 2

    # draw to window and print to log file
    draw_lib.draw_figure(time_pass, temperature, c_d_r_x)
    log_file_obj.print(time_pass, temperature, c_d_r_x)



