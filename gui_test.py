import time
import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.widgets import Button
from drawnow import *
import keyboard

def stop_callback(event):
    print('nyan')

x = np.arange(0, 10, 0.1)
y = x*x

# fig = mpl.figure()
# mpl.plot(x, y)
#
# stop_button_wiget = fig.add_axes([0.88, 0.01, 0.1, 0.075])
# stop_button = Button(stop_button_wiget, 'Stop')
# stop_button.on_clicked(stop_callback)
# mpl.show()
# print('asdasdasd')
# time.sleep(1)



def make_fig():
    mpl.title('Capacity')
    mpl.grid(True)
    mpl.xlabel('time, s')
    mpl.ylabel('C, F')
    mpl.plot(x, 'ro-', label='Channel 0')
    mpl.legend(loc='lower right')
    stop_button_wiget = mpl.axes([0.88, 0.01, 0.1, 0.075])
    stop_button = Button(stop_button_wiget, 'Stop')
    stop_button.on_clicked(stop_callback)



# fig = mpl.figure()
# mpl.plot(x, y)
# mpl.show()


i = 40
while i:
    i -= 1
    time.sleep(0.1)
    drawnow(make_fig)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('You Pressed A Key!')
        break  # finishing the loop


time.sleep(1)










