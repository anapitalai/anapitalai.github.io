import folium
import pandas as pd
import os

regions = os.path.join('data', 'PNG_prov_regions.geojson')
population_data = os.path.join('data', 'pop_prov.csv')
region_data = pd.read_csv(population_data)

m = folium.Map(location=[-6.7164372353137045, 146.9958686828613], zoom_start=7)

m.choropleth(
    geo_data=regions,
    name='choropleth',
    data=region_data,
    columns=['Geographical Area','Persons'],
    key_on='feature.properties.NAME',
    fill_color='YlGn',
    #fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.7,
    legend_name='Population'
)


dist=folium.GeoJson(
    regions,
    highlight_function=lambda x: {'weight':5,'color':'#000', 'dashArray':'1.7'},
    style_function=lambda x:{'opacity': 0.1,'dashArray': 0.2,'fillOpacity': 0.1}
).add_to(m)


folium.features.GeoJsonTooltip(fields=['NAME','ID']).add_to(dist)


##custom lengend


legend =   '''
                <div style="position: fixed; 
                            bottom: 50px; left: 50px; width: 100px; height: 90px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">&nbsp; Cool Legend <br>
                              &nbsp; East &nbsp; <i class="fa fa-map-marker fa-2x" style="color:green"></i><br>
                              &nbsp; West &nbsp; <i class="fa fa-map-marker fa-2x" style="color:red"></i>
                </div>
                ''' 
legend_html =   '''
                <div style="position: fixed; 
                            bottom: 70px; left: 70px; width: 500px; height: 100px; 
                            border:2px solid grey;background:pink; z-index:9999; font-size:14px;
                            ">&nbsp;
                            The population of Papua New Guinea has reached 7,275,324 according to 2011 Census. It has increased by 40% and at average annual growth rate 3.1% since the last census in 2000. In absolute numbers a total of 2,084,538 persons were added to the population during the last 11 years.
                             <br>
                </div>
                ''' 
     

m.get_root().html.add_child(folium.Element(legend_html))

folium.LayerControl().add_to(m)

m.save('png_pop.html')
