# imgresize and img2csv

In order to analyze individual evaluations using image data 
who can provide reliable evaluations or who cannot, the following processes are needed:

1.All image files should be resized and converted to the same size of images.

2.For machine learning, resized image data should be converted to a single csv file.

# imgresize.py 

imgresize.py is used to resize an image file to an image file of the same width and height.
"size" determines the size of width or height. 
The width of the image file should be equal to the height.
"sdir" is a source directory. 
"ddir" is a distination directory.
"type" is either gray scale "L" or "RGB" color.

$ python imgresize.py size=128 sdir="./original" ddir="./resized" type="L"

size (width=height), source directory=sdir, destination directory=ddir, 
and type (RGB or L:gray scale) must be given to imgresize.py

# img2csv


