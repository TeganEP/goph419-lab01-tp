import numpy as np
from src.lab01.functions import launch_angle_range


def test_launch_angle_range():
    """
    Test the launch_angle_range function to ensure correctness.
    """
    ve_v0 = 2.0  # Velocity ratio
    alpha = 0.25  # Maximum altitude as a fraction of Earth's radius
    tol_alpha = 0.02  # Tolerance for altitude

    # Expected angles in radians (calculated using external tool or reference)
    expected_min_angle = np.arcsin(np.sqrt(1 - (alpha * (1 + tol_alpha) / ve_v0) ** 2))
    expected_max_angle = np.arcsin(np.sqrt(1 - (alpha * (1 - tol_alpha) / ve_v0) ** 2))

    # Compute the launch angle range using the function
    phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
    phi_min, phi_max = phi_range

    # Debug prints for computed and expected values
    print(f"Expected min angle (radians): {expected_min_angle}")
    print(f"Expected max angle (radians): {expected_max_angle}")
    print(f"Computed phi_min (radians): {phi_min}")
    print(f"Computed phi_max (radians): {phi_max}")

    # Check if the computed values are close to the expected values within a small tolerance
    assert np.isclose(phi_min, expected_min_angle, atol=0.01), f"phi_min test failed: {phi_min} != {expected_min_angle}"
    assert np.isclose(phi_max, expected_max_angle, atol=0.01), f"phi_max test failed: {phi_max} != {expected_max_angle}"

    print("All tests passed.")


if __name__ == "__main__":
    # Run the test function when executed directly
    test_launch_angle_range()
