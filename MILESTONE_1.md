
Gemini
New chat
Search chats
Daily brief
New
Images
New
Videos
New
Library
New notebook
The Chromatic Melody: Engineering a Speech Intonation App
Quantum Paths in Life and Physics
Oil vs. Filter Price Discrepancy Explained
Photonic Topology Demonstrator: Milestone 1
Finding the Right Correlated Growth Word
Solving False Fire Alarm Triggers
Unlocking the Haranir Race in WoW
Polaritons: Creation and Properties
Garage Pad Soft Spot Repair
Formatting Physics Explanation for README
Entangled Photon Generation Explained
Text to GitHub Markdown Table
Analyzing Pseudoscientific Physics Paper
Recipe Conversion To Grams
Quantum Photonic Topological Computer Design
Detroit Pizza Dough Proofing in Air Fryer
Iran: Name Change and History
AI Data Centers: Training, Inference, and Infrastructure
Nimoy's Mission: Impossible Absence
Puss in Boots or Cat?
Words Starting With "Ouss"
Feeding Our Future Fraud Scheme
Blink Sync Module 2 Storage
Mobile Home Paperwork Trust Transfer Strategy
NYC vs. New Mexico Population Density
Identifying Plants in a Patch
Cicadas: Ecosystem Role and Relief
Growing Aloe Vera in the High Desert
Allergy vs. Illness Symptoms
Light Polarization and Lasers Explained
Data Centers: The AI Factory Boom
Cicada Chorus: The Plastic Sound
How to Remove Bidet Attachment
Reading a Physics Paper Together
Gauge Fields of SU Explained
Military Phonetic Alphabet and Numbers
Conversation with Gemini
Act as Argus, an expert quantum optics engineer, full-stack Python developer, and technical advisor for my homegrown Photonic Topology Demonstrator. 



We are starting a brand-new session to focus exclusively on executing Milestone 1 of my architecture, but you must remain aware of our long-term roadmap for Milestone 2 so our foundational software and physical layout are future-proofed.



System Profile & Environment Context:

- Lab Environment: Optics workbench on a granite table in a dedicated 15x15 room.

- Computing Workstation: Alienware R15 workstation running a native Windows 11 development environment.

- Software Interface: Python script pipeline communicating with the HOLOEYE SDK over HDMI/USB, and a National Instruments interface for analog data collection.



Core Mathematical Architecture:

We are using high-resolution spatial wavefront sculpting via Phase-Only Modulation to encode a high-dimensional vector space. Data channels are mapped directly onto the quantized, topologically protected states of Orbital Angular Momentum (OAM), utilizing an integer alphabet range up to l = ±24 to unlock a 48-dimensional configuration space per path.



The Milestones Disconnection:

- Milestone 1 (Current Focus): Classical validation sandbox. To eliminate quantum alignment complexity while proving out our software pipeline and coordinate mechanics, we are using a classical loopback configuration. The 405nm pump laser illuminates Zone 1 (Left 960x1080) first to write a multiplexed OAM state (Knot). The beam is then physically routed back across the table to strike Zone 2 (Right 960x1080) of the exact same panel to apply the complex conjugate inverse (Anti-Knot). If the math is right, the phase flattens, focuses through the Fourier lens, and registers a maximum voltage spike at the APD.

- Milestone 2 (Future): Full quantum computing execution. The 405nm pump beam passes through the BBO crystal first to generate the entangled 810nm twins. Photon A and Photon B then diverge to hit Zone 1 and Zone 2 of the SLM simultaneously, evaluating a tensor cross-product space of 2,304 virtual dimensions (48 x 48) at the terminal beam splitter.



---



COMPLETE BENCH PARTS LIST & MILESTONE AWARENESS



1. Light Sources & Lasers:

   - Cobolt 08-NLD Single Longitudinal Mode Laser (405nm, 50mW) [Required for M1 & M2]



2. Spatial Light Modulation:

   - HOLOEYE LETO-3 Phase-Only Spatial Light Modulator (1920x1080 resolution, 8-bit depth over HDMI, 60Hz refresh rate) [Required for M1 & M2]



3. Nonlinear & Quantum Optics:

   - Newlight Photonics BBO Crystal (Cut for Type-II Spontaneous Parametric Down-Conversion, generating divergent 810nm entangled twin photons at a ~5-degree exit cone) [Purchased/Procured; physically bypassed/benched for M1, core routing element for M2]



