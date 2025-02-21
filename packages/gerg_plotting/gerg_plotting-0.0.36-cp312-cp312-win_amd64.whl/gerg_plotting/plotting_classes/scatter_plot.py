import matplotlib
import matplotlib.axes
import matplotlib.cm
import matplotlib.figure
import matplotlib.pyplot
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import numpy as np
from attrs import define, field
import cmocean

from gerg_plotting.plotting_classes.plotter import Plotter
from gerg_plotting.modules.calculations import get_sigma_theta, get_density
from gerg_plotting.data_classes.variable import Variable

@define
class ScatterPlot(Plotter):
    """
    Class for creating scatter plots from Data objects.

    Inherits from Plotter class for basic plotting functionality. Provides methods
    for various scatter plot types including T-S diagrams, hovmoller plots, and
    velocity vector plots.
    """

    def scatter(self, x: str, y: str, color_var: str | None = None, invert_yaxis:bool=False, fig=None, ax=None, **scattter_kwargs) -> None:
        """
        Create scatter plot of two variables with optional color mapping.

        Parameters
        ----------
        x : str
            Variable name for x-axis
        y : str
            Variable name for y-axis
        color_var : str or None, optional
            Variable name for color mapping
        invert_yaxis : bool, optional
            Whether to invert y-axis
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        ``**scattter_kwargs``
            Additional arguments for scatter plot (see matplotlib.pyplot.scatter)

        Returns
        -------
        matplotlib.collections.PathCollection
            Scatter plot object
        """
        self.data._check_for_vars([x,y,color_var])
        self.init_figure(fig, ax)  # Initialize figure and axes

        # If color_var is passed
        if color_var is not None:
            if color_var == "time":
                color_data = self.data.date2num()
            else:
                color_data = self.data[color_var].values
            sc = self.ax.scatter(
                self.data[x].values,
                self.data[y].values,
                c=color_data,
                cmap=self.get_cmap(color_var),
                vmin = self.data[color_var].vmin,
                vmax = self.data[color_var].vmax, **scattter_kwargs
            )
            self.add_colorbar(sc, var=color_var)  # Add colorbar

        # If color_var is not passed 
        else:
            sc = self.ax.scatter(self.data[x].values, self.data[y].values, **scattter_kwargs)

        self.format_axes(xlabel=self.data[x].label,ylabel=self.data[y].label,invert_yaxis=invert_yaxis)

        return sc
    
    def scatter3d(self, x: str, y: str, z:str, color_var: str | None = None, invert_yaxis:bool=False, fig=None, ax=None, **scattter_kwargs) -> None:
        """
        Create scatter plot of two variables with optional color mapping.

        Parameters
        ----------
        x : str
            Variable name for x-axis
        y : str
            Variable name for y-axis
        color_var : str or None, optional
            Variable name for color mapping
        invert_yaxis : bool, optional
            Whether to invert y-axis
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        ``**scattter_kwargs``
            Additional arguments for scatter plot (see matplotlib.pyplot.scatter)

        Returns
        -------
        matplotlib.collections.PathCollection
            Scatter plot object
        """
        self.data._check_for_vars([x,y,color_var])
        self.init_figure(fig, ax, three_d=True)  # Initialize figure and axes

        # If color_var is passed
        if color_var is not None:
            if color_var == "time":
                color_data = self.data.date2num()
            else:
                color_data = self.data[color_var].values
            sc = self.ax.scatter(
                self.data[x].values,
                self.data[y].values,
                self.data[z].values,
                c=color_data,
                cmap=self.get_cmap(color_var),
                vmin = self.data[color_var].vmin,
                vmax = self.data[color_var].vmax, **scattter_kwargs
            )
            self.add_colorbar(sc, var=color_var)  # Add colorbar

        # If color_var is not passed 
        else:
            sc = self.ax.scatter(self.data[x].values, self.data[y].values, self.data[z].values, **scattter_kwargs)

        self.format_axes(xlabel=self.data[x].label,ylabel=self.data[y].label,zlabel=self.data[z].label,invert_yaxis=invert_yaxis)

        return sc   
  
    
    def hovmoller(self, var: str, fig=None, ax=None,**scattter_kwargs) -> None:
        """
        Create depth vs time plot colored by variable.

        Parameters
        ----------
        var : str
            Variable name for color mapping
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        ``**scattter_kwargs``
            Additional arguments for scatter plot (see matplotlib.pyplot.scatter)
        """
        sc = self.scatter(x='time',
                          y='depth',
                          color_var=var,
                          invert_yaxis=True,
                          ax=ax, fig=fig,**scattter_kwargs)
        
        locator = mdates.AutoDateLocator()
        formatter = mdates.AutoDateFormatter(locator)

        self.ax.xaxis.set_major_locator(locator)  # Set date locator for x-axis
        self.ax.xaxis.set_major_formatter(formatter)  # Set date formatter for x-axis
        self.format_axes(xlabel=self.data.time.label,ylabel=self.data.depth.label)

    def _add_contours(self, contour_kwargs):
        """
        Add contours to plot.
        """   
        # Calculate sigma-theta contours
        Sg, Tg, sigma_theta = get_sigma_theta(
            salinity=self.data['salinity'].values,
            temperature=self.data['temperature'].values,
        )
        
        # Default contour settings
        contour_defaults = {
            'colors': 'grey',
            'linestyles': 'dashed',
            'zorder': 1,
            'levels': np.arange(18, 40, 2)
        }
        
        # Update defaults with any user-provided kwargs
        if contour_kwargs:
            contour_defaults.update(contour_kwargs)
 
        cs = self.ax.contour(Sg, Tg, sigma_theta,**contour_defaults)
        matplotlib.pyplot.clabel(cs, fontsize=10, inline=True, fmt='%.1f')  # Add contour labels


    def TS(self, color_var=None, fig=None, ax=None, contours: bool = True, scatter_kwargs=None, contour_kwargs=None) -> None:
        """
        Create temperature-salinity diagram.

        Parameters
        ----------
        color_var : str or None, optional
            Variable name for color mapping
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        contours : bool, optional
            Whether to show sigma-theta contours, default True
        scatter_kwargs : dict, optional
            Additional arguments to pass to scatter plot (see matplotlib.pyplot.scatter)
        contour_kwargs : dict, optional
            Additional arguments to pass to contour plot (see matplotlib.pyplot.contour)
        """
        # Initialize empty dicts if None provided
        scatter_kwargs = scatter_kwargs or {}
        contour_kwargs = contour_kwargs or {}
        
        # Add zorder to scatter kwargs to ensure points appear above contours
        scatter_kwargs['zorder'] = scatter_kwargs.get('zorder', 3)
        
        sc = self.scatter('salinity', 'temperature', color_var=color_var, 
                        fig=fig, ax=ax, **scatter_kwargs)

        if contours:
            self._add_contours(contour_kwargs)

        self.format_axes(xlabel=self.data.salinity.label, ylabel=self.data.temperature.label)
        self.ax.set_title('T-S Diagram', fontsize=14, fontweight='bold')
        self.ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        self.ax.yaxis.set_major_locator(MaxNLocator(nbins=8))


        
    def get_density_color_data(self, color_var: str) -> np.ndarray:
        """
        Get color data for density plotting.

        Parameters
        ----------
        color_var : str
            Variable name for color data

        Returns
        -------
        np.ndarray
            Array of color values
        """
        if color_var == 'density':
            if not isinstance(self.data['density'], Variable):  # If density is not already provided
                color_data = get_density(
                    self.data['salinity'].values,
                    self.data['temperature'].values
                )  # Calculate density from salinity and temperature
            else:
                color_data = self.data[color_var].values
        else:
            color_data = self.data[color_var].values  # Retrieve color data for the specified variable

        return color_data

    def cross_section(self, longitude, latitude) -> None:
        """
        Method placeholder for plotting cross-sections.

        Args:
            longitude: Longitude line for the cross-section.
            latitude: Latitude line for the cross-section.
        
        Raises:
            NotImplementedError: Indicates that the method is not yet implemented.
        """
        raise NotImplementedError('Need to add method to plot cross sections')
    
    def calculate_quiver_step(self,num_points,quiver_density) -> int:
        """
        Calculate step size for quiver plot density.

        Parameters
        ----------
        num_points : int
            Total number of data points
        quiver_density : int
            Desired density of quiver arrows

        Returns
        -------
        int
            Step size for data sampling
        """
        step = round(num_points/quiver_density)
        return step
    
    def quiver1d(self,x:str,quiver_density:int=None,quiver_scale:float=None,fig=None,ax=None) -> None:
        """
        Create 1D quiver plot for velocity data.

        Parameters
        ----------
        x : str
            Variable name for x-axis
        quiver_density : int, optional
            Density of quiver arrows
        quiver_scale : float, optional
            Scaling factor for arrow length
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        """
        self.data.calculate_speed()
        self.data._check_for_vars([x,'u','v','speed'])
        self.init_figure(fig=fig,ax=ax,figsize=(15,5))
        
        # Get the data slice step size using the quiver_density value
        if quiver_density is not None:
            step = self.calculate_quiver_step(len(self.data.u.values),quiver_density)
        elif quiver_density is None:
            step = 1

        # Create the quiver plot
        mappable = self.ax.quiver(self.data[x].values[::step], 0, 
                                        self.data.u.values[::step], self.data.v.values[::step], 
                                        self.data.speed.values[::step], cmap=cmocean.cm.speed,
                                        pivot='tail', scale=quiver_scale, units='height')
        # Add the colorbar
        self.add_colorbar(mappable,'speed')
        self.format_axes(xlabel=self.data[x].label,ylabel=None)
        self.ax.get_yaxis().set_visible(False)

    def quiver2d(self,x:str,y:str,quiver_density:int=None,quiver_scale:float=None,fig=None,ax=None) -> None:
        """
        Create 2D quiver plot for velocity data.

        Parameters
        ----------
        x : str
            Variable name for x-axis
        y : str
            Variable name for y-axis
        quiver_density : int, optional
            Density of quiver arrows
        quiver_scale : float, optional
            Scaling factor for arrow length
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        """
        self.data.calculate_speed()
        self.data._check_for_vars([x,y,'u','v','speed'])
        self.init_figure(fig=fig,ax=ax)

        # Get the data slice step size using the quiver_density value
        if quiver_density is not None:
            step = self.calculate_quiver_step(len(self.data.u.values),quiver_density)
        elif quiver_density is None:
            step = 1

        # Create the quiver plot
        mappable = self.ax.quiver(self.data[x].values[::step], self.data[y].values[::step], 
                                        self.data.u.values[::step], self.data.v.values[::step], 
                                        self.data.speed.values[::step], cmap=cmocean.cm.speed,
                                        pivot='tail', scale=quiver_scale, units='height')
        # Add the colorbar
        self.add_colorbar(mappable,'speed')
        self.format_axes(xlabel=self.data[x].label,ylabel=self.data[y].label)

    def power_spectra_density(self,psd_freq=None,psd=None,
                              var_name:str=None, sampling_freq=None,segment_length=None,theta_rad=None,
                              highlight_freqs:list=None,fig=None,ax=None) -> None:
        """
        Create power spectral density plot.

        Parameters
        ----------
        psd_freq : array-like, optional
            Frequency values
        psd : array-like, optional
            Power spectral density values
        var_name : str, optional
            Variable name for PSD calculation
        sampling_freq : float, optional
            Sampling frequency
        segment_length : int, optional
            Length of segments for PSD calculation
        theta_rad : float, optional
            Angle in radians
        highlight_freqs : list, optional
            Frequencies to highlight
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on

        Raises
        ------
        ValueError
            If neither PSD values nor calculation parameters are provided
        """
        # Check if all variables are None         
        if all(var is None for var in [psd_freq, psd, sampling_freq, segment_length]):
            raise ValueError('You must pass either [psd_freq and psd] or [sampling_freq, segment_length, and theta_rad (optional)]')  
             
        # Calculate the power spectra density
        if psd_freq is None or psd is None:
            self.data.calcluate_PSD(sampling_freq,segment_length,theta_rad)
            
        elif psd_freq is not None and psd_freq is not None:
            self.data.add_custom_variable(Variable(psd_freq,name='psd_freq',units='cpd',label='Power Spectra Density Frequency (cpd)'),exist_ok=True)
            self.data.add_custom_variable(Variable(psd,name=f'psd_{var_name}',units='cm²/s²/cpd',label='Power Spectra Density V (cm²/s²/cpd)'),exist_ok=True)

        self.init_figure(fig=fig,ax=ax)
        self.ax.plot(self.data.psd_freq.values, self.data[f'psd_{var_name}'].values, color='blue')
        self.ax.set_xlabel(self.data.psd_freq.label)
        self.ax.set_ylabel(self.data[f'psd_{var_name}'].label)
        self.ax.set_yscale("log")  # Log scale for PSD
        self.ax.set_xscale("log")  # Log scale for frequency
        self.ax.grid(True, which="both", linestyle="--", linewidth=0.5)
        # Add highlight freqencies
        if highlight_freqs is not None:
            _ = [self.ax.axvline(highlight_freq, color=plt.get_cmap('tab10')(idx), linestyle='--', linewidth=1, label=f'{highlight_freq:.3f} cpd') for idx,highlight_freq in enumerate(highlight_freqs)]
            self.ax.legend()
        self.fig.suptitle(f'Power Spectra Density',fontsize=22)

    def tricontourf(self,x:str,y:str,z:str,fig=None,ax=None,levels=None):
        """
        Create filled contour plot of irregular grid data.

        Parameters
        ----------
        x : str
            Variable name for x-axis
        y : str
            Variable name for y-axis
        z : str
            Variable name for contour values
        fig : matplotlib.figure.Figure, optional
            Figure to plot on
        ax : matplotlib.axes.Axes, optional
            Axes to plot on
        levels : int, optional
            Number of contour levels
        """
        # Check if vars are present
        self.data._check_for_vars([x,y,z])
        self.init_figure(fig=fig,ax=ax)
        self.ax.tricontourf(self.data[x].values,self.data[y].values,self.data[z].values,cmap=self.data[z].cmap,levels=levels)
        self.format_axes(xlabel=self.data[x].label,ylabel=self.data[y].label)





