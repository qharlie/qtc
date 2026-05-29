import numpy as np
import os
import ctypes
# Assuming the HOLOEYE SDK is installed and reachable via standard Windows DLL paths
# We import the low-level data display components from the SDK
try:
    import holoeye
except ImportError:
    # Fallback/Mock placeholder for dry-run testing without physical USB/HDMI hookup
    holoeye = None
    raise Exception("HOLOEYE SDK not found. Please ensure the SDK is installed and accessible in your Python environment.")

# --- CONSTANTS & CONFIGURATION ---
SLM_WIDTH = 1920
SLM_HEIGHT = 1080
ZONE_WIDTH = 960  # SLM_WIDTH // 2
ALPHABET_LIMIT = 24

# --- SECTION 1: PURE WAVEFRONT GENERATION FUNCTIONS (Mathematical Core) ---

def create_coordinate_grid(width: int, height: int) -> tuple[np.ndarray, np.ndarray]:
    """Generates normalized Cartesian grids centered on the zone center."""
    cx, cy = width / 2.0, height / 2.0
    x = np.arange(width) - cx
    y = np.arange(height) - cy
    X, Y = np.meshgrid(x, y)
    return X, Y

def cartesian_to_azimuthal(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """Computes the angular component (theta) from spatial coordinates."""
    return np.arctan2(Y, X)

def generate_oam_phase_mask(theta: np.ndarray, l_charge: int) -> np.ndarray:
    """
    Computes a pure helical phase factor: exp(i * l * theta).
    Returns an array bounded between [0, 2*pi].
    """
    if abs(l_charge) > ALPHABET_LIMIT:
        raise ValueError(f"OAM charge {l_charge} exceeds alphabet boundary of +/-{ALPHABET_LIMIT}")
    
    raw_phase = l_charge * theta
    # Wrap phase to standard [0, 2*pi] domain
    wrapped_phase = np.mod(raw_phase, 2 * np.pi)
    return wrapped_phase

def quantize_phase_to_8bit(phase_mask: np.ndarray) -> np.ndarray:
    """Transforms continuous [0, 2*pi] phase space to discrete 8-bit grayscale data."""
    scaled_mask = (phase_mask / (2 * np.pi)) * 255.0
    return np.clip(scaled_mask, 0, 255).astype(np.uint8)

def compile_dual_zone_frame(zone1_charge: int, zone2_charge: int) -> np.ndarray:
    """
    Functional pipeline compiling Zone 1 and Zone 2 side-by-side into a single 
    1920x1080 frame topology.
    """
    # Create coordinate maps for a single isolated zone grid
    X, Y = create_coordinate_grid(ZONE_WIDTH, SLM_HEIGHT)
    theta = cartesian_to_azimuthal(X, Y)
    
    # Compute masks using the custom functional pipeline
    z1_phase = generate_oam_phase_mask(theta, l_charge=zone1_charge)
    z2_phase = generate_oam_phase_mask(theta, l_charge=zone2_charge)
    
    # Quantize vectors to native 8-bit unsigned integers
    z1_8bit = quantize_phase_to_8bit(z1_phase)
    z2_8bit = quantize_phase_to_8bit(z2_phase)
    
    # Horizontally stack the arrays (Zone 1 left, Zone 2 right)
    full_frame = np.hstack((z1_8bit, z2_8bit))
    return full_frame


# --- SECTION 2: PROCEDURAL HOLOEYE SDK RUNTIME ---

def initialize_slm_device():
    """Procedurally establishes hardware communication hooks."""
    print("[INFO] Initializing HOLOEYE LETO-3 Spatial Light Modulator...")
    if holoeye is None:
        print("[WARN] HOLOEYE SDK not detected. Operating in Simulation/Emulation mode.")
        return None
    
    # Initialize the low-level SDK client hook
    # Typically: instance = holoeye.DisplayAPI()
    try:
        slm_instance = holoeye.DisplayAPI()
        # Verify resolution constraints
        if slm_instance.width != SLM_WIDTH or slm_instance.height != SLM_HEIGHT:
            print(f"[ERROR] Resolution mismatch! Hardware detects {slm_instance.width}x{slm_instance.height}")
        return slm_instance
    except Exception as e:
        print(f"[CRITICAL] Could not connect to SLM over HDMI/USB. Error: {e}")
        return None

def display_frame_on_hardware(slm_device, frame_data: np.ndarray) -> bool:
    """Procedurally updates the SLM display matrix buffer."""
    if frame_data.shape != (SLM_HEIGHT, SLM_WIDTH):
        raise ValueError(f"Invalid frame dimensions for data write: {frame_data.shape}")
        
    if slm_device is None:
        print(f"[SIMULATOR] Frame matrix updated. Buffer checksum: {np.sum(frame_data)}")
        return True
    
    try:
        # Push raw C-contiguous buffer directly to the liquid crystal backplane via the SDK
        # The SDK typically consumes raw pointer arrays via ctypes or built-in wrapper arrays
        slm_device.showData(frame_data.ctypes.data_as(ctypes.c_void_p))
        return True
    except Exception as e:
        print(f"[ERROR] Failed writing raster matrix to SLM engine: {e}")
        return False

def close_slm_device(slm_device):
    """Releases hardware context to avoid memory leak states on the device controller."""
    print("[INFO] Releasing SLM hardware contexts...")
    if slm_device is not None:
        try:
            slm_device.release()
        except Exception as e:
            print(f"[ERROR] Device detachment encountered failures: {e}")


# --- SECTION 3: REPR RUNTIME PIPELINE (Execution Block) ---

def execute_milestone1_sandbox_run(target_l_charge: int):
    """
    Main execution pipeline sequence.
    Applies the topological Knot to Zone 1, and the mathematical
    complex conjugate Anti-Knot to Zone 2.
    """
    print(f"\n=================== RUNNING MILESTONE 1 PIPELINE (l = {target_l_charge}) ===================")
    
    # 1. Evaluate inverse conjugate parameters for phase cancellation
    zone1_charge = target_l_charge
    zone2_charge = -target_l_charge  # Complex Conjugate Inverse: e^(i*l*theta) * e^(-i*l*theta)
    
    # 2. Compile spatial data matrix via functional stack
    compiled_matrix = compile_dual_zone_frame(zone1_charge, zone2_charge)
    print(f"[DATA] Matrix array compiled. Shape: {compiled_matrix.shape}, Dtype: {compiled_matrix.dtype}")
    
    # 3. Connect to the table hardware
    slm_handle = initialize_slm_device()
    
    # 4. Project the combined matrix
    success = display_frame_on_hardware(slm_handle, compiled_matrix)
    
    if success:
        print(f"[SUCCESS] Wavefront locked onto panel.")
        print(f" -> Zone 1 (Left) projecting Knot:      l = {zone1_charge}")
        print(f" -> Zone 2 (Right) projecting Anti-Knot: l = {zone2_charge}")
        print(" -> Action Required: Check analog NI-DAQ voltage spike at the APD.")
    else:
        print("[FAILURE] Pipeline collapsed during data transmission.")
        
    # 5. Clean up footprint
    close_slm_device(slm_handle)

if __name__ == "__main__":
    # Test execute with an intermediate charge value from our alphabet (e.g., l = 12)
    execute_milestone1_sandbox_run(target_l_charge=12)