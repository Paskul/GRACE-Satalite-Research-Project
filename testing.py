import netCDF4 as nc
import numpy as np

#\\podaac-tools.jpl.nasa.gov@SSL\DavWWWRoot\drive\files\allData\tellus\L3\grace\land_mass\RL06\v04\CSR
#GRD-3_2002213-2002243_GRAC_UTCSR_BA01_0600_LND_v04.nc

fn = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR/GRD-3_2002213-2002243_GRAC_UTCSR_BA01_0600_LND_v04.nc'
ds = nc.Dataset(fn,'r')

#print(ds)
#print(ds.__dict__['standard_name_vocabulary'])

#for var in ds.variables.values():
    #print(var)

lon = ds['lon'][:]
lat = ds['lat'][:]
time = ds['time'][:]
lwe = ds['lwe_thickness'][:][:][:]
uncertainty = ds['uncertainty'][:][:][:]
lat_bounds = ds['lat_bounds'][:][:]
lon_bounds = ds['lon_bounds'][:][:]
time_bounds = ds['time_bounds'][:][:]

print(lat)

#print(lat)
#print(lwe_thickness(time[0], lat[20] , lon[20]))


    #time is only one point, hence there being only 1 file read
#lwe_thickness = ds['lwe_thickness'][:][:][:]
    #gets error, displaying all data points would be very high
#uncertainty = ds['uncertainty'][:][:][:]
    #gets error, displaying all data points would be very high


"""
float64 lon(lon)
    units: degrees_east
    long_name: longitude
    axis: X
    valid_min: 0.5
    valid_max: 359.5
    comment: longitude value at each pixel
unlimited dimensions: 
current shape = (360,)
filling on, default _FillValue of 9.969209968386869e+36 used
<class 'netCDF4._netCDF4.Variable'>
float64 lat(lat)
    units: degrees_north
    long_name: latitude
    axis: Y
    valid_min: -89.5
    valid_max: 89.5
    comment: latitude value at each pixel
unlimited dimensions:
current shape = (180,)
filling on, default _FillValue of 9.969209968386869e+36 used
<class 'netCDF4._netCDF4.Variable'>
float64 time(time)
    units: days since 2002-01-01T00:00:00
    long_name: time
    axis: T
    calendar: gregorian
    bounds: time_bounds
unlimited dimensions: time
current shape = (1,)
filling on, default _FillValue of 9.969209968386869e+36 used
<class 'netCDF4._netCDF4.Variable'>
float64 lwe_thickness(time, lat, lon)
    _FillValue: -99999.0
    units: m
    long_name: Liquid_Water_Equivalent_Thickness
    coordinates: time lat lon
    grid_mapping: WGS 84
    valid_min: -30.0
    valid_max: 30.0
    comment: none
unlimited dimensions: time
current shape = (1, 180, 360)
filling on
<class 'netCDF4._netCDF4.Variable'>
float64 uncertainty(time, lat, lon)
    _FillValue: -99999.0
    units: m
    long_name: uncertainty
    coordinates: time lat lon
    grid_mapping: WGS 84
    valid_min: -30.0
    valid_max: 30.0
    comment: none
unlimited dimensions: time
current shape = (1, 180, 360)
filling on
<class 'netCDF4._netCDF4.Variable'>
float64 lat_bounds(lat, bounds)
    long_name: latitude boundaries
    units: degrees_north
    comment: latitude values at the north and south bounds of each pixel
unlimited dimensions:
current shape = (180, 2)
filling on, default _FillValue of 9.969209968386869e+36 used
<class 'netCDF4._netCDF4.Variable'>
float64 lon_bounds(lon, bounds)
    long_name: longitude boundaries
    units: degrees_east
    comment: longitude values at the west and east bounds of each pixel
unlimited dimensions:
current shape = (360, 2)
filling on, default _FillValue of 9.969209968386869e+36 used
<class 'netCDF4._netCDF4.Variable'>
float64 time_bounds(time, bounds)
    long_name: time bounds for each time value, i.e. the first day and last day included in the monthly solution
    units: days since 2002-01-01T00:00:00
    comment: time bounds for each time value, i.e., the first day and last day included in the monthly solution
unlimited dimensions: time
current shape = (1, 2)
filling on, default _FillValue of 9.969209968386869e+36 used
"""