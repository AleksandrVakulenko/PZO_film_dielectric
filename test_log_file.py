
from random import random
from Log_files import LogFile


log_file_name = 'delete.txt'

c_d_r_x = [0, 0, 0, 0]

log_file = LogFile(log_file_name)
time = 1
frequency = 20
for i in range(100):
    time = time * 1.12
    temperature = random()*200
    frequency = frequency * 1.1
    c_d_r_x[0] = random()*1e-10
    c_d_r_x[1] = random()*0.3
    c_d_r_x[2] = random()*20e3
    c_d_r_x[3] = random()*200e3

    log_file.print(time, temperature, frequency, c_d_r_x)


