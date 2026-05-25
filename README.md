## qtc
Open-Source Quantum Topological Computer you can build at home.

The goal is to stream pairs of entagled electrons, with 48 modifiable properties each ( -4 to +4 OAM and 0 to 5 concentric rings, radial degrees of freedom ) , where we hijack t]he entire state matrix as a manifold and encode our data directly in the relationship of the entagled photons. We use the state probabilities of both entagled photons for a 48x48 matrix or 2034 bit payload, using the amplitude for each as the actual real numbered values.

Much of this works stems directly from [Revealing the topological nature of entangled orbital angular momentum states of light](https://doi.org/10.1038/s41467-025-66066-3)

## The Jist

We aim a single longitudinal mode (SLM) diode pumped solid state (DPSS) laser at our beta barium borate non-linear crystal (BBO) to create lots of pairs of entagled photons. They leave the BBO and enter our Spatial Light Modulator (SLM), guided through the crystal with our 30 AWG micro heated walls where we can tune the path by nanometers.

In our SLM

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
