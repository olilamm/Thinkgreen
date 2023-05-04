import streamlit as st

st.title("Thinkgreen")

st.write("This site is for my final project in Geog 510")

st.text("This is some text")

class Map(ipyleaflet.Map):
    
        def __init__(self, center=[20, 0], zoom=2, **kwargs) -> None:

            if "scroll_wheel_zoom" not in kwargs:
                kwargs["scroll_wheel_zoom"] = True

            super().__init__(center=center, zoom=zoom, **kwargs)

            if "height" not in kwargs:
                self.layout.height = "500px"
            else:
                self.layout.height = kwargs["height"]

            if "fullscreen_control" not in kwargs:
                kwargs["fullscreen_control"] = True
            if kwargs["fullscreen_control"]:
                self.add_fullscreen_control()
            
            if "layers_control" not in kwargs:
                kwargs["layers_control"] = False
            if kwargs["layers_control"]:
                self.add_layers_control()

        def add_search_control(self, position="topleft", **kwargs):
            """Adds a search control to the map.
            Args:
                kwargs: Keyword arguments to pass to the search control.
            
            Returns:
                ipyleaflet.SearchControl: The search control.
            """
            if "url" not in kwargs:
                kwargs["url"] = 'https://nominatim.openstreetmap.org/search?format=json&q={s}'
        

            search_control = ipyleaflet.SearchControl(position=position, **kwargs)
            self.add_control(search_control)

        def add_draw_control(self, **kwargs):
            """Adds a draw control to the map.
            Args:
                kwargs: Keyword arguments to pass to the draw control.
            
            Returns:
                ipyleaflet.DrawControl: Draw control.
            """
            draw_control = ipyleaflet.DrawControl(**kwargs)

            draw_control.polyline =  {
                "shapeOptions": {
                    "color": "#6bc2e5",
                    "weight": 8,
                    "opacity": 1.0
                }
            }
            draw_control.polygon = {
                "shapeOptions": {
                    "fillColor": "#6be5c3",
                    "color": "#6be5c3",
                    "fillOpacity": 1.0
                },
                "drawError": {
                    "color": "#dd253b",
                    "message": "Oups!"
                },
                "allowIntersection": False
            }
            draw_control.circle = {
                "shapeOptions": {
                    "fillColor": "#efed69",
                    "color": "#efed69",
                    "fillOpacity": 1.0
                }
            }
            draw_control.rectangle = {
                "shapeOptions": {
                    "fillColor": "#fca45d",
                    "color": "#fca45d",
                    "fillOpacity": 1.0
                }
            }

            self.add_control(draw_control)

        def add_layers_control(self, position="topright"):
            """Adds a layers control to the map.
            Args:
                kwargs: Keyword arguments to pass to the layers control.
            
            Returns: 
                ipyleaflet.LayersControl: The layers control.
            """
            layers_control = ipyleaflet.LayersControl(position=position)
            self.add_control(layers_control)

        def add_fullscreen_control(self, position="topleft"):
            """Adds a fullscreen control to the map.
            Args:
                kwargs: Keyword arguments to pass to the fullscreen control.

            Returns:
                ipyleaflet.FullscreenControl: Allows control of screensize.
            """
            fullscreen_control = ipyleaflet.FullScreenControl(position=position)
            self.add_control(fullscreen_control)