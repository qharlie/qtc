import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def render_wavefront_visual(l_charge: int, title_suffix: str):
    """
    Computes and renders a 3D wavefront surface and its corresponding 
    2D transverse intensity profile for a given topological OAM charge.
    """
    fig = plt.figure(figsize=(12, 5))
    
    # --- Left Subplot: 3D Wavefront Geometry ---
    ax1 = fig.add_subplot(121, projection='3d')
    
    # Build cylindrical meshgrid mapping
    r = np.linspace(0.1, 2, 30) # Start at 0.1 to leave space for the central singularity core
    theta = np.linspace(0, 2 * np.pi, 100)
    R, Theta = np.meshgrid(r, theta)
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    
    # Line 23: Fixed empty syntax error by explicitly populating the list of discrete propagation planes
    z_planes = [1.0, 2.5, 4.0]
    
    for z_val in z_planes:
        if l_charge == 0:
            # Flat plane wave: wavefront surface is a constant flat sheet
            Z = np.full_like(X, z_val)
            intensity = np.exp(-R**2)  # Solid Gaussian distribution
        else:
            # Helical wave: wavefront surface is a screw-like spiral staircase
            # The phase wrap modifies the Z position relative to the azimuthal angle (Theta)
            Z = z_val + (l_charge * Theta) / (2 * np.pi)
            intensity = (R**2) * np.exp(-R**2) # Vortex doughnut distribution (zero intensity at center)
            
        # Plot the calculated 3D surface mesh
        ax1.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(intensity), 
                         shade=False, rstride=1, cstride=1, alpha=0.75)
        
    ax1.set_title(f"3D Wavefront Topology ({title_suffix})", fontsize=12)
    ax1.set_xlabel("X Axis")
    ax1.set_ylabel("Y Axis")
    ax1.set_zlabel("Propagation Axis (Z)")
    ax1.set_zlim(0, 6)
    ax1.view_init(elev=22, azim=45)
    
    # --- Right Subplot: 2D Spatial Transverse Profile ---
    ax2 = fig.add_subplot(122)
    x_2d = np.linspace(-2.5, 2.5, 250)
    y_2d = np.linspace(-2.5, 2.5, 250)
    X_2d, Y_2d = np.meshgrid(x_2d, y_2d)
    R_2d = np.sqrt(X_2d**2 + Y_2d**2)
    
    if l_charge == 0:
        intensity_2d = np.exp(-R_2d**2)
        ax2.set_title("Transverse Profile: Solid Gaussian Spot ($l=0$)", fontsize=11)
    else:
        # Higher charges scale the inner dark singularity wider
        intensity_2d = (R_2d**(2 * abs(l_charge))) * np.exp(-R_2d**2)
        ax2.set_title(f"Transverse Profile: OAM Ring Singularity ($l={l_charge}$)", fontsize=11)
        
    im = ax2.imshow(intensity_2d, extent=[-2.5, 2.5, -2.5, 2.5], cmap='viridis', origin='lower')
    plt.colorbar(im, ax=ax2, label='Relative Optical Intensity')
    ax2.set_xlabel("X Plane Coordinate")
    ax2.set_ylabel("Y Plane Coordinate")
    
    plt.tight_layout()
    
    # Save image out to your workspace directory for easy retrieval
    filename = f"oam_profile_l_{l_charge}.png"
    plt.savefig(filename, dpi=300)
    print(f"[SUCCESS] Exported high-resolution graphic to: {filename}")
    plt.show()

# --- RUN DESIRED VISUALIZATION PLOTS ---
if __name__ == "__main__":
    # Generate the baseline flat laser profile
    render_wavefront_visual(l_charge=0, title_suffix="l = 0 Planar Baseline")
    
    # Generate the counter-clockwise helical channel
    render_wavefront_visual(l_charge=-4, title_suffix="l = -4 Left-Handed Helix")
    
    # Generate the high-density clockwise helical channel
    render_wavefront_visual(l_charge=6, title_suffix="l = +6 Right-Handed Helix")