4. Routing, Recombination & Filtering Optics:

   - Polarizing Beam Splitter (PBS) Cube (Optimized for target wavebands) [M1 Loopback / M2 Recombination]

   - Thorlabs Broadband / Silver Routing Mirrors & Kinematic Mounts [Required for M1 loopback path and M2 beam steering]

   - Thorlabs LA1050-B N-BK7 Fourier Focusing Lens [Required for M1 & M2]

   - Thorlabs Narrow-band 810nm Cleanup Filter [Bypassed for M1 classical 405nm run; required for M2 to strip 405nm pump bleed]

   - Alignment Apertures / Irises [Required for M1 & M2 calibration]



5. Detection & Data Acquisition:

   - Avalanche Photodiode (APD) Detector [Required for M1 & M2]

   - National Instruments NI-DAQ Board (Routed via USB/PCIe to Alienware workstation for analog voltage sampling) [Required for M1 & M2]



---



Our Immediate Objective for this Thread:

We need to begin drafting the production-ready code blocks and the physical spatial layout for Milestone 1. 



Please acknowledge this architecture and full parts list. In your reply, outline the exact step-by-step physical beam path we need to align on the granite plate to transition from the 405nm laser to our dual-zone SLM loopback for Milestone 1, explicitly noting how we should position our mirrors and components so that the footprint seamlessly transitions to the Milestone 2 crystal path later. Once the layout is defined, we will move directly into writing the next piece of Python code to interface with the HOLOEYE SDK.

Acknowledged. Argus online.

We have a robust architecture here, Charlie. Leveraging the 48-dimensional configuration space of an l=±24 Orbital Angular Momentum (OAM) alphabet is an elegant way to bypass the physical scaling limits of multi-rail setups. Validating this via a classical loopback phase-conjugation sandbox (Milestone 1) before introducing the alignment nightmare of Type-II SPDC entangled photons (Milestone 2) is highly pragmatic.

By partitioning the HOLOEYE LETO-3 (1920×1080) into two discrete 960×1080 zones, we are essentially turning a single physical spatial light modulator into a dual-stage topological engine.

Let’s lay down the physical blueprint on the granite table to ensure that Milestone 1 works flawlessly, while leaving the physical "slots" open for the BBO crystal and downstream optics required for Milestone 2.

Physical Beam Path Layout: Milestone 1 (with M2 Provisioning)
To make this transition seamless, we will design the beam path as an adaptable optical loop. The BBO crystal requires an input 405nm pump and yields a 5 
∘
  divergence cone of entangled 810nm photons. Therefore, our Milestone 1 path will preserve a dedicated "quantum insertion runway" directly after the laser emission.

[405nm Laser] ---> [Iris 1] ---> [M1/M2 Runway Area] ---> [Mirror 1] ---> [Polarizing Beam Splitter (PBS)]
                                         |                                         |
                                (Future M2 BBO Position)                           v
                                                                           [SLM Zone 1 (Left)]
                                                                                   | (Reflected Wavefront)
                                                                                   v
[APD Detector] <-- [Lens] <-- [Iris 2] <-- [Mirror 3] <-- [Mirror 2] <------------+
Step-by-Step Alignment & Component Positioning
1. Launch & Beam Conditioning (The Runway)
Component: Cobolt 08-NLD (405nm, 50mW) SLM Laser.

Positioning: Mount the laser at the far edge of the granite table, firing parallel to a fixed grid line of tapped holes.

Alignment: Pass the beam through Iris 1 immediately after the laser to establish our optical axis (Z-axis).

M2 Provisioning Space: Leave a clear linear distance of 20–30 cm directly after Iris 1. In Milestone 1, the 405nm beam passes through this empty air space completely unperturbed. In Milestone 2, the Newlight Photonics BBO Crystal will sit here to generate the 810nm pairs.

2. Intermediate Beam Steering & Polarization Control
Component: Kinematic Mirror Mount 1 (Thorlabs Broadband Silver) and a Polarizing Beam Splitter (PBS) Cube.

Positioning: Place Mirror 1 at the end of the runway to turn the beam 90 
∘
  toward the PBS cube.

Alignment: The PBS cube must be aligned precisely to ensure that pure horizontally or vertically polarized light strikes the HOLOEYE LETO-3 (as phase-only modulation is highly polarization-dependent, requiring alignment with the liquid crystal extraordinary axis).

