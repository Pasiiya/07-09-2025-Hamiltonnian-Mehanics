# Hamiltonian Mechanics — Assumption Hunting
**Date:** 2024-09-07  
**Author:** Aashish Kumar

## 1. Short summary
The Hamiltonian formulation uses generalized coordinates \(q\) and conjugate momenta \(p\), and evolves them via Hamilton's equations:
\[
\dot q = \frac{\partial H}{\partial p},\qquad
\dot p = -\frac{\partial H}{\partial q}
\]
For a simple pendulum (length \(l\), mass \(m\)), using \(q=\theta\) and \(p = m l^2 \dot\theta\), one gets:
\[
H(\theta,p) = \frac{p^2}{2 m l^2} - m g l \cos\theta
\]

## 2. Assumption Hunting — list of assumptions
A1. **Holonomic constraints & smooth coordinates.**  
  - The system can be described by a finite set of generalized coordinates and velocity → excludes systems with non-holonomic constraints or path-dependent constraints.

A2. **Invertible Legendre transform (velocities ↔ momenta).**  
  - The mapping \( \dot q \mapsto p=\partial L/\partial \dot q \) must be invertible. Fails for singular Lagrangians (gauge systems, constrained systems).

A3. **Conservative / monogenic forces (for simple H = T + V).**  
  - If non-conservative forces (friction, velocity-dependent dissipation) are present the simple Hamiltonian picture needs modification (dissipative terms, contact Hamiltonian, or extended phase space).

A4. **Smoothness and differentiability of H.**  
  - Requires \(H\) to be sufficiently smooth; singular potentials (hard-wall collisions) can break assumptions used in standard proofs.

A5. **Time parameterization & absolute time.**  
  - Classical Hamiltonian uses a global time parameter t. In relativistic contexts (reparameterization-invariant systems) Hamiltonian formalism must be adapted (Hamiltonian constraint, ADM formalism).

A6. **Determinism & continuum limit.**  
  - Assumes deterministic trajectories; at quantum scales one passes to operators and commutators (quantization), changing the conceptual status of p and q.

A7. **Phase-space volume conservation (Liouville).**  
  - Implies time-reversible microdynamics; fails in coarse-grained descriptions or dissipative effective theories.

## 3. Where the framework breaks down — consequences & frontiers
- **Non-conservative/dissipative systems:** friction cannot be encoded as H = T + V. Workarounds: extended phase space, contact Hamiltonians, Caldeira–Leggett models.
- **Singular Lagrangians → gauge theories:** Legendre transform degenerates; requires Dirac’s constrained Hamiltonian formalism (important in GR and gauge fields).
- **Relativity & gravity:** global Hamiltonian may be absent; in GR energy is not globally conserved in naive sense — leads to Hamiltonian constraints and ADM decomposition.
- **Quantum transition:** Poisson brackets → commutators; the role of phase space variables becomes operator algebra (canonical quantization, path integrals).
- **Statistical mechanics & ergodicity:** Liouville’s theorem underpins microcanonical ensembles; when ergodicity fails, statistical assumptions need checking.
- **Numerical solvers:** naive integrators break symplectic structure; symplectic integrators are required to preserve long-term qualitative features.

## 4. Short "research lead" notes (ideas)
- Explore **dissipative Hamiltonian analogues** — can materials-engineering views of energy loss inform friction models in microphysical systems?
- Investigate **phase-space signatures** of ultra-light dark matter (ULDM): is there a Hamiltonian-level observable in stellar kinematics that is robust to baryonic feedback?

