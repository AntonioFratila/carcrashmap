import folium, pandas

data = pandas.read_csv("MOCK_DATA.csv")
lat = list(data["LAT"])
lon = list(data["LONG"])
loc = list(data["Locatie"])
fat = list(data["Fatalitate"])
c_id = list(data["Numar de inmatriculare"])
sex = list(data["Sex"])

for strd, ni, sx in zip(loc, c_id, sex):
    info = strd + ", " + ni + ", " + sx
map = folium.Map(location=[44.452885, 26.130770], zoom_start=6,)

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup=info, icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Map1.html")

