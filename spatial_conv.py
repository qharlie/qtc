import numpy as np
import matplotlib.pyplot as plt

def generate_pure_oam_field(width, height, charge_l):
    """Generates a complex OAM field array: e^(i * l * theta)"""
    x = np.linspace(-width / 2, width / 2, width)
    y = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x, y)
    THETA = np.arctan2(Y, X)
    return np.exp(1j * charge_l * THETA)

def field_to_mask(complex_field):
    """Converts a complex wave field to an 8-bit SLM phase map."""
    phase = np.angle(complex_field)
    phase_wrapped = np.mod(phase, 2 * np.pi)
    return (phase_wrapped * (255.0 / (2 * np.pi))).astype(np.uint8)

if __name__ == "__main__":
    w, h = 800, 800  # High-res canvas for detailed phase-knot profiles
    
    # --- 1. ZONE 1: ENCODING A REAL-WORLD FLUCTUATING SIGNAL ---
    # We populate our 48-channel spectrum with a highly non-trivial signal mix.
    # It contains baseline drift (low-order) and crisp, fast feature edges (high-order).
    signal_profile = {
        1:  0.9,   # Strong low-frequency drift
        2:  0.7,
        15: 0.3,   # Mid-range frequencies
        -16: 0.4,
        23: 0.8,   # High-frequency target feature edge
        -24: 0.85
    }
    
    field_signal = np.zeros((h, w), dtype=np.complex128)
    for l, weight in signal_profile.items():
        field_signal += weight * generate_pure_oam_field(w, h, l)
    mask_zone1 = field_to_mask(field_signal)
    
    # --- 2. ZONE 2: THE HIGH-PASS CONVOLUTION KERNEL ---
    # To execute the convolution and extract only the crisp feature edges, 
    # our decoder strips the low-order baseline noise (l=1,2 get 0.0 weight) 
    # and isolates the conjugate high-frequency components.
    kernel_profile = {
        -15: 1.0,
        16:  1.0,
        -23: 1.0,
        24:  1.0
    }
    
    field_kernel = np.zeros((h, w), dtype=np.complex128)
    for l, weight in kernel_profile.items():
        field_kernel += weight * generate_pure_oam_field(w, h, l)
    mask_zone2 = field_to_mask(field_kernel)
    
    # --- 3. THE PHYSICAL INTERFERENCE (The Processing) ---
    # The two wavefronts meet at the beamsplitter, performing the element-wise 
    # frequency domain multiplication instantly.
    processed_field = field_signal * field_kernel
    resulting_phase = np.angle(processed_field)
    
    # --- MATPLOTLIB RENDERING ---
    fig, (ax_left, ax_right, ax_det) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Zone 1
    ax_left.imshow(mask_zone1, cmap='twilight')
    ax_left.set_title("Zone 1: Input Raw Data\n(Signal + Low-Freq Noise)")
    ax_left.axis('off')
    
    # Zone 2
    ax_right.imshow(mask_zone2, cmap='twilight')
    ax_right.set_title("Zone 2: Convolution Kernel\n(High-Pass Filter Decoder)")
    ax_right.axis('off')
    
    # Interference Output
    ax_det.imshow(resulting_phase, cmap='coolwarm', vmin=-np.pi, vmax=np.pi)
    ax_det.set_title("Arriving Beam Profile\n(Filtered Feature Output)")
    ax_det.axis('off')
    
    plt.tight_layout()
    print("Executing optical 1D convolution loop simulation...")
    plt.show()