import numpy as np
import pandas as pd
import xarray as xr
from itertools import combinations
import re

from gerg_plotting.data_classes.data import Data
from gerg_plotting.data_classes.variable import Variable


def normalize_string(input_string: str) -> str:
    """
    Normalize string by converting to lowercase and standardizing special characters.

    Parameters
    ----------
    input_string : str
        String to normalize

    Returns
    -------
    str
        Normalized string with special characters replaced by underscores

    Raises
    ------
    ValueError
        If input is not a string
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")
    
    # Define the characters to be replaced by underscores
    replace_pattern = r"[ \t\n\r\f\v.,;:!@#$%^&*()+=?/<>|\\\"'`~\[\]{}]"
    
    # Convert to lowercase
    normalized = input_string.lower()
    
    # Replace specified characters with underscores
    normalized = re.sub(replace_pattern, "_", normalized)
    
    # Collapse multiple underscores into one
    normalized = re.sub(r"__+", "_", normalized)
    
    # Remove leading and trailing underscores
    normalized = normalized.strip("_")
    
    return normalized


def merge_dicts(*dict_args):
    """
    Merge multiple dictionaries with later dictionaries taking precedence.

    Parameters
    ----------
    ``*dict_args`` : dict
        Variable number of dictionaries to merge

    Returns
    -------
    dict
        New dictionary containing merged key-value pairs
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def create_combinations_with_underscore(strings):
    """
    Generate pairwise combinations of strings joined by underscores.

    Parameters
    ----------
    strings : list
        List of strings to combine

    Returns
    -------
    list
        List of combined strings including original strings
    """
    # Generate all pairwise combinations
    pairs = combinations(strings, 2)
    # Join each pair with an underscore
    combination= ["_".join(pair) for pair in pairs]
    combination.extend(strings)
    return combination

def custom_legend_handles(labels:list[str],colors,hatches=None,color_hatch_not_background:bool=False):
    """
    Create custom legend handles with specified colors and patterns.

    Parameters
    ----------
    labels : list[str]
        List of legend labels
    colors : list
        List of colors for patches
    hatches : list, optional
        List of hatch patterns
    color_hatch_not_background : bool, optional
        Whether to color hatch instead of background

    Returns
    -------
    list
        List of matplotlib patch objects for legend
    """
    import matplotlib.patches as mpatches

    assert len(labels) == len(colors)

    labels = [label.replace('_','/') for label in labels]

    if hatches is None:
        hatches = [None for _ in labels]

    if color_hatch_not_background:
        legend_handles = [mpatches.Patch(edgecolor=color, facecolor='none', label=label, hatch=hatch) for color, label, hatch in zip(colors, labels, hatches)]

    else:
        # Create custom legend handles
        legend_handles = [mpatches.Patch(facecolor=color, label=label, hatch=hatch) for color, label, hatch in zip(colors, labels, hatches)]

    return legend_handles

def _map_variables(keys:list[str], values:list[str], synonyms:dict[str,list[str]]|None=None, blocklist:dict[str,list[str]]|None=None):
    """
    Map variable names to their corresponding values using flexible matching.

    Parameters
    ----------
    keys : list[str]
        List of target variable names
    values : list[str]
        List of available variable names
    synonyms : dict, optional
        Dictionary of variable synonyms
    blocklist : dict, optional
        Dictionary of terms to avoid for each variable

    Returns
    -------
    dict
        Mapping of variables to their matched values
    """
    # Initialize the dictionary with None for each key
    mapped_dict = {key: None for key in keys}
    
    # Iterate through each key
    for key in keys:
        # Gather possible matches, starting with the key itself
        possible_matches = [key]
        
        # Add synonyms if provided
        if synonyms and key in synonyms:
            possible_matches.extend(synonyms[key])
        
        # Get blocked words for the key if provided
        blocked_words = blocklist.get(key, []) if blocklist else []
        
        # Search through values for matches
        for value in values:
            # Check if the value is blocked for the key
            if any(block.lower() in value.lower() for block in blocked_words):
                continue  # Skip this value since it's blocked

            # Check for exact matches
            if any(match.lower() == value.lower() for match in possible_matches):
                mapped_dict[key] = value
                break
            
            # Check if this is a single-letter key (like 'u', 'v', 'w', or 's')
            if len(key) == 1:
                # Ensure the key appears only at the start or end of the value string with an underscore
                if value.lower().startswith(f"{key.lower()}_") or value.lower().endswith(f"_{key.lower()}"):
                    mapped_dict[key] = value
                    break
            else:
                # Check for matching using synonyms and the key itself
                if any(match.lower() in value.lower() for match in possible_matches):
                    mapped_dict[key] = value
                    break
    
    return mapped_dict



