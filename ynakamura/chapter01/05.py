import numpy as np
import matplotlib.pyplot as plt


fs = 16000
sec = 3
t = np.linspace(0., sec, int(fs * sec))

whitenoise = np.random.rand(int(fs * sec)) * 2 - 1

plt.plot(t, whitenoise)
plt.xlim(0, 0.03)
plt.show()