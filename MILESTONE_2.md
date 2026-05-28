## Milestone 2: Full Quantum Execution

The primary objective of Milestone 2 is to transition our classical sandbox into a true high-dimensional quantum computing architecture. By introducing spontaneous parametric down-conversion (SPDC), we replace the classical sequential loopback path with a simultaneous, non-local evaluation of an entangled twin-photon state space.

### 1. Quantum Mechanics & Tensor Cross-Product Space

In Milestone 2, the **Cobolt 08-NLD** 405nm laser transforms from a classical signal carrier into a high-coherence quantum pump. 

1. **Entanglement Generation:** The 405nm pump beam drives the **Newlight Photonics BBO Crystal** (Type-II SPDC). A single pump photon splits into a pair of orthogonally polarized, entangled twin photons (Photon A and Photon B) at an $810\text{ nm}$ wavelength, emerging along a $5^\circ$ divergence cone.
2. **The Space:** Because each photon independently occupies an Orbital Angular Momentum (OAM) state space spanning $l = -24$ to $l = +24$, the two-photon system evaluates a vast **tensor product Hilbert space**:
   $$\dim(\mathcal{H}_A \otimes \mathcal{H}_B) = 48 \times 48 = 2,304 \text{ Virtual Dimensions}$$
3. **Simultaneous Processing (The Coincidence Engine):** * **Zone 1 (Left Half):** Programmed to intercept Photon A, applying a high-dimensional spatial transformation matrix $\hat{U}_A$.
   * **Zone 2 (Right Half):** Programmed to intercept Photon B simultaneously, applying transformation matrix $\hat{U}_B$.

$$\lvert \Psi_{\text{out}} \rangle = (\hat{U}_A \otimes \hat{U}_B) \lvert \Psi_{\text{SPDC}} \rangle$$

The high-dimensional topological knot structures are no longer written into physical wavefront shapes of a single beam; they are embedded entirely within the non-local, spatial probability correlation matrix of the twins.

---

### 2. Physical Beam Path & Quantum Hardware Insertion

To execute Milestone 2, the kinematic loopback mirrors (Mirrors 2 and 3) from Milestone 1 are removed from the workbench. The previously provisioned "Quantum Insertion Runway" is populated, creating an un-intersected, parallel dual-rail processing topology.

#### Optical Bench Component Layout (Milestone 2 Quantum Mode)
+-------------------------------------------------------------------------+
|                                                                         |
|   [405nm Laser] ---> [Iris 1] ---> [ BBO Crystal ]                      |
|                                           |                             |
|                                           +--> (Photon A: V-Pol) --+    |
|                                           |                        |    |
|                                           +--> (Photon B: H-Pol) -+|    |
|                                                                   v|    |
|                                                          [M1 Mirror 1 Mode]
|                                                                   ||    |
|                                                                   vv    |
|                                                            [ PBS Cube ] |
|                                                             |        |  |
|                                                             v        v  |
|                                                      [SLM Z1]   [SLM Z2]|
|                                                         |        |      |
|   [Coincidence Logic] <-- [Dual APDs] <-- [810nm Filter] <-- [BS Cube]  |
|                                                                         |
+-------------------------------------------------------------------------+
#### Step-by-Step Quantum Realignment Protocol

1. **Populating the Runway:**
   * Mount the **Newlight Photonics BBO Crystal** precisely in the designated 20–30 cm clearing downstream from Iris 1.
   * Fine-tune the crystal's phase-matching angles to stabilize the Type-II spontaneous emission cone.
2. **Polarization Separation & Dual-Zone Injection:**
   * Photon A (Vertical Polarization) and Photon B (Horizontal Polarization) diverge naturally along the $5^\circ$ window.
   * Pass both paths through the **Polarizing Beam Splitter (PBS) Cube** to perfectly decouple the spatial tracks, sending Photon A directly to the geometric center of **Zone 1** (Pixels 0-959) and Photon B directly to the center of **Zone 2** (Pixels 960-1919) on the SLM panel simultaneously.
3. **Recombination & Terminal Filtering:**
   * Guide both reflected, phase-modulated outputs from Zone 1 and Zone 2 to converge at a terminal, symmetric **Non-Polarizing Beam Splitter (BS) Cube**.
   * Insert the **Thorlabs 810nm Narrow-band Cleanup Filter** immediately after the recombination stage to strip away any residual 405nm pump laser bleed-through, ensuring absolute state purity.
4. **Coincidence Detection Arm:**
   * Focus the terminal output modes into a dual-channel fiber-coupled **Avalanche Photodiode (APD)** array.
   * Route the output pulse streams into the **NI-DAQ interface** configured for high-speed, sub-nanosecond coincidence window counting to verify topological reconstruction metrics across the 2,304-dimensional space.

---

### 3. Quantum Software Extensions

Transitioning our Python control pipeline to support Milestone 2 introduces several low-latency architecture requirements:
* **Tensor Matrix Operators:** Upgrading the `NumPy` wavefront engine to compute high-dimensional Kronecker products (`np.kron`) to map simultaneous dual-zone SLM masks.
* **Coincidence Stream Processor:** Expanding the `nidaqmx` data capture loops into a multi-threaded asynchronous polling script capable of calculating real-time correlations, normalizing cross-talk matrices across the $\pm24$ OAM alphabet, and rendering the 48-dimensional Bloch textures.
