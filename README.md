# qtpc
Open-Source Quantum Topologically Protected Computer 

With the breakthrough in this paper [Revealing the topological nature of entangled orbital angular momentum states of light](https://doi.org/10.1038/s41467-025-66066-3) , we now only need to alter the phase of the wavefront to create 48 distinct orthogonal channels. These channels are simply the number of phase twists (oribtal angular momentum) per wavelength, and in traditional optics we can stack them all on top of eachother and they won't interfere. The topological protection comes from these whole integer twists ( l=-24 to +24 ) , the light can be slightly distorted but the knot (all the twists stacked on top of one another) is very hard to untie, and 4 twists will never physically interact with 5 twists making them stackable - making the whole setup more stable and suitable for manipulating. 

The Quantum part of our QTPC we achieve by using entagled photons. If they were not entangled, two photons would have 96 slots (48+48) . But with entanglement, _<ins>we hijack the entire probability state matrix</ins>_ for 48x48 or 2304 channels. 

Let's reduce our channels to just 4, *l=-2* to *l=+2* , (meaning physically: two twists to the left through two twists to the right giving us 4 channels for data). Right at the moment of creation, the probability state matrix is  perfectly anti-correlated and looks like this: 

| PHOTON A (Zone 1) \ PHOTON B (Zone 2) | l=-2 | l=-1 | l=+1 | l=+2 | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **l=-2** | 0 | 0 | 0 | 0.5 | If A is -2, B must be +2 |
| **l=-1** | 0 | 0 | 0.5 | 0 | If A is -1, B must be +1 |
| **l=+1** | 0 | 0.5 | 0 | 0 | x |
| **l=+2** | 0.5 | 0 | 0 | 0 | x |

Directly after the entagled photon leaves the BBO crystal we alter it's wavefront with a Spatial Light Modulator (link to holoeye#LATER), where we manipulate <b>*the superposition*</b> of the two photons in such a way that the probabilites of the photons hitting our end sensor array looks like this:

| PHOTON A (Zone 1) \ PHOTON B (Zone 2) | l=-2 | l=-1 | l=+1 | l=+2 | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **l=-2** | 0.0 | 0.15 | 0.0 | 0.35 | Encoded Data Row 1 |
| **l=-1** | 0.10 | 0.0 | 0.40 | 0.0 | Encoded Data Row 2 |
| **l=+1** | 0.0 | 0.25 | 0.0 | 0.0  | Encoded Data Row 3 |
| **l=+2** | 0.0 | 0.0 | 0.0 | 0.70   | Encoded Data Row 4 |

The end-result table is made up over 10k entries of _where the photon arrived on our 2d sensor array_  (link to device) and NI-DAQ board(link to device).  The numbers .40 and .70 above are 4000 and 7000 clicks registered at our 2d sensor array over a 10,000 click period. Those values are what we created by altering the superposition of photons a and b with the SLM by *passing the photons through the generated images below*
![slm_image](mask.png)

## And here come the juice

In traditional optics, you can combine two lightwaves and read the interference and destruction of their waves as a *matrix cross-product*. 

In our quantum computer, *the entire probability state matrix cross multiplies at the speed of light*. We get 48x48=2304 cross-multipled values we can read from our 2d sensor array terminal. With the our prototype spec materials we can get up to 1.3Ghz or 1.3 billiom matrix multiplications per second . An NVIDIA A100 processing 48×48 matrices in FP16 precision can theoretically execute roughly 1.41 billion per second. The QTPC takes barely any electricity and generates no heat , can reduce AI energy requirements by 100x and yes Im making that number up. 

# I need you 

Reach out and let's really make this thing. I'm pushing my limits with this project so don't worry about skill level or expertise everyone is welcome, we need everyone for this wild mid-air light computer made of quantum-magic.

