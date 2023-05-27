import folium
import json
import time

with open("metrodf.geojson") as f:
    track_data = json.load(f)


if __name__ == '__main__':
    m = folium.Map(location=(-15.835545964034853, -47.991309216590565), zoom_start=12,min_zoom=10,
                   min_lat=-16.053137204879715, max_lat=-15.483138831894765,
                   min_lon=-48.236550163323095, max_lon= -47.35429081565683,
                   max_bounds=True)
    a = [[-47, -15], [-47.8, -15.7]]
    folium.PolyLine(a, color='red',weight=3).add_to(m)
    for feature in track_data['features']:
        if feature['geometry']['type'] == 'LineString':
            # Get the coordinates of the LineString geometry
            coords = feature['geometry']['coordinates']
            swapped_coords = [[coord[1], coord[0]] for coord in coords]
            print(swapped_coords)

            colour = feature["properties"]["colour"]
            line_thickness = 4 if feature["properties"]["ref"] == "Verde" else 3

            folium.PolyLine(swapped_coords, color=colour, weight=line_thickness, opacity=1).add_to(m)

    m.save("index.html")
    print("A")