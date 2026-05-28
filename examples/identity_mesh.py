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
    w, h = 800, 800  # Resolution for a crisp square visual
    
    # --- PHASE 1: ZONE 1 GRAPHICS (Matrix of All 1s) ---
    # We blend equal weights (1.0) of modes l=1, l=2, l=3, and l=4
    field_all_ones = np.zeros((h, w), dtype=np.complex128)
    for l in [1, 2, 3, 4]:
        field_all_ones += 1.0 * generate_pure_oam_field(w, h, l)
    mask_zone1 = field_to_mask(field_all_ones)
    
    # --- PHASE 2: ZONE 2 GRAPHICS (The Diagonal Identity Matrix Decoder) ---
    # To decode the identity operation, we apply the exact negative conjugates
    field_identity = np.zeros((h, w), dtype=np.complex128)
    for l in [-1, -2, -3, -4]:
        field_identity += 1.0 * generate_pure_oam_field(w, h, l)
    mask_zone2 = field_to_mask(field_identity)
    
    # --- PHASE 3: THE PHYSICAL RECOMBINATION (The Interference) ---
    # Multiplying the fields simulates the beams overlaying in the beam splitter
    combined_beam = field_all_ones * field_identity
    terminal_phase = np.angle(combined_beam)
    
    # --- MATPLOTLIB RENDERING ---
    fig, (ax_left, ax_right, ax_det) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Zone 1 Display
    ax_left.imshow(mask_zone1, cmap='twilight')
    ax_left.set_title("Zone 1 Mask: Matrix of All 1s\n(Superposition l = 1, 2, 3, 4)")
    ax_left.axis('off')
    
    # Zone 2 Display
    ax_right.imshow(mask_zone2, cmap='twilight')
    ax_right.set_title("Zone 2 Mask: Identity Decoder\n(Superposition l = -1, -2, -3, -4)")
    ax_right.axis('off')
    
    # APD Arriving Phase Display
    ax_det.imshow(terminal_phase, cmap='coolwarm', vmin=-np.pi, vmax=np.pi)
    ax_det.set_title("Arriving Beam Phase\n(Flat Profile = Identity Verified)")
    ax_det.axis('off')
    
    plt.tight_layout()
    print("Plotting optical identity matrix multiplication execution...")
    plt.show()