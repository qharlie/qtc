import numpy as np
import matplotlib.pyplot as plt

def generate_spatial_wavefront(width, height, channel_vector):
    """
    Takes an arbitrary 48-dimensional vector and synthesizes its 
    physical continuous complex spatial light field using OAM modes.
    """
    x = np.linspace(-width / 2, width / 2, width)
    y = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x, y)
    THETA = np.arctan2(Y, X)
    
    # Initialize our complex wave canvas
    complex_field = np.zeros((height, width), dtype=np.complex128)
    
    # Map the vector elements to their topologically protected lanes
    for l, amplitude in channel_vector.items():
        # Physical field equation: E = A * e^(i * l * theta)
        complex_field += amplitude * np.exp(1j * l * THETA)
        
    return complex_field

def field_to_slm_mask(complex_field):
    """
    Extracts the geometric phase boundaries from a complex field 
    and normalizes it into a raw 8-bit grayscale mask for the HOLOEYE SDK.
    """
    phase = np.angle(complex_field)
    phase_wrapped = np.mod(phase, 2 * np.pi)
    return (phase_wrapped * (255.0 / (2 * np.pi))).astype(np.uint8)

if __name__ == "__main__":
    # Resolution parameters matching one-half of your HOLOEYE LETO-3 panel
    w, h = 960, 1080
    
    print("=========================================================")
    print("INITIALIZING MULTI-CHANNEL QUANTUM COMPUTATION SIMULATION")
    print("=========================================================\n")
    
    # -----------------------------------------------------------------
    # STEP 1: THE INPUT SIGNAL (Zone 1 - Photon A)
    # A non-trivial 48-dimensional data vector containing low-frequency
    # background noise mixed with distinct high-frequency information features.
    # -----------------------------------------------------------------
    input_vector_A = {
        1:  0.85,  # Baseline noise channel
        -2: 0.60,  # Secondary drift channel
        12: 0.40,  # Mid-tier feature lane
        -18: 0.75, # High-frequency feature alpha
        24: 0.95   # High-frequency feature beta (Target Edge)
    }
    
    print("1. Sculpting Photon A's wavefront with input data matrix...")
    field_A = generate_spatial_wavefront(w, h, input_vector_A)
    mask_A = field_to_slm_mask(field_A)
    
    # -----------------------------------------------------------------
    # STEP 2: THE CONVOLUTION KERNEL DECODER (Zone 2 - Photon B)
    # Because of the quantum conservation of angular momentum (l_A + l_B = 0),
    # our decoder matrix uses the negative conjugate lanes. 
    # We configure this kernel to block the noise (l=1,-2 receive 0.0 weight)
    # and isolate/multiply the high-frequency features.
    # -----------------------------------------------------------------
    kernel_vector_B = {
        -12: 0.50, # Scale mid-tier feature
        18:  1.00, # Maximize feature alpha
        -24: 1.00  # Maximize feature beta
    }
    
    print("2. Synthesizing entangled conjugate convolution kernel for Photon B...")
    field_B = generate_spatial_wavefront(w, h, kernel_vector_B)
    mask_B = field_to_slm_mask(field_B)
    
    # -----------------------------------------------------------------
    # STEP 3: PHYSICAL INTERFERENCE & BEAM RECOMBINATION
    # The two photons overlay inside the polarizing beam splitter cube.
    # Mathematically, their independent spatial states multiply together.
    # -----------------------------------------------------------------
    print("3. Simulating physical wave superposition inside the beam splitter...")
    interfered_field = field_A * field_B
    net_phase_landscape = np.angle(interfered_field)
    
    # -----------------------------------------------------------------
    # STEP 4: HARDWARE EQUALS SIGN (The Focused APD Readout)
    # The combined wave passes through your Fourier focusing lens.
    # The lens takes the wide spatial energy and collapses it to a center point.
    # -----------------------------------------------------------------
    print("4. Executing spatial Fourier transform via focused lens...")
    # The center pixel of a Fourier transform is equivalent to the sum of the spatial field
    apd_voltage_signal = np.abs(np.sum(interfered_field))
    
    # Calculate a baseline maximum possible voltage for scaling reference
    max_theoretical_voltage = (w * h) * 5.0 
    normalized_daq_output = (apd_voltage_signal / max_theoretical_voltage) * 10.0 # Scale to a 0-10V DAQ range
    
    print(f"\n>>> HARDWARE READOUT COMPLETE <<<")
    print(f"Simulated NI-DAQ Analog Voltage Spike: {normalized_daq_output:.4f} Volts")
    print("=========================================================\n")
    
    # -----------------------------------------------------------------
    # VISUALIZATION PIPELINE (Matplotlib UI)
    # -----------------------------------------------------------------
    # Explicitly unpack our 1 row, 3 column axes to prevent array errors
    fig, (ax_input, ax_kernel, ax_output) = plt.subplots(1, 3, figsize=(16, 6))
    
    # Render the input phase knot
    ax_input.imshow(mask_A, cmap='twilight')
    ax_input.set_title("Zone 1: Input Data Mask\n(Scrambled Spatial Phase Knot)")
    ax_input.axis('off')
    
    # Render the convolutional filter kernel
    ax_kernel.imshow(mask_B, cmap='twilight')
    ax_kernel.set_title("Zone 2: Kernel Filter Mask\n(Conjugate OAM Decoupler)")
    ax_kernel.axis('off')
    
    # Render the arriving phase profile before it hits the lens
    ax_output.imshow(net_phase_landscape, cmap='coolwarm', vmin=-np.pi, vmax=np.pi)
    ax_output.set_title(f"Terminal Wavefront Profile\nResulting DAQ Output: {normalized_daq_output:.3f} V")
    ax_output.axis('off')
    
    plt.tight_layout()
    print("Displaying full system execution schematic. Close window to release workspace.")
    plt.show()