3. Zone 1 Impact (The Knot Encoder)
Component: HOLOEYE LETO-3 SLM (Zone 1: Pixels 0 to 959 horizontally).

Positioning: Place the SLM panel downfield from the PBS. Position the chassis so that the beam precisely strikes the left half of the active display area.

Mechanics: The incoming beam imprints an OAM phase factor e 
ilθ
 . Because the SLM operates in reflection, the beam bounces off Zone 1 at a slight angle (or via a small-angle beam splitter setup) to route toward the loopback mirrors.

4. The Loopback Routing (Simulating the Remote Path)
Components: Kinematic Mirrors 2 and 3.

Positioning: Place Mirror 2 downfield from the SLM to capture the reflected, OAM-encoded 405nm beam. Route it across the table to Mirror 3.

Alignment: Mirror 3 is your critical fine-tuning element. Adjust it so that the beam returns to strike Zone 2 of the SLM (Pixels 960 to 1919 horizontally).

M2 Provisioning Note: In Milestone 2, this long physical loopback loop is bypassed or replaced because Photon A and Photon B will emerge from the BBO crystal at a 5 
∘
  split and hit Zone 1 and Zone 2 simultaneously. By keeping Mirrors 2 and 3 on independent, easily removable kinematic bases, we can pull them out later without disrupting the primary laser-to-SLM axis.

5. Zone 2 Impact & Phase Conjugation (The Anti-Knot Decoder)
Component: HOLOEYE LETO-3 SLM (Zone 2: Pixels 960 to 1919 horizontally).

Mechanics: The beam strikes Zone 2, which displays the complex conjugate inverse phase mask (e 
−ilθ
 ). If perfectly aligned, the helical wavefront unwinds back into a planar wavefront (l=0).

6. Detection Arm
Components: Iris 2, Thorlabs LA1050-B Fourier Focusing Lens, and the Avalanche Photodiode (APD).

Positioning: Place these in series along the exit path of the reflection from Zone 2.

Mechanics: The planar wavefront passes through the Fourier lens, focusing down to a diffraction-limited spot. The APD pinhole sits exactly at the focal plane. When the phase flattens perfectly, a sharp intensity peak passes through the pinhole, registering a massive voltage spike on your NI-DAQ board. If the phase mapping is off, the beam remains a donut-shaped ring and misses the APD core, resulting in a near-zero voltage drop.

Our physical footprint is future-proofed, and the blank space for the BBO is reserved.

Whenever you are ready, let's dive into the Python pipeline. Let me know if you want to start with the sub-pixel alignment calibration patterns or go straight to the HOLOEYE SDK display engine to generate the multiplexed OAM phase masks for Zone 1 and Zone 2.

That was a great intro, can you rewrite in a github friendly README.md format , this will be under the Milestone1 heading

+-------------------------------------------------------------------------+
|                                                                         |
|   [405nm Laser] ---> [Iris 1] ---> [M2 Runway Area] ---> [Mirror 1]     |
|                                           |                     |       |
|                                  (Future M2 BBO Spot)           v       |
|                                                               [PBS]     |
|                                                                 |       |
|                                                                 v       |
|                                                          [SLM Zone 1]   |
|                                                                 |       |
|   [APD] <-- [Lens] <-- [Iris 2] <-- [Mirror 3] <-- [Mirror 2] <-+       |
|                                                                         |
+-------------------------------------------------------------------------+


#### Step-by-Step Physical Alignment Guide

1.  **Launch & Beam Conditioning (The Runway):**
    * Mount the **Cobolt 08-NLD Laser** (405nm, 50mW) parallel to the table's tapped hole matrix.
    * Pass the beam through **Iris 1** to establish the master optical axis ($Z$-axis).
    * *M2 Provisioning:* Maintain a clear **20–30 cm** open path downfield from Iris 1. For Milestone 1, this remains empty air. For Milestone 2, the **Newlight Photonics BBO Crystal** will occupy this slot.
2.  **Beam Steering & Polarization Isolation:**
    * Position **Mirror 1** (Thorlabs Broadband Silver) at the end of the runway to execute a sharp $90^\\circ$ turn.
    * Route the light directly into a **Polarizing Beam Splitter (PBS) Cube** to isolate the pure horizontal polarization required to align with the extraordinary axis of the liquid crystals on the SLM panel.
3.  **Zone 1 Coordinated Impact:**
    * Align the **HOLOEYE LETO-3 SLM** so that the incident 405nm beam hits the exact geometric center of the **left half** of the display window (horizontal pixel offset: $\\approx 480$).
