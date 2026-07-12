import matplotlib.pyplot as plt
import numpy as np


N0=100 #Initial number of atoms
half_life=18 #Half-life of copper-64 in minutes

# Target for 99.9% decay: only 0.1% remains
N=N0*0.001

# Calculate the time required for the decay
t = half_life * (np.log2(N0/N))

# Create 1000 evenly spaced time points from 0 to t_max
time = np.linspace (0, t, 1000)

# Calculate remaining atoms at each time point
amount = N0*np.power(0.5, time/half_life)

plt.plot(time,amount)
plt.xlabel('time(minutes)')
plt.ylabel('remaining atoms')
plt.title(f'Radioactive Decay of Copper-64\nInitial: {N0} atoms, Half-life: {half_life} minutes')
plt.show()

