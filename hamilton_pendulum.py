"""
Simple symplectic (leapfrog) integrator for a pendulum in Hamiltonian form.
Variables: theta (angle), p (conjugate momentum = m*l^2 * theta_dot)
"""

import numpy as np
import matplotlib.pyplot as plt

# parameters
m = 1.0    # kg
l = 1.0    # m
g = 9.8    # m/s^2

# Hamiltonian derivatives:
# dtheta/dt = p / (m l^2)
# dp/dt = - m g l sin(theta)

def leapfrog(theta0, p0, dt, steps):
    theta = np.zeros(steps)
    p = np.zeros(steps)
    theta[0] = theta0
    p[0] = p0

    # half-step for p
    p_half = p0 + 0.5 * dt * (-m * g * l * np.sin(theta0))

    for i in range(1, steps):
        theta[i] = theta[i-1] + dt * (p_half / (m * l**2))
        p_half = p_half + dt * (-m * g * l * np.sin(theta[i]))
        p[i] = p_half - 0.5 * dt * (-m * g * l * np.sin(theta[i]))  # full-step p

    return theta, p

if __name__ == "__main__":
    # initial conditions
    theta0 = 0.5  # rad (~28.6 degrees)
    p0 = 0.0
    dt = 0.005
    T = 20.0
    steps = int(T / dt)

    theta, p = leapfrog(theta0, p0, dt, steps)
    t = np.linspace(0, T, steps)

    # energy over time for monitoring
    H = p**2 / (2 * m * l**2) - m * g * l * np.cos(theta)

    # plots
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.plot(t, theta)
    plt.xlabel("t (s)")
    plt.ylabel("theta (rad)")
    plt.title("Theta vs time")

    plt.subplot(1,2,2)
    plt.plot(theta, p)
    plt.xlabel("theta (rad)")
    plt.ylabel("p")
    plt.title("Phase space (theta, p)")

    plt.tight_layout()
    plt.savefig("hamilton_pendulum.png", dpi=200)
    plt.show()