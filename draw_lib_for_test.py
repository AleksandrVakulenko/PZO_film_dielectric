import matplotlib.pyplot as plot
from drawnow import drawnow
import time

__plot_cap = [0]
__plot_tanD = [0]
__plot_temp = [0]
__plot_time = [0]


def draw_figure(time_now, temperature, c_d_r_x):
    __update_arrays(time_now, temperature, c_d_r_x)
    drawnow(__make_fig)


def __make_fig():
    plot.subplot(221)
    plot.grid(True)
    plot.xlabel('T, C°')
    plot.ylabel('C, nF')
    plot.plot(__plot_temp, __plot_cap, 'ro-')

    plot.subplot(222)
    plot.grid(True)
    plot.xlabel('T, C°')
    plot.ylabel('D, 1')
    plot.plot(__plot_temp, __plot_tanD, 'ro-')

    plot.subplot(223)
    plot.grid(True)
    plot.xlabel('time, s')
    plot.ylabel('T, C°')
    plot.plot(__plot_time, __plot_temp, 'ro-')


def __update_arrays(time_now, temperature, c_d_r_x):
    __plot_time.append(time_now)
    __plot_cap.append(c_d_r_x[0])
    __plot_tanD.append(c_d_r_x[1])
    if __plot_temp[len(__plot_temp) - 1] > 15:
        __plot_temp.append(__plot_temp[len(__plot_temp) - 1] - temperature)
    else:
        __plot_temp.append(__plot_temp[len(__plot_temp) - 1] + temperature)










