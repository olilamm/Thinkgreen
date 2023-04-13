import folium  

class Map(folium.Map):

    def __init__(self, center=[20, 0], zoom=2, **kwargs) -> None:
        
        super().__init__(location=center, zoom_start=zoom, **kwargs)