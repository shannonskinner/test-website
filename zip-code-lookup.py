
# coding: utf-8

import pandas as pd
import numpy as np
input_zip = input('What is your zip code?')

# bring in data from Census sources

zips = pd.read_csv('https://www2.census.gov/geo/docs/maps-data/data/rel/zcta_county_rel_10.txt', dtype={'ZCTA5': str, 'STATE': str, 'COUNTY':str, 'GEOID':str})
counties = pd.read_csv('https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt', header=None, names=['STATE','STATEFP', 'COUNTYFP', 'COUNTYNAME', 'CLASSFP'], dtype={'STATEFP': str, 'COUNTYFP':str, 'GEOID':str})


# As user to input zip code

# calculate & output 

counties['GEOID'] = counties.STATEFP.map(str)+counties.COUNTYFP.map(str)
counties = counties[['STATE', 'GEOID', 'STATEFP', 'COUNTYFP', 'COUNTYNAME', 'CLASSFP']]
input_geoid = str(zips[zips['ZCTA5']==input_zip]['GEOID'].values[0])
county_output = counties.COUNTYNAME[counties.GEOID==str(zips[zips['ZCTA5']==input_zip]['GEOID'].values[0])].values[0]
state_output = counties.STATE[counties.GEOID==str(zips[zips['ZCTA5']==input_zip]['GEOID'].values[0])].values[0]
print('Zip code ',input_zip, ' is in ',county_output,', ',state_output,'. Thank you!')
