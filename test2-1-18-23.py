import pygmt
pygmt.show_versions()

fig = pygmt.Figure()
fig.coast(region="g", frame=True, shorelines=1)
fig.show()









'''
import netCDF4 as nc
import numpy as np

dirname = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR'
filename = 'GRD-3_2003305-2003334_GRAC_UTCSR_BA01_0600_LND_v04'
location = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR/GRD-3_2003305-2003334_GRAC_UTCSR_BA01_0600_LND_v04.nc'

gfs = nc.Dataset(location)

for dname in sfctmp.dimensions:
  print(gfs.variables[dname])


soilmvar = gfs.variables['Volumetric_Soil_Moisture_Content_depth_below_surface_layer']
print(soilmvar)
print("================")
print(soilmvar.missing_value)
'''