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

## Customize map controls

```python
m = thinkgreen.Map()
```