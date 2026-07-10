"""RADIOAVTIVE DECAY TIME CALCULATOR
Calculates the time required for a given number of atoms to decay to a target number of atoms using the half-life formula"""
import numpy as np

def time_required(initial,target, half_life):
    """
    Calculate time needed to reach target amount.
    Formula: t = half_life * log₂(initial/target)
    """
    time = half_life *(np.log2(initial/target))
    return time

initial = 100 # Initial number of atoms
target = 25 # Target number of atoms
half_life = 18 # Half-life of copper-64 in minutes

# Calculate the time required to decay from initial to target atoms
time = time_required(initial, target, half_life)

print(f"time required to decay from {initial} to {target} atoms: {time} minutes")
