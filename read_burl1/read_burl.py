# Script to read burl1 data to extract wind
# Rob Hetland
# 2013-09-03

import numpy as np

f = open('burl1_2011.dat')

pressure = []

for line in f.readlines()[2:]:
    data = line.split()
    pressure.append( float(data[12]) )

pressure = np.array(pressure)

print 'Mean pressure = ', pressure.mean()
print 'Min pressure = ', pressure.min()
print 'Max pressure = ', pressure.max()
