import numpy as np
import matplotlib.pyplot as plt

def generate_pure_oam_mask(width, height, charge_l):
    """
    Generates a 2D 8-bit phase mask array for a specific topological charge.
    
    Parameters:
        width (int): Canvas width in pixels (one half of the SLM).
        height (int): Canvas height in pixels (full SLM height).
        charge_l (int): The topological charge / number of helical twists.
        
    Returns:
        np.ndarray: A 2D uint8 matrix (0-255) mapping the phase layout.
    """
    # 1. Create a center-zeroed pixel coordinate grid (x, y)
    x_indices = np.linspace(-width / 2, width / 2, width)
    y_indices = np.linspace(-height / 2, height / 2, height)
    X, Y = np.meshgrid(x_indices, y_indices)
    
    # 2. Convert to Polar angle grid (theta) from -pi to +pi
    THETA = np.arctan2(Y, X)
    
    # 3. Apply the topological twist calculation (Phase = charge * theta)
    phase_continuous = charge_l * THETA
    
    # 4. Wrap the phase back into the fundamental 0 to 2*pi domain
    phase_wrapped = np.mod(phase_continuous, 2 * np.pi)
    
    # 5. Normalize the 0 to 2*pi array into 8-bit unsigned integers (0-255)
    mask_8bit = (phase_wrapped * (255.0 / (2 * np.pi))).astype(np.uint8)
    
    return mask_8bit

if __name__ == "__main__":
    # Panel dimensions for half of the HOLOEYE LETO-3 screen
    zone_width = 960
    zone_height = 1080
    
    # Milestone 1 validation target channel
    target_charge = 24  
    
    print(f"[+] Generating Milestone 1 validation masks for l = {target_charge}...")
    
    # Zone 1: The Knot (Clockwise spiral)
    knot_mask = generate_pure_oam_mask(zone_width, zone_height, charge_l=target_charge)
    
    # Zone 2: The Anti-Knot (Counter-clockwise spiral)
    anti_knot_mask = generate_pure_oam_mask(zone_width, zone_height, charge_l=-target_charge)
    
    # --- Matplotlib Visualizer (Explicit Subplot Unpacking) ---
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Render Zone 1 (Left Half)
    ax_left.imshow(knot_mask, cmap='twilight')
    ax_left.set_title(f"Zone 1: The Knot\n(Encoder Matrix l = +{target_charge})")
    ax_left.axis('off')
    
    # Render Zone 2 (Right Half)
    ax_right.imshow(anti_knot_mask, cmap='twilight')
    ax_right.set_title(f"Zone 2: The Anti-Knot\n(Decoder Matrix l = -{target_charge})")
    ax_right.axis('off')
    
    plt.tight_layout()
    print("[+] Rendering side-by-side array. Close the window to release the terminal.")
    plt.show()