# img2csv

In order to analyze individual evaluations using image data 
who can provide reliable evaluations or who cannot, the following prcesses are needed:
1.All image files should be resized and converted to the same size of images.
2.For machine learning, resized image data should be converted to a single csv file.

# imgresize.py for resizing image files to image files with the same width and height.

imgresize.py is used to resize an image file to an image file of the same width and height.

$ python imgresize.py size=128 sdir="./photo" ddir="./newphoto"

size of width=height, source directory and destination directory must be given to imgresize.py


