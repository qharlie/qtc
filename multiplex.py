import numpy as np
import matplotlib.pyplot as plt

def generate_multiplexed_mask(width, height, channels):
    """
    Blends multiple OAM channels into a single phase-only spatial mask.
    
    Parameters:
        width (int): Canvas width in pixels.
        height (int): Canvas height in pixels.
        channels (dict): A dictionary mapping {topological_charge_l: amplitude_weight}
                         e.g., {3: 1.0, -7: 0.5}
                         
    Returns:
        np.ndarray: A 2D uint8 matrix (0-255) for the SLM backplane.
    """
    # 1. Coordinate Grid Setup
    x_indices = np.linspace(-width / 2, width / 2, width)
    y_indices = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x_indices, y_indices)
    THETA = np.arctan2(Y, X)
    
    # 2. Synthesize the Complex Fields in Superposition
    # We initialize an empty complex-valued grid matching our pixel canvas
    complex_field = np.zeros((height, width), dtype=np.complex128)
    
    for l, weight in channels.items():
        # Evolve the helical wavefront for this specific channel component
        # e^(i * l * theta)
        channel_field = weight * np.exp(1j * l * THETA)
        # Stack it directly onto the same spatial canvas
        complex_field += channel_field
        
    # 3. Extract the Phase Angle from the Combined Wavefront
    # np.angle returns values from -pi to +pi
    combined_phase = np.angle(complex_field)
    
    # 4. Wrap and Normalize to 8-bit Space (0 to 255)
    phase_wrapped = np.mod(combined_phase, 2 * np.pi)
    mask_8bit = (phase_wrapped * (255.0 / (2 * np.pi))).astype(np.uint8)
    
    return mask_8bit

# --- Main Test Pipeline ---
if __name__ == "__main__":
    zone_width = 960
    zone_height = 1080
    
    # Define our data vector! 
    # We are packing three channels into the exact same beam space:
    # Channel l=+2 (Weight 1.0), Channel l=-5 (Weight 0.8), Channel l=+12 (Weight 0.4)
    input_vector = {
        2: 1.0,
        -5: 0.8,
        12: 0.4
    }
    
    print("Synthesizing multi-channel orthogonal superposition mask...")
    mixed_encoder = generate_multiplexed_mask(zone_width, zone_height, input_vector)
    
    # To decode or "read" the data out classically, your decoder zone has to match
    # the exact conjugate transpose of the channel you want to isolate.
    # Let's see what the composite matrix looks like:
    fig, ax = plt.subplots(figsize=(6, 6))
    
    ax.imshow(mixed_encoder, cmap='twilight') # Using 'twilight' because it loops gracefully for phase
    ax.set_title("Zone 1: Multiplexed State Matrix\n(l=+2, l=-5, l=+12 Co-Existing)")
    ax.axis('off')
    
    plt.tight_layout()
    print("Rendering multiplexed wavefront pattern...")
    plt.show()