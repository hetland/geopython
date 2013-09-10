# Script to read burl1 data to extract wind
# Rob Hetland
# 2013-09-03

import numpy as np
from datetime import datetime

f = open('burl1_2011.dat')

dates = []
pressure = []

for line in f.readlines()[2:]:
    data = line.split()
    year = int(data[0])
    dates.append(datetime(year, 1, 1))
    pressure.append( float(data[12]) )

# pressure = np.array(pressure)
# dates = np.array(dates)

data = {'dates': np.array(dates), 'pressure': np.array(pressure)}
print data['dates']
print data['pressure']


# print 'Mean pressure = ', pressure.mean()
# print 'Min pressure = ', pressure.min()
# print 'Max pressure = ', pressure.max()