def _get_var_mapping(column_names:list,provided_map:None|dict=None) -> dict:
    """
    Create variable mapping from DataFrame columns.

    To add a new default variable:

    Add the variable name to keys and add any synonyms or blocklists that may exist to their respective dictionaries

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing data columns

    Returns
    -------
    dict
        Mapping of standard variable names to DataFrame columns
    """
    keys = ['lat', 'lon', 'depth', 'time', 'temperature', 'salinity', 'density', 'u', 'v','w', 'speed','cdom','chlor','turbidity','oxygen','buoyancy_frequency']
    values = column_names
    synonyms = {
        'depth': ['pressure', 'pres'],
        'temperature': ['temp', 'temperature_measure'],
        'salinity': ['salt', 'salinity_level'],
        'density': ['density_metric', 'rho','dens'],
        'u': ['eastward_velocity', 'u_component', 'u_current', 'current_u'],
        'v': ['northward_velocity', 'v_component', 'v_current', 'current_v'],
        'w': ['downward_velocity','upward_velocity','w_component', 'w_current', 'current_w'],
        's': ['combined_velocity','velocity','speed', 's_current', 'current_s'],
        'cdom': ['cdom_concentration','cdom_concentration_measure','sci_flbbcd_cdom_units'],
        'chlor': ['chlorophyll_concentration','chlorophyll_concentration_measure','sci_flbbcd_chlor_units'],
        'turbidity': ['turb','turbidity_measure','turbidity_units','turbidity','sci_flbbcd_bb_units'],
        'oxygen': ['oxy','oxygen'],
        'buoyancy_frequency': ['buoyancy_frequency_measure','buoyancy_frequency','buoyancy_frequency_units'],
    }
    blocklist = {
        's': ['sound','pres'],
        'lat':['platform']
    }

    mapped_variables = _map_variables(keys, values, synonyms, blocklist)
    
    # Update the mapping with provided values
    if provided_map is not None:
        mapped_variables.update(provided_map)

    return mapped_variables

def interp_glider_lat_lon(ds: xr.Dataset) -> xr.Dataset:
    """
    Interpolate all glider data variables that use m_time as their dimension.

    Parameters
    ----------
    ds : xarray.Dataset
        Dataset containing glider data

    Returns
    -------
    xarray.Dataset
        Dataset with all m_time variables interpolated to time dimension
    """
    # Convert time and m_time to float64 for interpolation
    new_time_values = ds['time'].values.astype('datetime64[ns]').astype('float64')
    new_mtime_values = ds['m_time'].values.astype('datetime64[ns]').astype('float64')

    # Create a new dataset to store interpolated values
    new_ds = ds.copy()

    # Find all variables that have m_time as a dimension
    mtime_vars = [var for var in ds.data_vars if 'm_time' in ds[var].dims]

    # Interpolate each variable
    for var in mtime_vars:
        valid_data = ~np.isnan(ds[var].values)
        new_ds[var] = xr.DataArray(
            np.interp(new_time_values, new_mtime_values[valid_data], ds[var].values[valid_data]),
            [('time', ds['time'].values)]
        )

    # Drop the m_time coordinate
    new_ds = new_ds.drop_vars('m_time')

    return new_ds


def _process_custom_vars(vars_to_add: str | list[str], data_source) -> dict:
    """
    Process custom variables from data source into Variable objects.

    Parameters
    ----------
    vars_to_add : str | list[str]
        Variable name(s) to process from data source
    data_source : pd.DataFrame | xr.Dataset
        Source data containing the variables

    Returns
    -------
    dict
        Dictionary of processed Variable objects
    """
    if isinstance(vars_to_add, str):
        vars_to_add = [vars_to_add]
    
    custom_vars = {}
    for var in vars_to_add:
        if isinstance(data_source, pd.DataFrame):
            if var in data_source.columns:
                custom_vars[normalize_string(var)] = Variable(
                    values=data_source[var].values,
                    name=normalize_string(var)
                )
        elif isinstance(data_source, xr.Dataset):
            if var in data_source.variables:
                custom_vars[normalize_string(var)] = Variable(
                    values=data_source[var].values,
                    name=normalize_string(var)
                )
    return custom_vars



