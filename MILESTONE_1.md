# Photonic Topology Demonstrator

Welcome to the core documentation repository for the Homegrown Photonic Topology Demonstrator. This project implements high-resolution spatial wavefront sculpting via Phase-Only Modulation to encode high-dimensional vector spaces onto the quantized, topologically protected states of Orbital Angular Momentum (OAM). 

By utilizing an integer alphabet range up to $l = \pm24$, we unlock a 48-dimensional configuration space per optical path.

---

## Milestone 1: Classical Validation Sandbox

The primary objective of Milestone 1 is to implement a classical validation loopback configuration. This architecture eliminates quantum alignment complexities (such as photon pair entanglement and coincidence counting) while fully proving out our software control pipeline, spatial light modulator (SLM) coordinate mechanics, and phase-unwrapping algorithms.

### 1. Conceptual Mechanics & Loopback Architecture

Milestone 1 partitions a single **HOLOEYE LETO-3** Phase-Only SLM ($1920 \times 1080$ resolution) into two independent, software-controlled logic zones:

* **Zone 1 (Left Half - Pixels 0 to 959):** Acts as the **Knot Encoder**. It modulates the incoming 405nm single longitudinal mode laser beam, imprinting a multiplexed OAM state:
    $$\psi_{\text{encoded}}(\theta) = e^{i l \theta}$$
* **Zone 2 (Right Half - Pixels 960 to 1919):** Acts as the **Anti-Knot Decoder**. After the beam is physically routed across the optics workbench via a loopback mirror configuration, it strikes Zone 2, which applies the complex conjugate inverse phase mask:
    $$\psi_{\text{decoded}}(\theta) = e^{-i l \theta}$$

$$\Psi_{\text{terminal}}(\theta) = \psi_{\text{encoded}}(\theta) \cdot \psi_{\text{decoded}}(\theta) = e^{i l \theta} \cdot e^{-i l \theta} = e^{0} = 1$$

When the physical alignment and mathematical phase maps correspond exactly, the helical wavefront unwinds back into a flat, planar wavefront ($l = 0$). This flat wavefront passes through a Fourier focusing lens, collapsing into a diffraction-limited spot at the focal plane, triggering a maximum voltage spike on our Avalanche Photodiode (APD) monitored via an NI-DAQ interface.

---

### 2. Physical Beam Path & Hardware Configuration

The physical footprint on the granite optical workbench has been precisely engineered to remain **future-proof**. A dedicated "Quantum Insertion Runway" is provisioned immediately after the laser launch to ensure a seamless transition to Milestone 2 (Type-II Spontaneous Parametric Down-Conversion) without rebuilding the core layout.

#### Optical Bench Component Layout
