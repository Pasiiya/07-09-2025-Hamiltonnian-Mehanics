# damped_pendulum_phase_space.py
# Visualizes the Phase Space of a Damped, Driven Nonlinear Pendulum
# This system can exhibit chaos, making its phase space complex and fascinating.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the parameters for a chaotic case
g = 9.8   # gravity (m/s^2)
L = 1.0   # length of pendulum (m)
omega_d = 2.0 # driving frequency (rad/s)
F_d = 1.2 # driving force amplitude
q = 0.5   # damping coefficient

# Definition of the ODEs for the damped, driven pendulum
# We use: d^2θ/dt^2 + (q)*dθ/dt + (g/L)*sin(θ) = F_d * cos(omega_d * t)
# We break this into two first-order ODEs:
# dθ/dt = ω
# dω/dt = -q*ω - (g/L)*sin(θ) + F_d * cos(omega_d * t)
def damped_pendulum_ode(t, state):
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -q * omega - (g/L) * np.sin(theta) + F_d * np.cos(omega_d * t)
    return [dtheta_dt, domega_dt]

# Simulation time: Integrate for a long time to see the attractor
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Initial condition: start from rest at a large angle
initial_state = [np.pi/2, 0]  # [theta, omega]

# Solve the ODE
sol = solve_ivp(damped_pendulum_ode, t_span, initial_state, t_eval=t_eval, method='RK45', rtol=1e-8)

# Extract the solution
theta = sol.y[0]
omega = sol.y[1]

# Plot the Phase Portrait
plt.figure(figsize=(10, 6))
plt.plot(theta, omega, ',', color='blue', alpha=0.5, markersize=0.1)
plt.title('Phase Space of a Damped, Driven Nonlinear Pendulum (Chaotic Regime)')
plt.xlabel('Angular Position, θ (radians)')
plt.ylabel('Angular Velocity, ω (radians/s)')
plt.xlim(-np.pi, np.pi)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Save the plot
plt.savefig('damped_pendulum_phase_space.png', dpi=300, bbox_inches='tight')
plt.show()

print("Chaotic phase space plot generated! Check 'damped_pendulum_phase_space.png'.")