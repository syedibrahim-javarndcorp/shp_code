import shapefile    
import os

shp_path = r"shp\shape.shp"
assert os.path.exists(shp_path)
sf = shapefile.Reader(shp_path)

shapes = sf.shapes()
print("===================================================================")
print(shapes)
print("===================================================================")

r = len(shapes)

print("===================================================================")
print(r)
print("===================================================================")

for i in range(r):
    for point in shapes[i].points:
        print(point)







# import shapefile

# # Open the shapefile
# sf = shapefile.Reader(r"shp\shape.shp")

# # Get the first feature (assuming there is only one)
# feature = sf.shapeRecords()[0]

# # Get the shape object
# shape = feature.shape

# # Extract the coordinates from the shape object
# coordinates = [(i[0], i[1]) for i in shape.points]

# # Output the coordinates
# print(coordinates)