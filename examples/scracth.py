import numpy as np
import matplotlib.pyplot as plt

def generate_oam_phase_mask(width, height, charge_l):
    """
    Generates a 2D 8-bit phase mask array for a specific Orbital Angular Momentum (OAM).
    
    Parameters:
        width (int): Width of the SLM target canvas in pixels.
        height (int): Height of the SLM target canvas in pixels.
        charge_l (int): The topological charge / number of corkscrew twists.
        
    Returns:
        np.ndarray: A 2D uint8 matrix (values 0-255) ready for the HOLOEYE SDK.
    """
    # 1. Create a center-zeroed pixel coordinate grid (x, y)
    x_indices = np.linspace(-width / 2, width / 2, width)
    y_indices = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x_indices, y_indices)
    
    # 2. Convert Cartesian pixel grids to Polar angle grid (theta)
    # atan2 returns angles from -pi to +pi relative to the center of the beam
    THETA = np.arctan2(Y, X)
    
    # 3. Apply the topological twist calculation
    # Phase = charge * theta. This builds the spiral staircase geometry.
    phase_continuous = charge_l * THETA
    
    # 4. Wrap the phase back into the fundamental 0 to 2*pi domain
    # This prevents values from escaping the liquid crystals' physical limits
    phase_wrapped = np.mod(phase_continuous, 2 * np.pi)
    
    # 5. Normalize the 0 to 2*pi floating-point array into 8-bit unsigned integers
    # 0 maps to 0 phase shift, 255 maps to a full 2*pi (360 degree) delay
    mask_8bit = (phase_wrapped * (255.0 / (2 * np.pi))).astype(np.uint8)
    
    return mask_8bit

# --- Sandbox Execution ---
if __name__ == "__main__":
    # For Milestone 1, we split the 1920x1080 panel into two side-by-side halves.
    # Each zone gets a 960x1080 canvas.
    zone_width = 960
    zone_height = 1080
    
    # Target twist for our high-dimensional space vector element
    target_twist = 24  
    
    print(f"Generating 2D spatial coordinate grid for l = {target_twist}...")
    
    # Generate the Encoder Mask (Zone 1)
    # This physically carves a tight 24-twist spiral into the flat 405nm wave
    encoder_mask = generate_oam_phase_mask(zone_width, zone_height, charge_l=target_twist)
    
    # Generate the Decoder Mask (Zone 2)
    # The mathematical inverse (Anti-Knot). This unwinds the 24-twist spiral back to flat.
    decoder_mask = generate_oam_phase_mask(zone_width, zone_height, charge_l=-target_twist)
    
    # --- Visual Verification Block ---
    # Unpacking the axis tuple explicitly into two variables so matplotlib doesn't crash
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10, 5))
    
    # Render the Left Encoder Panel
    ax_left.imshow(encoder_mask, cmap='gray')
    ax_left.set_title(f"Zone 1: Encoder (l = +{target_twist})")
    ax_left.axis('off')
    
    # Render the Right Decoder Panel
    ax_right.imshow(decoder_mask, cmap='gray')
    ax_right.set_title(f"Zone 2: Decoder (l = -{target_twist})")
    ax_right.axis('off')
    
    plt.tight_layout()
    print("Displaying 2D coordinate mask visual map. Close window to terminate script.")
    plt.show()