import shapefile    
import os

file_name = input("Enter the file name with .txt : ")

shp_path = r"shp\D\D.shp"
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

        with open(file_name,"a") as file:
            file.write(str(point))
            file.write("\n")