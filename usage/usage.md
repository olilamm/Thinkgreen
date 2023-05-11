# Usage

You can try out leafmap by using Google Colab [![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/olilamm/thinkgreen/blob/main/docs/examples/thinkgreen.ipynb) 

## To use thinkgreen in a project:

```
import thinkgreen
```

## Create an interactive map

```python
m = thinkgreen.Map(center = [36, -84], zoom = 10)

m
```
## Another way to create an interactive map

```python
import folium

m = folium.Map(location =[36, -84], zoom_start=10)

m
```
## Customize base layers

```python
m = thinkgreen.Map(center = [36, -84], zoom = 10)
m.add_search_control(position="topright")
m.add_layers_control()
m.add_tile_layer(url=url, name="Google Maps", attribution="Google")
m.add_basemap(basemap="satellite")

m
```

## Customize basemaps

```python
m = thinkgreen.Map()

m.add_toolbar()

m
```

## Adding different types of graphs

```python
m = thinkgreen.Map() 

m.add_bar(x=[1,2,3,4], y=[1,2,3,4])

m.add_pie(x=[1,2,3,4])

m.add_plot(x=[1,2,3,4], y=[1,2,3,4])
```

## Add Shapefiles or GeoJSON layers

```python
m = thinkgreen.Map()

m.add_shp("filename")

m.add_geojson("filename")
```
