# calculations.py

import numpy as np
import gsw


def get_center_of_mass(lon: np.ndarray, lat: np.ndarray, pressure: np.ndarray) -> tuple:
    """
    Calculates the center of mass for given longitude, latitude, and pressure arrays.
    Handles cases where inputs are empty or contain only NaN values.

    Parameters:
    - lon (np.ndarray): Array of longitude values.
    - lat (np.ndarray): Array of latitude values.
    - pressure (np.ndarray): Array of pressure values.

    Returns:
    - tuple: A tuple containing the mean longitude, mean latitude, and mean pressure. If an input is empty or all-NaN, the corresponding value in the tuple is np.nan.
    """
    def safe_nanmean(arr: np.ndarray) -> float:
        """
        Safely computes the mean of an array, returning np.nan if the array is empty
        or contains only NaN values.
        """
        if arr.size == 0 or np.isnan(arr).all():
            return np.nan
        return np.nanmean(arr)
    
    return (
        safe_nanmean(lon),
        safe_nanmean(lat),
        safe_nanmean(pressure)
    )

def get_sigma_theta(salinity, temperature, cnt=False) -> tuple[np.ndarray,np.ndarray,np.ndarray]|tuple[np.ndarray,np.ndarray,np.ndarray,np.ndarray]:
    # Remove NaNs first to work with clean data
    mask = ~(np.isnan(salinity) | np.isnan(temperature))
    salinity, temperature = salinity[mask], temperature[mask]
    
    # Set target points based on input size
    target_points = min(100, len(salinity))
    
    # Calculate grid boundaries
    mint, maxt = np.min(temperature), np.max(temperature)
    mins, maxs = np.min(salinity), np.max(salinity)
    tempL = np.linspace(mint - 0.5, maxt + 0.5, target_points)
    salL = np.linspace(mins - 0.5, maxs + 0.5, target_points)
    Tg, Sg = np.meshgrid(tempL, salL)
    
    # Calculate density
    sigma_theta = get_density(Sg, Tg)
    
    return (Sg, Tg, sigma_theta, np.linspace(sigma_theta.min(), sigma_theta.max(), target_points)) if cnt else (Sg, Tg, sigma_theta)



# def get_sigma_theta(salinity, temperature, cnt=False) -> tuple[np.ndarray,np.ndarray,np.ndarray]|tuple[np.ndarray,np.ndarray,np.ndarray,np.ndarray]:
#     """
#     Computes sigma_theta on a grid of temperature and salinity data.
    
#     Args:
#         salinity (np.ndarray): Array of salinity values.
#         temperature (np.ndarray): Array of temperature values.
#         cnt (bool): Whether to return a linear range of sigma_theta values.
    
#     Returns:
#         tuple: Meshgrid of salinity and temperature, calculated sigma_theta, 
#                and optionally a linear range of sigma_theta values.
#     """
#     # Determine target sample size
#     num_points = len(temperature)
#     target_points = min(10_000, num_points)
#     downsample_factor = max(1, num_points // target_points)

#     # Downsample if necessary
#     salinity = salinity[::downsample_factor]
#     temperature = temperature[::downsample_factor]

#     # Remove NaNs from the arrays
#     salinity, temperature = salinity[~np.isnan(salinity)], temperature[~np.isnan(temperature)]

#     # Calculate grid boundaries and mesh
#     mint, maxt = np.min(temperature), np.max(temperature)
#     mins, maxs = np.min(salinity), np.max(salinity)
#     tempL, salL = np.linspace(mint - 1, maxt + 1, target_points), np.linspace(mins - 1, maxs + 1, target_points)
#     Tg, Sg = np.meshgrid(tempL, salL)

#     # Calculate density
#     sigma_theta = get_density(Sg, Tg)

#     # Optionally, return a linear range of sigma_theta values
#     return (Sg, Tg, sigma_theta, np.linspace(sigma_theta.min(), sigma_theta.max(), target_points)) if cnt else (Sg, Tg, sigma_theta)


def get_density(salinity, temperature) -> np.ndarray:
    """
    Calculate seawater density (sigma-0) from salinity and temperature.

    Parameters
    ----------
    salinity : array_like
        Practical salinity [PSU]
    temperature : array_like
        Temperature [°C]

    Returns
    -------
    np.ndarray
        Potential density [kg/m³] referenced to 0 dbar pressure
    """
    return np.array(gsw.sigma0(salinity, temperature))


def rotate_vector(u, v, theta_rad) -> tuple[np.ndarray, np.ndarray]:
    """
    Rotate velocity vectors by a given angle.

    Parameters
    ----------
    u : array_like
        Zonal (east-west) velocity component
    v : array_like
        Meridional (north-south) velocity component
    theta_rad : float
        Rotation angle in radians

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Rotated u and v components (u_rotated, v_rotated)
    """
    u_rotated = u * np.cos(theta_rad) - v * np.sin(theta_rad)
    v_rotated = u * np.sin(theta_rad) + v * np.cos(theta_rad)
    return u_rotated, v_rotated

