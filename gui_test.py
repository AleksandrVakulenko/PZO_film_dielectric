import numpy as np
import matplotlib.pyplot as mpl
from matplotlib.widgets import Button

def stop_callback(event):
    print('nyan')


fig = mpl.figure()
x = np.arange(0, 10, 0.1)
y = x*x
mpl.plot(x, y)

stop_button_wiget = fig.add_axes([0.88, 0.01, 0.1, 0.075])
stop_button = Button(stop_button_wiget, 'Stop')
stop_button.on_clicked(stop_callback)
mpl.show()








