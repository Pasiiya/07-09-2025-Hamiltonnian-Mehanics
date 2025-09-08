# Hamiltonian Mechanics — Assumption Hunting
**Date:** 07-09-2025  
**Author:** Aashish Kumar

## Quick Recap
- Started from L = T – V (Lagrangian).  
- Switched to Hamiltonian = T + V (for conservative systems).  
- Variables: (q, p) instead of (q, q̇).  
- For the pendulum:
  - q = θ  
  - p = m l² θ̇  
  - H(θ,p) = p² / (2 m l²) – m g l cosθ

## What assumptions are baked in?
1. **We can describe the system with generalized coordinates.**  
   → Works fine for pendulum, fails if constraints are messy/non-holonomic.  

2. **Legendre transform works (velocities ↔ momenta).**  
   → Needs invertibility. Breaks in gauge theories or constrained systems.  

3. **Energy is conservative.**  
   → Hamiltonian = T + V only holds here. With friction/dissipation this is broken.  

4. **Time is absolute.**  
   → Assumes one global time parameter t. Relativity messes with this.  

5. **Smoothness.**  
   → Potentials are nice functions. If you had hard collisions (like a ball hitting a wall), Hamiltonian is trickier.  

6. **Deterministic.**  
   → Dynamics is fully determined once (q,p) are known. Quantum mechanics shatters this picture.  

## Where it cracks
- Friction or damping: can’t write down a nice H.  
- Singular systems / gauge freedom: need Dirac’s fix.  
- In GR: Hamiltonian formalism is possible but not straightforward.  
- Quantum: Hamiltonian survives but interpretation changes (operators).  

## My takeaway
Hamiltonian mechanics is a change of perspective — from thinking in terms of “trajectories in q(t)” to “flows in phase space (q,p).” It feels more geometric.  
The assumptions look simple, but they also explain why Hamiltonians are central in quantum theory and statistical mechanics, while Lagrangians are often nicer for constraints.
