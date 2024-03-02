import webbrowser
import folium
import geopandas
import requests

#code example from offical pages
#https://www.digitraffic.fi/tuki/koodiesimerkit/#junat-kartalla

train_locations_url = "https://rata.digitraffic.fi/api/v1/train-locations.geojson/latest"
headers = {"Digitraffic-User": "Junahenkilö/FoobarApp 1.0", "Accept-Encoding": "gzip"}
trains = requests.get(train_locations_url, headers=headers).text

trains_gdf = geopandas.read_file(trains)
print(trains_gdf)



class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    
    def showMap(self,dataset):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)


        for index, train in dataset.iterrows():
            marker_color = "red" if train.speed == 0 else "green"
  
        map.add_child(
            folium.Marker(
                location=(train.geometry.y, train.geometry.x),
                popup="Train number: " + str(train.trainNumber),
                icon=folium.Icon(color="%s" % marker_color),
            )
        )

        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")

coords = [62.2426, 25.7473]
map = Map(center = coords, zoom_start = 6)
map.showMap(trains_gdf)




