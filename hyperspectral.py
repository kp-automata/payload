""" Example script on how to start matlab engine instance
and interwave spectral python and matlab hyperspectral image
toolbox source code.

Requires valid matlab license instance. For additional
requirements see requirements.txt

https://gitlab.citius.gal/hiperespectral/ChangeDetectionDataset
"""
import matlab.engine



def main():
    # Start matlab engine
    core = matlab.engine.start_matlab()

    # Sample data
    first = "BayArea2013PV.raw"
    second = "BayArea2015PV.raw"

    # Example code on how to detect change overtime for a given
    # hyperspectral image raw data set using MATLAB hyperspectral imaging toolbox.
    matlab_code = f"""

    datacube_2013 = hypercube({first})
    datacube_2015 = hypercube({second})
    windowSize = 7;

    changeMap(datacube_2013, datacube_2015, windowSize)

    function changeMap = changeDetection(imageData1, imageData2, windowSize)
        % Get the center of window.
        centerPixel = ((windowSize-1)/2);

        % Get the size of the input data.
        [row,col,~] = size(imageData1);

        if isinteger(imageData1)
            imageData1 = single(imageData1);
            imageData2 = single(imageData2);
        end

        % Apply zero padding to handle the edge pixels.
        imageData1 = padarray(imageData1,[centerPixel centerPixel],0,"both");
        imageData2 = padarray(imageData2,[centerPixel centerPixel],0,"both");

        % Initialize the change map output.
        changeMap = zeros(row,col);

        for r = (centerPixel + 1):(row + centerPixel)
            for c = (centerPixel + 1):(col + centerPixel)
                rowNeighborhood = (r - centerPixel):(r + centerPixel);
                colNeighborhood = (c - centerPixel):(c + centerPixel);
                % Find the Euclidean distance between the reference signature and
                % the neighborhood of the target signature.
                spectra1 = reshape(imageData1(r,c,:),1,[]);
                spectra2 = reshape(imageData2(rowNeighborhood,colNeighborhood,:), ...
                    windowSize*windowSize,size(imageData1,3));
                a = min(pdist2(spectra1,spectra2));
                % Find the Euclidean distance between the target signature and
                % the neighborhood of the reference signature.
                spectra1 = reshape(imageData2(r,c,:),1,[]);
                spectra2 = reshape(imageData1(rowNeighborhood,colNeighborhood,:), ...
                    windowSize*windowSize,size(imageData1,3));
                b = min(pdist2(spectra1, spectra2));
                % Store the pixel-wise results in the change map.
                changeMap(r - centerPixel,c - centerPixel) = max(a,b);
            end
        end
    end
    """
    core.eval(matlab_code, nargout=0)

if __name__ == "__main__":
    main()