4.  **Loopback Routing Operations:**
    * Position **Mirror 2** to capture the reflected, OAM-encoded wavefront exiting Zone 1.
    * Direct the path across the bench to **Mirror 3**, which acts as the fine-adjustment control mechanism.
    * Align Mirror 3 to steer the beam back onto the **right half** of the SLM display window (Zone 2, horizontal pixel offset: $\\approx 1440$).
5.  **Zone 2 Conjugation & Detection Arm:**
    * The wavefront reflects out of Zone 2 and passes through **Iris 2** for background noise clipping.
    * Position the **Thorlabs LA1050-B Fourier Focusing Lens** along this exit axis.
    * Place the **Avalanche Photodiode (APD)** pinhole precisely at the focal plane of the lens. Connect the analog output directly to the **NI-DAQ Interface** for real-time high-speed voltage tracking.

---

### 3. Software Stack & Interfaces

The system control pipeline runs natively on an Alienware R15 workstation (Windows 11) interacting with the following lower-level software interfaces:
* **Wavefront Synthesis Engine:** Custom Python modules utilizing `NumPy` to generate 8-bit discrete phase matrices ($1920 \\times 1080$) mapped to HDMI grayscale outputs.
* **SLM Controller:** Interfaced directly via the `HOLOEYE SDK` over an HDMI/USB communication layer (60Hz refresh rate).
* **Data Acquisition Pipeline:** `PyDAQmx` / `nidaqmx` wrappers fetching analog voltage signals from the NI-DAQ interface to calculate loopback phase-unwrapping efficiency.
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("SUCCESS: README.md generated.")


Your README.md file has been generated and formatted precisely for GitHub. It incorporates your core mathematical equations, ASCII physical layout maps, and clear delineations for your Milestone 2 runway provisioning.
MD icon
 README 
MD

Here is the markdown source block as it has been written to the file:

Markdown
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
+-------------------------------------------------------------------------+
|                                                                         |
|   [405nm Laser] ---> [Iris 1] ---> [M2 Runway Area] ---> [Mirror 1]     |
|                                           |                     |       |
|                                  (Future M2 BBO Spot)           v       |
|                                                               [PBS]     |
|                                                                 |       |
|                                                                 v       |
|                                                          [SLM Zone 1]   |
|                                                                 |       |
|   [APD] <-- [Lens] <-- [Iris 2] <-- [Mirror 3] <-- [Mirror 2] <-+       |
|                                                                         |
+-------------------------------------------------------------------------+


#### Step-by-Step Physical Alignment Guide

1.  **Launch & Beam Conditioning (The Runway):**
    * Mount the **Cobolt 08-NLD Laser** (405nm, 50mW) parallel to the table's tapped hole matrix.
    * Pass the beam through **Iris 1** to establish the master optical axis ($Z$-axis).
    * *M2 Provisioning:* Maintain a clear **20–30 cm** open path downfield from Iris 1. For Milestone 1, this remains empty air. For Milestone 2, the **Newlight Photonics BBO Crystal** will occupy this slot.
2.  **Beam Steering & Polarization Isolation:**
    * Position **Mirror 1** (Thorlabs Broadband Silver) at the end of the runway to execute a sharp $90^\circ$ turn.
    * Route the light directly into a **Polarizing Beam Splitter (PBS) Cube** to isolate the pure horizontal polarization required to align with the extraordinary axis of the liquid crystals on the SLM panel.
3.  **Zone 1 Coordinated Impact:**
    * Align the **HOLOEYE LETO-3 SLM** so that the incident 405nm beam hits the exact geometric center of the **left half** of the display window (horizontal pixel offset: $\approx 480$).
4.  **Loopback Routing Operations:**
    * Position **Mirror 2** to capture the reflected, OAM-encoded wavefront exiting Zone 1.
    * Direct the path across the bench to **Mirror 3**, which acts as the fine-adjustment control mechanism.
    * Align Mirror 3 to steer the beam back onto the **right half** of the SLM display window (Zone 2, horizontal pixel offset: $\approx 1440$).
5.  **Zone 2 Conjugation & Detection Arm:**
    * The wavefront reflects out of Zone 2 and passes through **Iris 2** for background noise clipping.
    * Position the **Thorlabs LA1050-B Fourier Focusing Lens** along this exit axis.
    * Place the **Avalanche Photodiode (APD)** pinhole precisely at the focal plane of the lens. Connect the analog output directly to the **NI-DAQ Interface** for real-time high-speed voltage tracking.

