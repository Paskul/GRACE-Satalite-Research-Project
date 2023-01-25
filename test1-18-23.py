import netCDF4 as nc
import numpy as np

dirname = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR'
filename = 'GRD-3_2003305-2003334_GRAC_UTCSR_BA01_0600_LND_v04'
location = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR/GRD-3_2003305-2003334_GRAC_UTCSR_BA01_0600_LND_v04.nc'

f = nc.Dataset(location)

#print(f.variables.keys()) # get all variable names
lwe = f.variables['lwe_thickness'] # temperature variable
#print(lwe)

#for d in f.dimensions.items():
  #print(d)

print(lwe.dimensions)
print(lwe.shape)
time = f.variables['time']
print(time)

timeUsing = time[:]
print(time.shape)
print(time.dimensions)
print(timeUsing)


lat, lon = f.variables['lat'], f.variables['lon']
latvals = lat[:]; lonvals = lon[:]

print(lat)
print(lon)
print(lat[:])

import matplotlib.pyplot as plt
%matplotlib inline
cs = plt.contourf(soilm)