import matplotlib.pyplot as plt
import numpy as np
import itertools

# create a list from 0 to 10 in 0.1 steps
time = np.arange(0, 10, 0.1)

# generate sin/cos values for each time value
x = np.sin(time)
y= np.cos(time)

# plot it
plt.title('Sine vs Cosine')

plt.plot(time, x, label='Sine')
plt.plot(time, y, label='Cosine')

plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.grid()
plt.legend(loc='upper right')
plt.show()
