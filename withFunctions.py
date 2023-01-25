import netCDF4 as nc
import numpy as np
import glob
import os

lon = []
lat = []
time = []
lwe = []
uncertainty = []
lat_bounds = []
lon_bounds = []
time_bounds = []

dirname = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR'

def initializeData():
    totalFiles = len(glob.glob1(dirname,"*.nc"))
    hitFile = 0
    for files in glob.glob(os.path.join(dirname,'*.nc')):
        print("Working on reading file: " + files)
        hitFile+=1

        ds = nc.Dataset(files,'r')

        lon = ds['lon'][:]
        lat = ds['lat'][:]
        time = ds['time'][:]
        lat_bounds = ds['lat_bounds'][:][:]
        lon_bounds = ds['lon_bounds'][:][:]
        time_bounds = ds['time_bounds'][:][:]

        if hitFile == 1:
            lwe = ds['lwe_thickness'][:][:][:]
            uncertainty = ds['uncertainty'][:][:][:]
        else:
            lwe = np.concatenate([lwe, ds['lwe_thickness'][:][:][:]])
            uncertainty = np.concatenate([uncertainty, ds['uncertainty'][:][:][:]])

        
        print("Finished reading file: %d / %d" % (hitFile, totalFiles))
        #lon, lat, time, lat_bounds, lon_bounds, time_bounds stay the same
        #lwe and uncertainty changes
        #lwe is our big data chunk
    return lon, lat, time, lwe, uncertainty, lat_bounds, lon_bounds, time_bounds

(lon, lat, time, lwe, uncertainty, lat_bounds, lon_bounds, time_bounds) = initializeData()

print(lwe.shape)