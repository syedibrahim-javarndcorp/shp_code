# import geopandas as gpd
import pandas as pd
# df = gpd.read_file('shp/E/E_map.shp')
# print(df)
# csv = df.to_csv("cv.csv")



# import pandas as pd
import pandas as pd
  

with open("E1.txt","r") as file:
    df = pd.DataFrame(file)
    with open("dat.csv","a") as f:
        f.writelines(df.to_string())
        
