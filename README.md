# Aerosol Optical Depth and Hyperspectral Imaging

### Mathematical Definition of Aerosol Optical Depth (AOD)
In essence, aerosol optical depth is the measurement of various aerosols within a given atmospheric vertical column. Semantic definitions can differ slightly depending on whether the sensing instrument is located on Earth's surface or above in a low-earth-orbit satellite. To be precise, AOD is the natural logarithmic *ratio* of incident to [transmitted radiant power](https://goldbook.iupac.org/terms/view/A00028) through a given wavelength sample. It is not to be considered in terms of dimensionality/area. It has also been described as unit-less extinction coefficient that varies based on the given wavelength. 

The first logical step in [generating AOD](https://aeronet.gsfc.nasa.gov/new_web/PDF/afi.pdf) is through the Beer-Lambert-Law.

$$V(\lambda) = V_o(\lambda)d^2 exp[-t(\lambda)_{TOT} * m]$$

V is the voltage at the specific wavelength $$\lambda$$, while $$V_o$$ is the voltage from space multiplied against the ratio of actual earth to sun distance. Most importantly $$t_{TOT}$$ is the total optical depth and m represents the air mass.

With the goal of extracting information solely targeting aerosol content, several other atmospheric elements need to subtracted from the initial *total* measurement. From the total value the following componenents are substracted: water vapor, Rayleigh sky scattering, oxygen, carbon dixoide, nitrogen dixoide, and methane. This gives us the final total aerosol measurement for the given wavelength. 

Finally, we consider the *angstrom parameter*. This will allow us to discern the size distribution of aerosol in our results. If we take the first derivative of the logarithmic ratio of the above aerosol *total* measurement and the given wavelength we get the target angstrom parameter, typically referred to as $$\alpha$$. Values of $$\alpha$$ $$\gt$$ 2.0 show us finer particulates, while $$\alpha$$ being close to zero alerts us to the presence of coarse particulates. Within the field, the angstrom parameter is also called aerosol particle size parameter (APSP). APSP ultimately formalizes the dependence of AOD on wavelength. 


#### Practical Uses
Aerosol optical depth is indispensable regarding matters of climate data and analysis—especially if we want to make statements regarding the overall aerosol effect on climate. This epistemological goal requires a formal method to distinguish natural and anthropogenic aerosols. The spatial distribution discerned from aerosol optical depth as well as the separation of particle size from the angstrom parameter is optimal for these types of statements. Furthermore, AOD data gathered via remote sensing allows the collection of concrete evidence supporting claims that entities are emitting pollutants into the atmosphere. For example, the [burning of biomass](https://aeronet.gsfc.nasa.gov/new_web/PDF/1999JD900923.pdf) in the context of agriculture practices could be monitored and analyzed after the fact via AOD collection. 


#### Satellite Measurement Considerations and Resolution

Satellite measurement of aerosol optical depth gives us all the benefits of *remote sensing* of data and can be enhanced by auxiliary on site scientific data collected on land. For traditional AOD algorithms, we will concern ourself just with optical sensing versus other modalities that can be measured via satellite. In the context of satellites, we need to introduce some specific vernacular to clarify mission requirements. Specifically *resolution* refers to a class of characteristics to describe the nature and integrity of our data. 

Out of the various types of resolution (spatial, temporal, spectral, radiometric), temporal resolution is integral to ensuring fidelity of the AOD capture. Temporal resolution is the interval of satellite overflights. For the AOD algorithm, sun reflectance is a key component so the temporal resolution would ideally be fitted for the mission requirements. For goals described in the practical uses section, revisiting the same global area is most likely needed for salient scientific observations. The reliance on solar radiation characterizes the AOD remote sensing approach as *passive* instead of *active*.

Spatial resolution of the eventual pixel dimensions informs the general AOD algorithm below regarding the coefficient look up tables. The actual location/geometry of the satellite has a fundamental role in the spatial resolution. The [vertical nadir](https://darktarget.gsfc.nasa.gov/algorithm-intro) is the space directly below the satellite. If sensor information extends beyond the direct nadir, pixel overlap occurs as well as distortion. In order to be efficient with bandwidth this extraneous data can be chosen not be aggregated. 

[Radiometric resolution](https://www.usgs.gov/faqs/what-radiometric-resolution) technical details are sensor specific and illustrate the overall greyscale value range. The higher the bit depth, the higher precision of floating point pixel values of they greyscale image.

Specifics regarding spectral resolution will be discussed below on the topic of the hyperspectral imager setup.

#### General Algorithm
AOD gathered from a satellite follows a predetermined algorithm. First the type of on-board sensor is detected Advanced Baseline Imager [(ABI)](https://www.earthdata.nasa.gov/data/instruments/abi) or Visible Infrared Imaging Radiometer Suite [(VIIRS)](https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/).The appropriate coefficients are retrieved from a look up table. All algorithmic decisions made are informed by external geolocation and appropriate weather data as well as spatial resolution of the pixels. Next, memory is then allocated for the input pixel. Using the cumulative data and mask strategies the pixel is identified as either a land or water pixel if the conditions are right. 
*Dark Target* is the specific name for land retrieval whilst *Deep Blue* is for water pixels. From the look up table, atmospheric or sun glint strategies fork the algorithm for accurate AOD retrieval/calculation. Quality is then screened for the pixels samples. Artifacts like cirrus clouds, snow/ice, sun glint and shallow water have a direct effect on the confidence of the observed AOD data. Finally, the output value of the pixel is recorded and the algorithmic loop starts over again the input pixel stage. 


### Hyperspectral Imaging
#### Overview 
Hyperspectral imaging approximates the continuous electromagnetic spectrum  with the collection of many bands and very low bandwidth in the nanometers. The granularity of hyperspectral imagers allow us to detect specific material signatures. Processing and identification of these material signatures typically involve use of deep learning classification methods and [signature library](https://www.mathworks.com/help/images/classify-hyperspectral-image-using-sam-metric.html) datasets. 

Generally, the output of hyperspectral imagers is a datacube (usually an ENVI file), with a dimensionality of $$_/Rp$$ (p represents the number of bands, spectral channels, and pixel lat/long dimensions). Metadata regarding the sensor settings can also be embedded into the eventual output of the datacube in the form of a header .dat extension. Typical image processing approaches (greyscale reduction and operations solely on the RGB channels) do not even begin cover the problemspace of hyperspectral image analysis. 

From a mission perspective, this high dimensionality can pose problems for storage constraints on-board the satellite. It could be advantageous to maximize [feature extraction](https://arxiv.org/abs/2003.02822) to reduce the data density and lean on machine learning method for the post process image data classification. The images are reduced in dimensionality via typical PCA (Principal Component Analysis) and ICA (Independent Component Analysis) image segmentation methods for feature extraction.
However, relying solely on this approach for processing hyperspectral imagery (HSI) comes with clear disadvantages. We lose lose fidelity of the original data cube and suffer the consequences of a lack of classification/training data sets in the scientific community given the complexity of the task.

Alternatively, there is existing [methodological research](https://ieeexplore.ieee.org/document/8296399) for maintaining the high dimensionality of HSI. Specifically we can use *voxel storage*. Voxels are volumetric data structures for image storage. Instead of per pixel context the local spatial context is preserved in the volumetric form. Combined with contemporary stacked auto-encoder transformers within machine learning we can balance the tradeoff between maintaining data fidelity and the efficiency of computer vision. Technical details will be expanded upon further below for voxel-based solutions. 

####  Mission Requirements
Given we are operating a CubeSat nanosatellite, efficient design and testing of the overall [payload optical system](https://doi.org/10.1364/AO.476978) is obviously paramount. Full simulations are necessary for ensuring to robustness of the optical system. We can use physical ray tracing techniques like [(OSLO)](https://lambdares.com/oslo/) for quality control of the optical system. [OpenVDB](https://www.openvdb.org/about/) as a file format for hyperspectral imagery offers clear advantages given its optimized/designed for computer graphics applications. The MATLAB environment is ideal for testing closed simulation system, especially considering the power system constraints. Communication latency and data compression strategies is also mission critical and will need specialized teams and testing to ensure mission success.

### Code 
From a purely practical standpoint, it seems like there are two distinct routes we can go regarding the post-processing of the collected data. We are presented with the choice of MATLAB's [hyperspectral imaging tools](https://www.mathworks.com/help/images/hyperspectral-image-processing.html) and the [spectral python module](https://www.spectralpython.net/) (SPy). 

SPy is easily accessible with clear documentation and open source code. Any python code has the added advantage of utilizing other modules in the given programming environment for data shaping and analysis. MATLAB's toolbox on the other hand requires an active license and is best expressed inside the application with Mathwork's proprietary scripting language. However, the MATLAB suite is more user friendly for non-programmers. It also has robust testing setups for closed systems. Thankfully for the time-being licensing is a non-issue given our institutional status. At the moment, we can avoid the liscense quandary altogether, but there is still the open question of inteleaving these two approaches (SPy and MATLAB).
 
Thankfully, it is completely possible to use the MATLAB engine within our python scripts and embed calls to MATLAB's image processing toolbox as needed. This strategy gives us flexibility if we run into features not available in either environment. For further information find a working example in the hyperspectral.py script in this repository.

For machine learning purposes and for spectral signature classification we can also go the route of using [OpenCV's C++ API](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html). This approach is ideal for performance purposes, given the density of hyperspectral data. OpenCV has a multitude of feature extraction functionalities and is as low-level as you can get regarding data bit level data manipulation. Also, if need to conform our code to the hardware we are using (i.e. vectorization) OpenCV is the way to go. Furthermore, it has a huge community of contributors and industry professionals in the computer vision field. Novelly, regarding the adoption of the voxel data approach, we could look into OpenVDB. OpenVDB is designed for constant-time random and sequential access to voxels (i.e. it's very fast). The API also exposes various topological operations for masking and data shaping that could directly serve our image processing pipeline. 



#### Resources

