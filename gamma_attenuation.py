'''GAMMA RAY ATTENUATION COMPARISON
================================
This program compares how well different materials shield gamma radiation.

Formula: I = I₀ * e^(-μx)

Materials:
- Lead:      μ = 0.77 cm⁻¹  (Best shielding)
- Steel:     μ = 0.46 cm⁻¹  (Good shielding)
- Concrete:  μ = 0.15 cm⁻¹  (Moderate shielding)
- Water:     μ = 0.071 cm⁻¹ (Weakest shielding)'''

import matplotlib.pyplot as plt
import numpy as np

I0 = 100 # Initial intensity
x = np.linspace(0,5,100) # Distance in cm
# Attenuation coefficient for lead (Pb) in cm^-1
mu_Pb = 0.77 
# Attenuation coefficient for water (H2O) in cm^-1
mu_H2O = 0.071
# Attenuation coefficient for steel (Fe) in cm^-1
mu_Fe = 0.46
# Attenuation coefficient for concrete (C) in cm^-1
mu_C = 0.15

# Calculate the intensity at each distance using the attenuation formula
I_Pb = I0 *np.exp(-mu_Pb*x)
I_H2O = I0 *np.exp(-mu_H2O*x)
I_Fe = I0 *np.exp(-mu_Fe*x)
I_C = I0 *np.exp(-mu_C*x)

# Plot the results
plt.plot(x,I_Pb,'b', label='Lead')
plt.plot(x,I_H2O,'g', label='Water')
plt.plot(x,I_Fe, 'orange', label='Steel')
plt.plot(x,I_C, 'y', label='Concrete')

plt.xlabel('Distance (cm)')
plt.ylabel("Intensity (I)")
plt.title(f'Attenuation of Radiation in Different Materials\n(1 MeV Gamma Ray)')
plt.legend()
plt.show()

