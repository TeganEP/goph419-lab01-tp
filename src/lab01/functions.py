import numpy as np


def launch_angle_range(ve_v0, alpha, tol_alpha):
    """
    Calculate the range of allowable launch angles for a rocket.

    Parameters
    ----------
    ve_v0 : float
        Ratio of escape velocity to terminal velocity.
    alpha : float
        Desired maximum altitude as a fraction of Earth's radius.
    tol_alpha : float
        Tolerance for maximum altitude.

    Returns
    -------
    np.array
        Minimum and maximum allowable launch angles in radians.
    """

    def launch_angle(ve_v0, alpha):
        """
        Helper function to compute a single launch angle.

        Parameters
        ----------
        ve_v0 : float
            Ratio of escape velocity to terminal velocity.
        alpha : float
            Desired maximum altitude as a fraction of Earth's radius.

        Returns
        -------
        float
            The launch angle in radians.
        """
        # Compute sin(phi0) based on the input parameters
        sin_phi0 = np.sqrt(1 - (alpha / ve_v0) ** 2)
        # Calculate and return the arcsin of sin_phi0
        return np.arcsin(sin_phi0)

    # Calculate lower and upper bounds for alpha based on the tolerance
    lower_alpha = alpha * (1 - tol_alpha)
    upper_alpha = alpha * (1 + tol_alpha)

    # Compute the minimum and maximum launch angles
    phi_min = launch_angle(ve_v0, upper_alpha)
    phi_max = launch_angle(ve_v0, lower_alpha)

    # Return the range of launch angles as a numpy array
    return np.array([phi_min, phi_max])
