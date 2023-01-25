import pandas as pd
import xarray as xr
import plotly.express as px
import plotly.graph_objects as go
import netCDF4 as nc
import numpy as np

dirname = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR\GRD-3_2005274-2005304_GRAC_UTCSR_BA01_0600_LND_v04.nc'

ds = xr.open_dataset(dirname)
#print(ds)
df = ds.to_dataframe()
#print(df.columns)

#artifically reading
testing = nc.Dataset(dirname,'r')
lon = testing['lon'][:]
lat = testing['lat'][:]
time = testing['time'][:]
lonNew = [np.nan]*len(df.index)
latNew = [np.nan]*len(df.index)
timeNew = [time]*len(df.index)

workingLon = 0.5
startingLat = -89.5
endingLat = 89.5
workingLat = startingLat
tick = 0
for i in range(len(df.index)):

    latNew[i] = workingLat
    lonNew[i] = workingLon
    workingLat += 1
    if workingLat > endingLat:
        tick+=1
        workingLat = startingLat
        if tick==2:
            workingLon+=1
            tick = 0

    #print(latNew[i])
    #print(lonNew[i])

#print(latNew[0])
#print(latNew[-1])

#print(len(latNew))
#print(len(lonNew))

#df.insert(0, 'time', [np.nan]*len(df.index))
df.insert(0, 'time', timeNew)
df.insert(0, 'lat', latNew)
df.insert(0, 'lon', lonNew)

print(df.columns)
print(df)

#fig = px.density_mapbox(df, lat='lat', lon='lon', z='lwe_thickness', radius=30, center=dict(lat=0, lon=180), zoom=0,mapbox_style="open-street-map", opacity=0.4)
#fig.show()

fig = go.Figure(go.Densitymapbox(lat=df.lat, lon=df.lon, z=df.lwe_thickness, radius=30, zmax= 1.0, zmin = 0.0))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()