def data_from_df(df: pd.DataFrame, mapped_variables: dict | None = None, custom_vars: str | list[str] | None = None, **kwargs):
    """
    Create Data object from DataFrame with optional custom variables.

    Parameters
    ----------
    df : pandas.DataFrame
        Source DataFrame
    mapped_variables : dict, optional
        Custom variable mapping
    custom_vars : str | list[str], optional
        Additional variable name(s) to include from DataFrame
    ``**kwargs`` : dict
        Additional arguments for Data initialization

    Returns
    -------
    Data
        Initialized Data object
    """
    mapped_variables = _get_var_mapping(df.columns.tolist(), mapped_variables)
    mapped_variables = {key: df[value] for key, value in mapped_variables.items() if value is not None}
    
    data = Data(**mapped_variables, **kwargs)
    
    if custom_vars:
        custom_variables = _process_custom_vars(custom_vars, df)
        for var_name, var_obj in custom_variables.items():
            data.add_custom_variable(var_obj, exist_ok=True)
    
    return data



def data_from_csv(filename:str,mapped_variables:dict|None=None,custom_vars: str | list[str] | None = None,**kwargs):
    """
    Create Data object from CSV file.

    Parameters
    ----------
    filename : str
        Path to CSV file
    mapped_variables : dict, optional
        Custom variable mapping
    custom_vars : str | list[str], optional
        Additional variable name(s) to include from DataFrame
    ``**kwargs``
        Additional arguments for Data initialization

    Returns
    -------
    Data
        Initialized Data object
    """
    df = pd.read_csv(filename)

    data = data_from_df(df,mapped_variables=mapped_variables,custom_vars=custom_vars,**kwargs)

    return data


def data_from_ds(ds: xr.Dataset, interp_glider: bool = False, mapped_variables: dict | None = None, custom_vars: str | list[str] | None = None, **kwargs):
    """
    Create Data object from xarray Dataset with optional custom variables.

    Parameters
    ----------
    ds : xarray.Dataset
        Input dataset to convert
    interp_glider : bool, optional
        Whether to interpolate glider positions
    mapped_variables : dict, optional
        Dictionary mapping variable names to dataset variables
    custom_vars : str | list[str], optional
        Additional variable name(s) to include from Dataset
    ``**kwargs`` : dict
        Additional arguments for Data initialization

    Returns
    -------
    Data
        New Data object containing the dataset variables
    """
    if interp_glider:
        ds = interp_glider_lat_lon(ds)
    
    mapped_variables = _get_var_mapping(ds.variables.keys(), mapped_variables)
    mapped_variables = {key: ds[value].values for key, value in mapped_variables.items() if value is not None}
    
    data = Data(**mapped_variables, **kwargs)
    
    if custom_vars:
        custom_variables = _process_custom_vars(custom_vars, ds)
        for var_name, var_obj in custom_variables.items():
            data.add_custom_variable(var_obj, exist_ok=True)
    
    return data


def data_from_netcdf(filename: str, mapped_variables: dict | None = None, interp_glider: bool = False,custom_vars: str | list[str] | None = None, **kwargs):
    """
    Create Data object from NetCDF file.

    Parameters
    ----------
    filename : str
        Path to NetCDF file
    mapped_variables : dict or None, optional
        Dictionary mapping variable names to dataset variables  
    interp_glider : bool, optional
        Whether to interpolate glider lat/lon positions
    custom_vars : str | list[str], optional
        Additional variable name(s) to include from Dataset
    ``**kwargs``
        Additional keyword arguments passed to Data constructor

    Returns
    -------
    Data
        New Data object containing the NetCDF variables
    """
    ds = xr.open_dataset(filename)
    data = data_from_ds(ds, interp_glider=interp_glider, mapped_variables=mapped_variables,custom_vars=custom_vars, **kwargs)
    return data

