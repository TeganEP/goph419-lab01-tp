import numpy as np
import matplotlib.pyplot as plt
import os
from src.lab01.functions import launch_angle_range


def main():
    """
    Main function to calculate and plot the range of launch angles.
    """
    ve_v0 = 2.0  # Velocity ratio
    tol_alpha = 0.04  # Tolerance for altitude
    alpha_values = np.linspace(0.01, 0.5, 100)  # Array of alpha values

    min_angles = []  # List to store minimum launch angles
    max_angles = []  # List to store maximum launch angles

    # Ensure the figures directory exists to save the plot
    if not os.path.exists("figures"):
        os.makedirs("figures")

    # Compute the launch angles for each alpha value
    for alpha in alpha_values:
        try:
            # Compute the range of launch angles for the current alpha
            phi_range = np.degrees(launch_angle_range(ve_v0, alpha, tol_alpha))
            min_angles.append(phi_range[0])  # Add the minimum launch angle
            max_angles.append(phi_range[1])  # Add the maximum launch angle
        except ValueError as e:
            # Handle exceptions and print the error message
            print(f"Error for alpha={alpha}: {e}")
            min_angles.append(None)
            max_angles.append(None)

    # Filter out None values for plotting
    min_angles = [angle for angle in min_angles if angle is not None]
    max_angles = [angle for angle in max_angles if angle is not None]
    alpha_values = alpha_values[:len(min_angles)]

    # Generate the plot
    plt.figure(figsize=(10, 6))
    plt.plot(alpha_values, min_angles, label="Minimum Launch Angle", color="blue")
    plt.plot(alpha_values, max_angles, label="Maximum Launch Angle", color="red")
    plt.xlabel("Alpha (maximum altitude as fraction of Earth’s radius)")
    plt.ylabel("Launch Angle (degrees)")
    plt.title("Launch Angle Range vs. Alpha")
    plt.legend()
    plt.grid(True)
    plt.savefig("figures/launch_angle_vs_alpha.png")  # Save the plot to the figures directory
    plt.show()  # Display the plot


if __name__ == "__main__":
    # Run the main function when executed directly
    main()
