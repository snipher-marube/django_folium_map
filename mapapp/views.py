from django.shortcuts import render
import folium
import pandas as pd

from .models import Carbon

def home(request):
    m = folium.Map(location=[30, 10], zoom_start=2, tiles='cartodbpositron')
    data = Carbon.objects.all()
    
    # convert the data to DataFrame
    data_df = pd.DataFrame(data.values())
    
    # convert the annual_co2_emissions_tonnes column to float data type
    data_df = data_df['annual_co2_emissions_tonnes'].astype(float)
    
    #replace Nan values with 0
    data_df = data_df.fillna(0, inplace=True)
    
    # Create a Choropleth map
    choropleth = folium.Choropleth(
        geo_data='https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson',
        name='choropleth',
        data=data_df,
        columns=["Entity", "Annual_CO2_emissions_tonnes"],
        key_on='feature.properties.name',
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        nan_fill_color="white",
        legend_name='CO2 Emissions per Capita',
        highlight=True
    ).add_to(m)
    
    # add layer control
    folium.LayerControl().add_to(m)
    
    # save the map to html file
    m.save('templates/home.html')
    
    # if you want to embed the map in django template, use below code
    # m = m.save('static/map.html')
    
    context = {
        #'map': 'map.html'
    }
    return render(request, 'home.html', context)
