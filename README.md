# Aerosol Optical Depth and Hyperspectral Imaging

### Mathematical Definition of Aerosol Optical Depth (AOD)
In essence, aerosol optical depth is the measurement of various aerosols within a given atmospheric vertical column. Specific definitions can 
differ slightly depending on whether the sensing instrument is located on Earth's surface or above in a low-earth-orbit satellite. Notably, AOD is the natural logarithmic *ratio* of incident to transmitted radiant power through a given wavelength sample. It is not to be considered in terms of dimensionality/area. It has also been described as unit-less extinction coefficient that varies based on the given wavelength. 

The first logical step in generating AOD is through the Beer-Lambert-Law.

$$V_{\lambda} = V$$



With the goal of extracting information solely targeting aerosol content, several other atmospheric elements need to subtracted from the initial
*total* measurement. 


Finally, we consider the *angstrom parameter*. This will allow us to discern the size distribution of aerosol in our results. If we take the first derivative of the logarithmic ratio of the above aerosol *total* measurement and the given wavelength we get the target angstrom parameter, typically referred to as $$\alpha$$. Values of $$\alpha$$ $$\gt$$ 2.0 show us finer particulates, while $$\alpha$$ being close to zero alerts us to the presence of coarse particulates. In the field, the angstrom parameter is also called aerosol particle size parameter (APSP). APSP ultimately formalizes the dependence of AOD on wavelength. 


#### Practical Uses
Aerosol optical depth is indispensable regarding matters of climate data and analysis--especially if we want to make statements regarding the overall aerosol effect on climate. This goal requires a formal method to distinguish natural and anthropogenic aerosols. The spatial distribution discerned from aerosol optical depth as well as the separation of particle size from the angstrom parameter is optimal for these types of statements. Furthermore, AOD data gathered via remote sensing allows the collection of concrete evidence supporting claims that entities are emitting pollutants into the atmosphere. For example, the burning of biomass in the context of agriculture practices could be monitored and analyzed after the fact via AOD collection. 


#### Satellite Measurement Considerations

Satellite measurement of aerosol optical depth gives us all the benefits of 
*remote sensing* of data and can be enhanced by auxiliary on site scientific data collected on land. For traditional AOD algorithms, we are just concerned with optical sensing versus other modalitites. In the context of satellites, we need to introduce a few terms. Specifically *resolution* refers to a class of characteristics to describe the nature and integrity of our data. Temporal resolution is the interval of satellite overflights. For the AOD algorithm, sun reflectance is a key component so the temporal resolution would ideally be fitted for the mission requirements. For goals described in the practical uses section, revisiting the same global area is most likely needed for salient scientific observations. 





##### General Algorithm
AOD gathered from a satellite follows a predetremined algorithm. First the type of sensor is detected

Land (specific name)

Ocean (specific  name)


### Hyperspectral Imaging
#### Overview 
Hyperspectral imaging approximates the continuous spectral with many bands and very low bandwidth nanometers. The granularity of hyperspectral imagers allow us to detect specific material signatures. The output is a datacube, with of a dimensionality of $$_/Rp$$ (p represents the
number of bands, spectral channels, and pixel lat/long dimensions).From a mission perspective, this high dimensionality can pose problems for storage constraints on board the satellite. It might be advantageous to maximize feature extraction to reduce the data density and lean on machine learning method for the post process image data classification. However, this approach for processing hyperspectral imagery (HSI) comes with clear disadvantages. We lose lose fidelity of the original data cube and suffer the consequence of a lack of classification/training data sets in the scientific community.  

Alternatively, there is existing research and methods for maintaining the high dimensionality of HSI via voxel storage. Combined with contemporary transformers in machine learning we can balance the dialectic between data fidelity and the efficiency of computer vision. 

####  Mission Requirements

### Code 
From a purely practical standpoint, it seems like there are two distinct routes we can go regarding the post-processing of the collected data. We are presented with the choice of MATLAB's [hyperspectral imaging tools](https://www.mathworks.com/help/images/hyperspectral-image-processing.html) and the [spectral python module](https://www.spectralpython.net/) (SPy). 

SPy is easily accessiable with clear documentation and open source code. Any python code has the added advantage of utilizing other modules in the given programming eviromment for data shaping and analysis. MATLAB's toolbox on the other hand requires an active lisence and is best expressed inside the application with Mathwork's profpiertary scripting language. However, it is more user friendly for non-programmers. Also liscneing is  a non-issue at our given academic institituion. Thankfully we can avoid this quandry altogether. 
It is completely possible to use the MATLAB engine within our python script and embed calls to MATLAB's image processing toolbox as needed. This gives us flexibility if we run into features not available in either environment. Find a working example in the hyperspectral.py script in this repository.

For machine learning purposes for spectral signature classification we can also go the route of using OpenCV's C++ API. This approach is ideal for performance purposes given the density of hyperspectral data. OpenCV has a multidude of feature extraction functionality like PCA...  
Novelly, regarding voxel data we could look into OpenVDB.



#### Resources

