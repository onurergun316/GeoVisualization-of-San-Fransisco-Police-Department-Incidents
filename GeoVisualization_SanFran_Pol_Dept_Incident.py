import numpy as np
import pandas as pd 
import folium

# importing csv file that contains PD incidents for the City San Fransisco
incidents = pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')

# limiting the incidents records to 100 lines
limit = 100
incidents = incidents.iloc[0:limit, :]

# San Francisco's latitude and longtitude values
latitude = 37.77
longtitude = -122.42

# Creating the Incidents Map of San Fransisco
map_san_fransisco = folium.Map(location = [latitude, longtitude], zoom_start = 12)

# Imposing the locations of crimes on to the map
sanf_incidents = folium.map.FeatureGroup()

# looping through 100 incidents that we limited
for lat,lng in zip(incidents.Y,incidents.X):
    sanf_incidents.add_child(
        folium.CircleMarker(
            [lat,lng],
            radius = 5,
            color = 'yellow',
            fill = True,
            fill_color = 'red',
            fill_opacity = 0.6
        )
    )
# adding pop-up text(info) to incidents on the map 
latitudes = list(incidents.Y)
longtitudes = list(incidents.X)
labels = list(incidents.Category)

for lat, lng, label in zip(latitudes,longtitudes,labels):
    folium.Marker([lat, lng], popup=label).add_to(map_san_fransisco)
    
# applying incidents to the map
map_san_fransisco.add_child(sanf_incidents)
map_san_fransisco.save("san_fransisco_incidents.html")