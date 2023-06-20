# shp_code
This code is to extract the locations(latitude and longitutde) or X and Y co-ordinates from a shape(.shp) file.
Give the relative path of the .shp or .dbf file to extract.
The output will be in txt format with two columns, latitude and longitude respectively.


This script reads a shapefile using the shapefile module and extracts the shapes and points from it. The script also writes the extracted points to a text file called 'location.txt'. 

The code reads the shapefile path from the 'shp_path' variable, which is expected to be a string. The script verifies that the file exists using the `os.path.exists()` function. If the file exists, the script reads the file using `shapefile.Reader()` and extracts the shapes using the `.shapes()` method.

The script then iterates through each shape and extracts the points using a nested for-loop. Finally, the script writes each point to a text file using the `open()` function with the 'a' flag to append to the file.

This script assumes that the shapefile contains valid shape data, and that the output file 'location.txt' is suitable for your particular use case.

