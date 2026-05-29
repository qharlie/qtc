# qtpc - Open-Source Quantum Topologically Protected Computer 
With our [Spatial Light Modulator](https://holoeye.com/product/leto-3-vis-009/) we can alter the phase of our [light](https://hubner-photonics.com/products/lasers/narrow-linewidth-lasers/08-01-series/) to twist it into whole numbers of twist per wavelength (from now on just $\lambda$) . Twisting it to the left we go negative and to the right we go positive (0 is our baseline).

Our topological protection stems from these whole integer twists ( l=-24 to +24 ). Our light can be slightly distorted (by dust etc) but the knot ( these twists stacked on top of one another all at the same time) is very hard to untie and each channel is distinct aka orthogonal ( 6 twists per $\lambda$  will never interfere with 5 twists per $\lambda$ keeping our channels clean ). For this project we'll be using 48 total channels, -24 to +24.

The Quantum part of our QTPC we achieve by using entagled photons. If they were not entangled, our two photons would have 96 channels (48+48) . But with entanglement, _<ins>we hijack the entire probability state matrix</ins>_ for 48x48 or 2304 channels. 

To illustrate what we're doing let's reduce our channels to just 4, *l=-2* to *l=+2* , (meaning physically: two twists to the left through two twists to the right giving us 4 channels for data). Right at the moment of creation, the probability state matrix is perfectly anti-correlated , meaning if photon A has two twists two the left, then photon B will have two twists to the right, and theres a 100/4=25% chance for each of our states, and looks like this: 

( _Al_ is the twist count for photon A )
| PHOTON A (Zone 1) \ PHOTON B (Zone 2) | l=-2 | l=-1 | l=+1 | l=+2 | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **l=-2** | 0 | 0 | 0 | 0.25 | If _Al_ is -2, _Bl_ must be +2 |
| **l=-1** | 0 | 0 | 0.25 | 0 | If _Al_ is -1, _Bl_ must be +1 |
| **l=+1** | 0 | 0.25 | 0 | 0 | If _Al_ is +1, _Bl_ must be -1 |
| **l=+2** | 0.25 | 0 | 0 | 0 | If _Al_ is +2, _Bl_ must be -2 |

Directly after the entagled photon leaves the [BBO crystal](https://www.newlightphotonics.com/SPDC-Components/BBO-SPDC-Compensators) we alter it's wavefront with our [SLM](https://holoeye.com/product/leto-3-vis-009/), where we manipulate <b>*the superposition*</b> of the two photons in such a way that the probabilites of the photons hitting our end sensor array looks like this:

| PHOTON A (Zone 1) \ PHOTON B (Zone 2) | l=-2 | l=-1 | l=+1 | l=+2 | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **l=-2** | 0.0 | 0.65 | 0.0 | 0.35 | Encoded Data Row 1 |
| **l=-1** | 0.60 | 0.0 | 0.40 | 0.0 | Encoded Data Row 2 |
| **l=+1** | 0.0 | 0.25 | 0.0 | 0.75 | Encoded Data Row 3 |
| **l=+2** | 0.30 | 0.0 | 0.0 | 0.70 | Encoded Data Row 4 |

The end-result table is made up over 10k clicks per row of _where the photon arrived on our [sensors](https://www.thorlabs.com/free-space-si-avalanche-photodetectors)_.  The numbers .65 and .35 above are 6500 and 3500 clicks registered over a 10,000 click period per row. Those clicks are what we created by altering the superposition of photons A and B with our SLM by passing the photons through masks we create, like the ones below

![slm_image](mask.png)

## And here come the juice

In traditional optics, you can combine two lightwaves and read the interference and destruction of their waves as a *tensor product*. 

In our quantum computer, *the entire probability state matrix cross multiplies at the speed of light*. We get 48x48=2304 cross-multipled values we can read from our 2d sensor array terminal. With the our prototype spec materials we can get up to 1.3Ghz or 1.3 billiom matrix multiplications per second. 

# Is this real though ?

Can we really [alter](https://holoeye.com/product/leto-3-vis-009/) the super position of two [entagled photons](https://www.newlightphotonics.com/SPDC-Components/BBO-SPDC-Compensators) to slyly shove data into where they are statistically likely to appear, and finally [combine them](https://www.thorlabs.com/non-polarizing-cube-beamsplitters-700---1100-nm?aID=13c106582ed9606ef3f9ea11e60cd787&aC=1&aE=1&aN=1&tabName=Overview) back in mid air and [unroll the waves](https://www.thorlabs.com/n-bk7-plano-convex-lenses-ar-coating-650---1050-nm) and [read our matrix multiplication results](https://www.thorlabs.com/free-space-si-avalanche-photodetectors) ?

# Join me and we will find out together!
### [Milestone 1](MILESTONE_1.md) <-- currently here
### [Milestone 2](MILESTONE_2.md)

