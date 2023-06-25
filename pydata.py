# import pandas as pd

# with open("E.txt","r") as data:


# # Create a list of dictionaries for the latitude and longitude values
#     lat_lon = []
#     for row in data.split('\n'):
#         if row:
#             lat, lon = row.split(', ')
#             lat_lon.append({'Latitude': lat, 'Longitude': lon})

#     # Create a pandas dataframe using the list of dictionaries
#     df = pd.DataFrame(lat_lon)

# # Print the dataframe
# print(df.head())






import pandas as pd

data = pd.read_csv('E1.csv')

