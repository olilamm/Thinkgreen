import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(layout=wide)

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

def get_layers(url):
    options = leafmap.get_wms_layers(url)
    return options 

st.title("Select a basemap from the drop-down menu")

col1, col2 = st.columns([4,1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    def add_toolbar(self, position="topright"):
        
        import ipywidgets as widgets 

        basemap = widgets.Dropdown(
        options=['ROADMAP', 'SATELLITE', 'TERRAIN'],
        value=None,
        description='Basemap:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='250px')
        )

        basemap_ctrl = ipyleaflet.WidgetControl(widget=basemap, position='bottomright')
        self.add_control(basemap_ctrl)
        def change_basemap(change):
            if change['new']:
                self.add_basemap(basemap.value)

        basemap.observe(change_basemap, names='value')

        def toolbar_click(b):
            with b:
                b.clear_output()

                if b.icon == 'map':
                    self.add_control(basemap_ctrl)