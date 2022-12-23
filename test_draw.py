import time
import random
import draw_lib_for_test


time_start = time.time()
time_pass = 0
c_d_r_x = [0, 0, 0, 0]

while time_pass <= 10:
    time_pass = time.time() - time_start
    temperature = random.random()
    c_d_r_x[0] = random.random() * 1e-10
    c_d_r_x[1] = random.random() * 0.3
    draw_lib_for_test.draw_figure(time_pass, temperature, c_d_r_x)






