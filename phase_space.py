# phase_space.py
# Visualizes the Phase Space of a Simple Harmonic Oscillator
# Phase space is a key concept in Hamiltonian mechanics.

import numpy as np
import matplotlib.pyplot as plt

# Define the Hamiltonian: H = (p^2)/2 + (q^2)/2  (for mass m=1 and spring constant k=1)
def Hamiltonian(p, q):
    return (p**2 + q**2) / 2

# Create a grid of points in phase space
q = np.linspace(-2.5, 2.5, 30)  # position
p = np.linspace(-2.5, 2.5, 30)  # momentum
Q, P = np.meshgrid(q, p)

# Calculate the Hamiltonian H at each point
H = Hamiltonian(P, Q)

# Plot the phase portrait (contours of constant energy)
plt.figure(figsize=(8, 6))
plt.contour(Q, P, H, levels=15, colors='blue', linestyles='solid')
plt.title('Phase Space of a Simple Harmonic Oscillator')
plt.xlabel('Position (q)')
plt.ylabel('Momentum (p)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.savefig('phase_space.png')  # Save the plot
plt.show()

print("Phase space plot generated! Check 'phase_space.png'.")