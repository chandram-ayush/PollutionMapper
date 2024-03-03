import netCDF4 as nc
import pandas as pd
import xarray as xr
import numpy as np
# Open the NetCDF file
nc_file = nc.Dataset('totrain.nc', 'r')
dataset = xr.open_dataset('totrain.nc')
print(dataset)
print(nc_file)
years = ['2007','2006']
for year in years:

    d1 = xr.open_dataset("PM25_data/"+year+"/1.nc")
    d2 = xr.open_dataset("PM25_data/"+year+"/2.nc")
    d3 = xr.open_dataset("PM25_data/"+year+"/3.nc")
    d4 = xr.open_dataset("PM25_data/"+year+"/4.nc")
    d5 = xr.open_dataset("PM25_data/"+year+"/5.nc")
    d6 = xr.open_dataset("PM25_data/"+year+"/6.nc")
    d7 = xr.open_dataset("PM25_data/"+year+"/7.nc")
    d8 = xr.open_dataset("PM25_data/"+year+"/8.nc")
    d9 = xr.open_dataset("PM25_data/"+year+"/9.nc")
    d10 = xr.open_dataset("PM25_data/"+year+"/10.nc")
    d11 = xr.open_dataset("PM25_data/"+year+"/11.nc")
    d12 = xr.open_dataset("PM25_data/"+year+"/12.nc")

    dd = {'01':d1,'02':d2,'03':d3,'04':d4,'05':d5,'06':d6,'07':d7,'08':d8,'09':d9,'10':d10,'11':d11,'12':d12}


    # Extract latitude, longitude, expver, time, and number
    latitude = nc_file.variables['latitude'][:]
    longitude = nc_file.variables['longitude'][:]
    time = [year+'-01-01',year+'-02-01',year+'-03-01',year+'-04-01',year+'-05-01',year+'-06-01',year+'-07-01',year+'-08-01',year+'-09-01',year+'-10-01',year+'-11-01',year+'-12-01']

    # Initialize an empty list to store data row by row
    data_rows = []

    for lat in np.arange(-8, 44, 0.5):
        print(lat,' - latitude')
        for lon in np.arange(65, 144, 0.5):
            print(lon)
            for t in time:
                num = 0
                exp = 1

                # Store the data row as a dictionary
                d = {
                    'latitude': lat,
                    'longitude': lon,
                    'time': t,
                }
                for var_name, var in nc_file.variables.items():
                        if var_name not in ['latitude', 'longitude', 'expver', 'time', 'number']:
                            try:
                                variable = dataset[var_name]
                                d[var_name] = variable.sel(time=t,longitude=lon,latitude=lat).item()
                            except:
                                    print(lon,lat,exp,t,num,var_name)
                
                # Adding PAM25 value
                                    
                dataset2 = dd[t[5:7]]
                variable = dataset2['GWRPM25']
                nearest_lon = variable['lon'].sel(lon=lon+0.05, method='nearest')
                nearest_lat = variable['lat'].sel(lat=lat+0.05, method='nearest')
                value_at_nearest_point = variable.sel(lon=nearest_lon, lat=nearest_lat).item()
                if np.isnan(value_at_nearest_point):
                        continue
                d['PAM25'] = value_at_nearest_point
                data_rows.append(d)

    # Create DataFrame from the list of dictionaries
    df = pd.DataFrame(data_rows)

    # Close the NetCDF file
    

    d1.close()
    d2.close()
    d3.close()
    d4.close()
    d5.close()
    d6.close()
    d7.close()
    d8.close()
    d9.close()
    d10.close()
    d11.close()
    d12.close()

    
    # Export DataFrame to CSV
    df.to_csv('CSV_Data/dataset'+year+'.csv', index=False)
nc_file.close()
dataset.close()
