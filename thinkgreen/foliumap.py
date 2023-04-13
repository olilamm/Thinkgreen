import folium 

class Map(folium.Map):

    def __init__(self, center=[20, 0], zoom=2, **kwargs) -> None:
        
        super().__init__(location=center, zoom_start=zoom, **kwargs)

    def add_tile_layer(self, url, name, attribution="", **kwargs):
            """Adds a tile layer to the map.
            Args:
                url (str): The URL template of the tile layer.
                attribution (str): The attribution of the tile layer.
                name (str, optional): The name of the tile layer. Defaults to "OpenStreetMap".
                kwargs: Keyword arguments to pass to the tile layer.

            Returns: 
                ipyleaflet.TileLayer: Adds a new layer to the map.
            """
            tile_layer = folium.TileLayer(
                url=url, 
                attr=attribution, 
                name=name, 
                **kwargs)
            self.add_child(tile_layer)