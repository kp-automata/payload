# Aerosol Optical Depth and Hyperspectral Imaging

### Defintion of Aerosol Optical Depth (AOD)
In essence, aerosol optical depth is the measurement of various aerosols within a given atmospheric vertical column. Specific definitions can 
differ slightly depending on whether the sensing instrument is located on Earth's surface or above in a low-earth-orbit satellite. Notably, AOD is the natural logarithmic *ratio* of incident to transmitted radiant power through a given wavelength sample. It is not to be considered in terms of dimensionality/area. 

The first logical step in generating AOD is through the Beer-Lambert-Law.

$$V_{\lambda} = V$$



With the goal of extracting information solely targeting aerosol content, several other atmospheric elements need to subtracted from the initial
*total* measurement. 


Finally, we consider the *angstrom parameter*. This will allow us to discern the size distribution of aerosol in our results. If we take the first derivative of the logarithmic ratio of the above aerosol *total* measurement and the given wavelength we get the target angstrom parameter, typically referred to as $$\alpha$$. Values of $$\alpha$$ $$\gt$$ 2.0 show us finer particulates, while $$\alpha$$ being close to zero alerts us to the presence of coarse particulates. 


#### Practical Uses
- climate data/analysis


- correcting satellite images


#### Satellite Measurement 


### Hyperspectral Imaging
#### Overview 

####  Mission Requirements

### Code 
At first glance it seems like there are two distinct routes we can go regarding post-processing of the collected data. We are presented with the choice between MATLAB's [hyperspectral imaging tools](https://www.mathworks.com/help/images/hyperspectral-image-processing.html)or the [spectral python module](https://www.spectralpython.net/) (SPy). However, this is a false dichotmy because we can actually use MATLAB's python engine to embedded calls to MATLAB's API. 


#### Resources

