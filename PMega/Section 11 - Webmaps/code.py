import folium
import pandas
import math
import re

data = pandas.read_excel("GVP_Volcano_List.xlsx",header = 1)

map = folium.Map(tiles="Mapbox Bright")
featureGroup = folium.FeatureGroup(name="Volcanoes")

#Debug
dumpfh = open('out.txt', 'w')

lonData = data["Latitude"]
latData = data["Longitude"]
nameData = data["Volcano Name"]
for lon, lat, name, i in zip(lonData, latData, nameData, range(0, len(nameData))):
    if not math.isnan(lon) and not math.isnan(lat):
        #Debug
        dumpfh.write('{i}: {lon} {lat} {name}\n'.format(i=i, lon=lon, lat=lat, name=name))
        dumpfh.flush()
        
        name = re.sub("'", '', name)
        featureGroup.add_child(folium.Marker(location=[lon,lat],popup=str(name),icon=folium.Icon(color="green")))
    
map.add_child(featureGroup)

map.save("VolcanoMap.html")

#Debug
print('finished')
