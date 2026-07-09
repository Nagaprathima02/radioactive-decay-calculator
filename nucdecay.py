#  RADIOCATIVE DECAY CALCULATOR
import numpy as np

# Function to calculate the remaining  atoms after a given time using the half-life formula
def calculate_decay (initial, half_life, time):
# Calculate the remaining  atoms after a given time using the half-life formula
    remaining = initial* np.power(0.5, (time / half_life))
# Calculate the remaining atoms after a given time
    return remaining
initial = 100 # Initial number of copper atoms
half_life = 18 # Half-life of copper-64 in minutes
time = 5 # Time in minutes

result = calculate_decay(initial, half_life, time)

print(f"remaining copper atoms after {time} minutes: {result}")