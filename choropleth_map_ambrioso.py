#  https://plotly.com/python/mapbox-county-choropleth/
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

#  This is what the json data looks like
print(counties["features"][0])


df = pd.read_csv("https://raw.githubusercontent.com/kjhealy/fips-codes/master/state_and_county_fips_master.csv")


df_FL = df[df['state'] == 'FL']
print(df_FL.reset_index(drop=True))

county_list = ['Hillsborough County', 'Manatee County', 'Brevard County', 'Sarasota County', 'Alachua County']

for county in county_list:
  print(df_FL[df_FL['name'] == county])

fips_list = [12057, 12081, 12009, 12115]
county_dict = dict(zip(county_list, fips_list))
print(county_dict)


# Generate result using pandas 
result = [] 
for value in df_FL['fips']: 
    if value == 12057:
        result.append(8)
    elif value ==12001:
      result.append(1) 
    elif value == 12081:
      result.append(2)
    elif value == 12009: 
        result.append(1)
    elif value == 12115:
        result.append(1)
    else:
      result.append(0)

df_FL["ambriosos"] = result    
print(df_FL) 


st = {"FL":(27.6648,-81.5158)}

fig = px.choropleth_mapbox(df_FL, geojson=counties, locations='fips', color='ambriosos',
                           color_continuous_scale="Viridis",
                           range_color=(0, 8),
                           mapbox_style="carto-positron",
                           # zoom=3, center = {"lat": 37.0902, "lon": -95.7129}, # for US
                           zoom=5.5, center = {"lat": 27.8, "lon": -84}, # for Florida (28.3232, -82.4319)
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Can use the renderer variable to get other out for example "png".
# See https://plotly.com/python/renderers/ for more information.
    
fig.show(renderer="browser")  
