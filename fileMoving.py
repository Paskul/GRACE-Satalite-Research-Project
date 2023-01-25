import netCDF4 as nc
import numpy as np
import glob
import os

#Line 8 loads the file directory from the NASA database server connected to my computer, I can help set this up for each computer needed when I am back at campus.
#This method allows for (I believe) most current data always being sent to a computer able to be used, as long as there is an internet connection
dirname = '//podaac-tools.jpl.nasa.gov@SSL/DavWWWRoot/drive/files/allData/tellus/L3/grace/land_mass/RL06/v04/CSR'

#Lines 11-12 are used for displaying what file is being used in the terminal when program is run
totalFiles = len(glob.glob1(dirname,"*.nc"))
hitFile = 0

#Line 16 begins the for-loop that will itterate through the file directory loaded under 'dirname' from the NASA server we set up earlier
#Directory can be changed accordingly, same with file type but more code may have to be changed if changing file type
for files in glob.glob(os.path.join(dirname,'*.nc')):
    print("Working on file: " + files)
    hitFile+=1

    #Line 21 uses the netCDF4 library to turn the .nc file into a readable dataset we can use
    ds = nc.Dataset(files,'r')

    #Lines 25-32 are taking data from that file and storing them in their given variables, I can explain this more later
    #This is just a framework, we can store this data into 'global' variables that we can then use after itteration (ie. graphing, data analysis)
    lon = ds['lon'][:]
    lat = ds['lat'][:]
    time = ds['time'][:]
    lwe = ds['lwe_thickness'][:][:][:]
    uncertainty = ds['uncertainty'][:][:][:]
    lat_bounds = ds['lat_bounds'][:][:]
    lon_bounds = ds['lon_bounds'][:][:]
    time_bounds = ds['time_bounds'][:][:]


    #Line 37 will only run if the file above ran sucsessfully, this program is structured to run files in order as they are in the file directory
    #If one file does not sucsessfully load (which I don't see how that can happen) the current program will crash
    print("Finished file: %d / %d" % (hitFile, totalFiles))