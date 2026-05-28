import numpy as np
import matplotlib.pyplot as plt

def generate_pure_oam_field(width, height, charge_l):
    """Generates the underlying continuous complex field for a pure OAM mode."""
    x = np.linspace(-width / 2, width / 2, width)
    y = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x, y)
    THETA = np.arctan2(Y, X)
    return np.exp(1j * charge_l * THETA)

# --- Automated Scanning Simulation ---
if __name__ == "__main__":
    w, h = 500, 500 # Using a smaller canvas for fast calculation loop
    
    # 1. Define the input vector programmed into Zone 1
    # We load data into three specific topological lanes
    zone1_vector = {
        2: 1.0,   # Channel 2  = Full power
        -5: 0.8,  # Channel -5 = 80% power
        12: 0.4   # Channel 12 = 40% power
    }
    
    # Synthesize the physical composite wave leaving Zone 1
    composite_wave = np.zeros((h, w), dtype=np.complex128)
    for l, weight in zone1_vector.items():
        composite_wave += weight * generate_pure_oam_field(w, h, l)
        
    # 2. Automated Diagnostic Sweep (Scan decoder from l = -15 to +15)
    scan_range = np.arange(-15, 16)
    detected_powers = []
    
    print("Beginning automated topological channel sweep...")
    for decode_l in scan_range:
        # Generate the test decoder template for Zone 2
        # Mathematically, decoding is multiplying by the complex conjugate: e^(-i * l * theta)
        decoder_template = generate_pure_oam_field(w, h, -decode_l)
        
        # The physical step: The beam hits Zone 2
        # This multiplies the incoming wave by our decoder phase profile
        transformed_wave = composite_wave * decoder_template
        
        # The Fourier step: The lens focuses the wave down to a single center point.
        # Mathematically, the center point of a Fourier transform is the sum of all pixels.
        center_pixel_intensity = np.abs(np.sum(transformed_wave))
        
        detected_powers.append(center_pixel_intensity)
        
    # Normalize results for plotting
    detected_powers = np.array(detected_powers)
    detected_powers /= np.max(detected_powers)
    
    # 3. Plot the Channel Isolation Spectrum
    plt.figure(figsize=(10, 5))
    plt.bar(scan_range, detected_powers, color='crimson', edgecolor='black', alpha=0.7)
    
    # Label the known inputs so you can see the isolation
    for l, weight in zone1_vector.items():
        plt.annotate(f"Input l={l}", xy=(l, weight), xytext=(l+0.5, weight+0.05),
                     arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=4))
        
    plt.title("Topological Channel Scan (Simulated APD Output)")
    plt.xlabel("Zone 2 Decoder Charge (l)")
    plt.ylabel("Normalized Detector Intensity (Voltage Spike)")
    plt.xticks(np.arange(-15, 16, 2))
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    print("Scan complete. Displaying isolation matrix...")
    plt.show()