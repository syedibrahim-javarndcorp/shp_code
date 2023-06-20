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

        with open("location.txt","w") as file:
            file.write(str(point))
            file.write("\n")