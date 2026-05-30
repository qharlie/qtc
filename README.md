# qpc - Quantum Photonic Computer 

![oam](oam__.png)

We can [twist](https://holoeye.com/product/leto-3-vis-009/) our [light](https://hubner-photonics.com/products/lasers/narrow-linewidth-lasers/08-01-series/)  into whole numbers of 'twists per wavelength'. Twisting it to the left we use negative integers ($l=-24$) and to the right we use positive ($l=+24$). Each of these represents a distinct spatial channel where data can be encoded using amplitude (brightness, scaled 1–64). In the picture above you can see $l=4$ on the left and $l=16$ on the right. 


Because each channel is mathematically orthogonal  (e.g., $l=6$ won't interfere with $l=5$), we can stack all of the different twists on top of each other *at the same time*. For this project, we'll be using 48 total channels, spanning from $l=-24$ to $l=+24$.

The quantum piece of QPC is achieved by using entangled photon pairs. In a classical system, two independent light beams would give us 96 channels ($48 + 48$). But by leveraging quantum entanglement, we *hijack the entire joint probability state space* to $48 \times 48 = 2304$ joint channels. 

To illustrate, let's reduce our channels to just 4: $l=-2, -1, +1, +2$. Directly after the moment of creation of our entagled photons inside our [BBO Crystal](https://www.newlightphotonics.com/SPDC-Components/BBO-SPDC-Compensators), the photons are strictly anti-correlated. This means if photon A has two twists to the left, photon B must have two twists to the right. With an even distribution, there is a 100% / 4 states = 25% chance for each correlated state:

(where $l_A$ is the twist count for photon A and $l_B$ is the twist count for photon B)

| PHOTON A (Zone 1) \ PHOTON B (Zone 2) | $l=-2$ | $l=-1$ | $l=+1$ | $l=+2$ | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **$l=-2$** | 0 | 0 | 0 | 0.25 | If $l_A = -2$, $l_B$ must be $+2$ |
| **$l=-1$** | 0 | 0 | 0.25 | 0 | If $l_A = -1$, $l_B$ must be $+1$ |
| **$l=+1$** | 0 | 0.25 | 0 | 0 | If $l_A = +1$, $l_B$ must be $-1$ |
| **$l=+2$** | 0.25 | 0 | 0 | 0 | If $l_A = +2$, $l_B$ must be $-2$ |

After we create the two entagled photons, we alter each wavefronts independently by sending them through a Spatial Light Modulator ([SLM](https://holoeye.com/product/leto-3-vis-009/)). By applying computed phase masks to the SLM, we manipulate the spatial superposition of the photon states. By altering A, we immediately alter all the states of B, and this is how we get our extra dimensionality. This shifts the joint probabilities measured at our detector array to look something like this:

| PHOTON A (Zone 1) \ PHOTON B (Zone 2) | $l=-2$ | $l=-1$ | $l=+1$ | $l=+2$ | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **$l=-2$** | 0.0 | 0.65 | 0.0 | 0.35   | Encoded Data Row 1 |
| **$l=-1$** | 0.60 | 0.10 | 0.15 | 0.15 | Encoded Data Row 2 |
| **$l=+1$** | 0.0 | 0.25 | 0.0 | 0.75 | Encoded Data Row 3 |
| **$l=+2$** | 0.30 | 0.0 | 0.0 | 0.70 | Encoded Data Row 4 |

This is our data we have now encoded in light.  We control these statistical distributions by passing the photons through computer-generated holograms on our SLMs. While the BBO crystal initializes the high-dimensional tensor-product state space ($H_A \otimes H_B$), the SLMs execute localized unitary operations ($U_A \otimes U_B$) in parallel across the entire joint distribution, which we then extract via coincidence counting at the detector array.

![slm_image](mask.png)


## The Computational Advantage

In classical optics, combining and interfering light waves maps directly to linear algebraic transformations. 

By scaling this to a high-dimensional quantum system, passing the entangled photons through engineered SLM phases allows the system to perform complex spatial transformations across all 2,304 joint state values simultaneously. With a high-repetition-rate pump laser and fast coincidence counters, we aim to demonstrate massive parallel processing capabilities approaching GHz-scale effective state transformations.

# Is this real though?

Can we really alter the spatial superposition of two entangled photons to deliberately program their joint probability distributions, recombine them, sort their twists, and read out the resulting matrix transformations?

Join me and we will find out together!

### [Milestone 1](MILESTONE_1.md) <-- currently here
### [Milestone 2](MILESTONE_2.md)

I might also [go another direction](README_QTPC.md) with this.
