import numpy as np
import matplotlib.pyplot as plt

def generate_oam_beam(width, height, channels):
    """
    Simulates the complex spatial wavefront resulting from multiplexed OAM states.
    """
    x = np.linspace(-width / 2, width / 2, width)
    y = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x, y)
    THETA = np.arctan2(Y, X)
    
    # Initialize an empty complex canvas
    complex_field = np.zeros((height, width), dtype=np.complex128)
    
    for l, weight in channels.items():
        # Superimpose each component: weight * e^(i * l * theta)
        complex_field += weight * np.exp(1j * l * THETA)
        
    return complex_field

def convert_field_to_8bit_mask(complex_field):
    """
    Extracts the phase angle from a complex field and formats it for the SLM backplane.
    """
    phase = np.angle(complex_field)
    phase_wrapped = np.mod(phase, 2 * np.pi)
    mask_8bit = (phase_wrapped * (255.0 / (2 * np.pi))).astype(np.uint8)
    return mask_8bit

# --- Execution Simulation ---
if __name__ == "__main__":
    # Standard dimensions for half of the HOLOEYE LETO-3 screen
    zone_width = 960
    zone_height = 1080
    
    # -----------------------------------------------------------------
    # THE COMPUTATION COMPUTING MATRIX
    # We are encoding a highly complex state vector into the photons.
    # We pack lanes l=-18, l=-3, l=+8, and l=+22 simultaneously.
    # -----------------------------------------------------------------
    matrix_problem_A = {
        -18: 0.5,
        -3:  1.0,
        8:   0.7,
        22:  0.9
    }
    
    # Because of the conservation of angular momentum inside the BBO crystal,
    # Photon B is born as the perfect quantum conjugate mirror of Photon A (l_A + l_B = 0).
    # Therefore, to decode the entire joint state simultaneously, Zone 2 must apply
    # the exact negative-signed conjugate weights.
    matrix_decoder_B = {
        18: 0.5,
        3:  1.0,
        -8:  0.7,
        -22: 0.9
    }
    
    print("Synthesizing Zone 1 (Photon A) complex phase knot...")
    field_A = generate_oam_beam(zone_width, zone_height, matrix_problem_A)
    mask_A = convert_field_to_8bit_mask(field_A)
    
    print("Synthesizing Zone 2 (Photon B) entangled matching conjugate...")
    field_B = generate_oam_beam(zone_width, zone_height, matrix_decoder_B)
    mask_B = convert_field_to_8bit_mask(field_B)
    
    # -----------------------------------------------------------------
    # THE HARDWARE SIMULATION VALUE: COLLAPSE INTERFERENCE TEST
    # Let's simulate what happens when these two physical wavefronts meet 
    # at the detector. If they match perfectly, they collapse into a flat plane.
    # -----------------------------------------------------------------
    # Quantum cross-multiplication is represented by multiplying the fields
    joint_quantum_state = field_A * field_B
    net_phase_landscape = np.angle(joint_quantum_state)
    
    # -----------------------------------------------------------------
    # GRAPHICS RENDERING (The Matplotlib UI)
    # -----------------------------------------------------------------
    fig, (ax_left, ax_right, ax_det) = plt.subplots(1, 3, figsize=(15, 6))    
    
    # 1. Render Zone 1 (What Photon A strikes)
    # 1. Render Zone 1 (What Photon A strikes)
    ax_left.imshow(mask_A, cmap='twilight')
    ax_left.set_title("Zone 1: Photon A Matrix Mask\n(Scrambled Phase Knot)")
    ax_left.axis('off')
    
    # 2. Render Zone 2 (What Photon B strikes)
    ax_right.imshow(mask_B, cmap='twilight')
    ax_right.set_title("Zone 2: Photon B Decoder Mask\n(Entangled Mirror Match)")
    ax_right.axis('off')
    
    # 3. Render the Resulting Interference Wavefront arriving at the detector
    ax_det.imshow(net_phase_landscape, cmap='coolwarm', vmin=-np.pi, vmax=np.pi)
    ax_det.set_title("Terminal Wavefront Profile\n(Flat Plane Wave = Correct Calculation)")
    ax_det.axis('off')
    
    plt.tight_layout()
    print("Displaying dual-zone entanglement mask layout and terminal collapse profiles...")
    plt.show()