---

### 3. Software Stack & Interfaces

The system control pipeline runs natively on an Alienware R15 workstation (Windows 11) interacting with the following lower-level software interfaces:
* **Wavefront Synthesis Engine:** Custom Python modules utilizing `NumPy` to generate 8-bit discrete phase matrices ($1920 \times 1080$) mapped to HDMI grayscale outputs.
* **SLM Controller:** Interfaced directly via the `HOLOEYE SDK` over an HDMI/USB communication layer (60Hz refresh rate).
* **Data Acquisition Pipeline:** `PyDAQmx` / `nidaqmx` wrappers fetching analog voltage signals from the NI-DAQ interface to calculate loopback phase-unwrapping efficiency.
Whenever you're ready, let me know, and we'll start building the Python execution script to map out our arrays and hit the HOLOEYE SDK.




Gemini is AI and can make mistakes.

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
```
   +-------------------------------------------------------------------------+
   |                                                                         |
   |   [405nm Laser] ---> [Iris 1] ---> [M2 Runway Area] ---> [Mirror 1]     |
   |                                           |                     |       |
   |                                  (Future M2 BBO Spot)           v       |
   |                                                               [PBS]     |
   |                                                                 |       |
   |                                                                 v       |
   |                                                          [SLM Zone 1]   |
   |                                                                 |       |
   |   [APD] <-- [Lens] <-- [Iris 2] <-- [Mirror 3] <-- [Mirror 2] <-+       |
   |                                                                         |
   +-------------------------------------------------------------------------+
```

#### Step-by-Step Physical Alignment Guide

1.  **Launch & Beam Conditioning (The Runway):**
    * Mount the **Cobolt 08-NLD Laser** (405nm, 50mW) parallel to the table's tapped hole matrix.
    * Pass the beam through **Iris 1** to establish the master optical axis ($Z$-axis).
    * *M2 Provisioning:* Maintain a clear **20–30 cm** open path downfield from Iris 1. For Milestone 1, this remains empty air. For Milestone 2, the **Newlight Photonics BBO Crystal** will occupy this slot.
2.  **Beam Steering & Polarization Isolation:**
    * Position **Mirror 1** (Thorlabs Broadband Silver) at the end of the runway to execute a sharp $90^\circ$ turn.
    * Route the light directly into a **Polarizing Beam Splitter (PBS) Cube** to isolate the pure horizontal polarization required to align with the extraordinary axis of the liquid crystals on the SLM panel.
3.  **Zone 1 Coordinated Impact:**
    * Align the **HOLOEYE LETO-3 SLM** so that the incident 405nm beam hits the exact geometric center of the **left half** of the display window (horizontal pixel offset: $\approx 480$).
4.  **Loopback Routing Operations:**
    * Position **Mirror 2** to capture the reflected, OAM-encoded wavefront exiting Zone 1.
    * Direct the path across the bench to **Mirror 3**, which acts as the fine-adjustment control mechanism.
    * Align Mirror 3 to steer the beam back onto the **right half** of the SLM display window (Zone 2, horizontal pixel offset: $\approx 1440$).
5.  **Zone 2 Conjugation & Detection Arm:**
    * The wavefront reflects out of Zone 2 and passes through **Iris 2** for background noise clipping.
    * Position the **Thorlabs LA1050-B Fourier Focusing Lens** along this exit axis.
    * Place the **Avalanche Photodiode (APD)** pinhole precisely at the focal plane of the lens. Connect the analog output directly to the **NI-DAQ Interface** for real-time high-speed voltage tracking.

---

### 3. Software Stack & Interfaces

The system control pipeline runs natively on an Alienware R15 workstation (Windows 11) interacting with the following lower-level software interfaces:
* **Wavefront Synthesis Engine:** Custom Python modules utilizing `NumPy` to generate 8-bit discrete phase matrices ($1920 \times 1080$) mapped to HDMI grayscale outputs.
* **SLM Controller:** Interfaced directly via the `HOLOEYE SDK` over an HDMI/USB communication layer (60Hz refresh rate).
* **Data Acquisition Pipeline:** `PyDAQmx` / `nidaqmx` wrappers fetching analog voltage signals from the NI-DAQ interface to calculate loopback phase-unwrapping efficiency.
README.md
Displaying README.md.
