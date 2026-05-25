## qtc
Open-Source Quantum Topological Computer you can build at home.

The goal is to stream pairs of entagled electrons, with 48 modifiable properties each ( -4 to +4 orbital angular momentum (OAM) and 0 to 5 concentric rings, radial degrees of freedom ) , where we hijack t]he entire state matrix as a manifold and encode our data directly in the relationship of the entagled photons. We use the state probabilities of both entagled photons for a 48x48 matrix or 2034 sized payload, using the amplitude for each as the actual real numbered values.

Much of this works stems directly from [Revealing the topological nature of entangled orbital angular momentum states of light](https://doi.org/10.1038/s41467-025-66066-3)

## The Workflow

We aim a single longitudinal mode diode-pumped solid-state (SLM DPSS) long-coherence laser at our beta barium borate (BBO) non-linear crystal. Through a process called Spontaneous Parametric Down-Conversion (SPDC), the crystal occasionally (1 in 1billion) splits a single high-energy photon into a pair of lower-energy 'daughter' photons. Because this decay must strictly obey the laws of conservation of energy and momentum, the resulting photon pairs are intrinsically entangled in their polarization, momentum, and times of creation ( [Go to Entanglement Section](###how_we_create_entaglement)  ). They leave the BBO and enter our Spatial Light Modulator (SLM), guided through the crystal with our 30 AWG micro heated wires where we can tune the path by nanometers by slightly altering the temperature of the crystal. 

We have two SLM's, one for photon A and one for photon B. Our SLM's are what alter the wavefront's PHASE ( by delaying it ) and OAM

### Milestone 1


### Parts List

| Component Description | Suggested Supplier | Part Number Example | Qty | Engineering Notes |
| :--- | :--- | :--- | :--- | :--- |
| 50:50 Non-Polarizing Beam Splitter Cube (1" / 25.4mm Coated for 532nm) | Thorlabs | BS013 | 1 | Heart of the core. Must be non-polarizing and AR-coated for 350-650nm to handle green laser. |
| Right-Angle Prism (Fused Silica 1" / 25.4mm) | Thorlabs | PS992-A | 2 | Used to build the hard 90-degree internal turns to and from the SLM screen. |
| Index Matching Gel (G608N3) | Thorlabs | G608N3 | 1 | Acts as liquid cement between the BS cube and prisms. Eliminates internal reflection loss. |
| Micro-Heater Resistance Wire (30 AWG Polyimide Coated) | McMaster-Carr | 8860K11 | 1 | Wrapped around the glass block for precision thermal path-length tuning (thermal flywheel). |
| High Thermal Conductivity Epoxy (Aluminum-Filled) | McMaster-Carr | 7457A1 | 1 | Secures the micro-heater wire and external PID thermistor tightly to the glass block face. |
| 532nm Green DPSS Laser (>10mW Single Longitudinal Mode) | HÜBNER Photonics / Cobolt | Cobolt 04-01 Series | 1 | CRITICAL: Must be single longitudinal mode for long coherence length. Cheap lasers blur the masks. |
| Kinematic Laser Diode Mount (Cage System Compatible) | Thorlabs | C4W | 1 | Provides micro tip/tilt alignment to inject the raw beam cleanly into the optics line. |
| Spatial Light Modulator (SLM) Phase-Only Reflective LCoS | Thorlabs OR HOLOEYE | Exulus-SE / LETO-3 | 1 | The core program engine. Requires 8-bit raw bitmap or NumPy array access via SDK for carrier gratings. |
| Si Avalanche Photodiode (APD) Cooled Analog Detector | Thorlabs | APD430A(/M) | 1 | Our unit test monitor. Measures the intensity spike when the anti-knot unrolls the beam profile. |
| Fourier Lens (Aspheric Singlet f=100mm Coated) | Thorlabs | LA1050-A | 1 | Focuses the unwound plane wave exiting the SLM decoder zone down into a sharp point for the APD. |
| Variable Aperture / Iris Diaphragm | Thorlabs | SM1D12 | 1 | Placed directly before the APD to physically slice away light scattered by the carrier gratings. |
| Machinist's Granite Surface Plate (18" x 24" x 4") | Starrett | Starrett 81803 | 1 | Laboratory Grade AA plate. Floated on dry sand inside a heavy tub to deaden earth vibrations. |
| Rigid Polyisocyanurate Insulation Panels (1" Foil-Lined) | Home Depot / Lowe's | Generic R-Max / AP | 3 | To build the primary thermal shield enclosure. Target stability inside is 71.6°F (22°C) +/-0.1°C. |
| Entanglement Upgrades,Beta Barium Borate (BBO) Crystal Type-II SPDC (Cut for 532nm -> 1064nm) | Thorlabs OR Newlight Photonics | BBO5050-P (Custom Cut) | 1 |CRITICAL FOR MILESTONE 2. Splitting a high-coherence pump photon into a 3D spatially entangled twin pair |


## Details And References 

### how_we_create_entaglement

The process occurs in three progressive layers: the **asymmetry of the lattice**, the **polarization wave** it creates, and the **quantum split**.

---

### 1. The Lattice Asymmetry (Non-Linearity)

In a standard material (like window glass), the electrons bound to atoms behave like linear springs. When light passes through, its electric field pushes the electrons back and forth, and they oscillate proportionally to the light's intensity.

**BBO (Beta Barium Borate) is different.** Its crystal lattice is *non-centrosymmetric*—meaning it lacks inversion symmetry. The electrons are bound in asymmetric potential wells (akin to a spring that is much harder to compress than it is to stretch).

When you hit this asymmetric lattice with the intense, concentrated electric field of your Single Longitudinal Mode (SLM) DPSS pump laser, the electrons are driven way past their linear comfort zone, causing them to oscillate anharmonically.

---

### 2. The Nonlinear Polarization Wave

Because the electrons are moving anharmonically within the lattice, they don't just re-radiate the original laser frequency. The collective response of the lattice creates a nonlinear macroscopic polarization wave in the medium.

Mathematically, the polarization $P(t)$ of the crystal is expanded as a power series of the electric field $E(t)$:

$$P(t) = \varepsilon_0 \left( \chi^{(1)}E(t) + \chi^{(2)}E^2(t) + \chi^{(3)}E^3(t) + \dots \right)$$

* **$\chi^{(1)}$** is the standard linear susceptibility (responsible for normal refraction).
* **$\chi^{(2)}$** is the second-order nonlinear susceptibility, which is exceptionally strong in BBO due to its asymmetric lattice.

The $E^2(t)$ term means that if you have a pump photon wave traveling through the lattice, the crystal's electrons mix the fields. This non-linear mixing is the exact mechanism that allows a single high-energy quantum wave packet to couple into two lower-energy wave packets.

---

### 3. The Quantum Birth of the Pairs

At the quantum level, this field-lattice coupling manifests as **Spontaneous Parametric Down-Conversion (SPDC)**.

> 💡 **Phase Matching**
> For the pump photon to effectively drive the lattice into creating two new photons, the individual waves must stay in phase as they travel through the crystal. Because BBO is birefringent, we can precisely tilt the crystal lattice relative to the laser beam so that the refractive index matches perfectly for both the incoming pump photon and the outgoing entangled pairs.

> 🧲 **The Lattice Momentum Kick**
> As the pump photon propagates through the periodic potential of the BBO lattice, the virtual state created by the non-linear interaction collapses. The lattice itself doesn't absorb energy, but it acts as the anchor that enforces the phase-matching condition, ensuring that the total momentum ($\vec{k}$) and energy ($\omega$) are perfectly split between the two emerging photons:

$$\omega_{\text{pump}} = \omega_{\text{signal}} + \omega_{\text{idler}}$$

$$\vec{k}_{\text{pump}} = \vec{k}_{\text{signal}} + \vec{k}_{\text{idler}}$$

Because the emission is constrained by these strict geometrical lines dictated by the lattice orientation, Type-II SPDC in BBO causes the photons to emerge along two overlapping cones.

The **entanglement** occurs precisely at the two intersection points of these cones. If a photon is found in one intersection, its twin is guaranteed to be in the other. Until a measurement occurs, their polarizations remain in a simultaneous, indeterminate superposition of both possibilities.
