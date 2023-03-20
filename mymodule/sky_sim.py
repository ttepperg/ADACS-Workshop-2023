'''

Author: Paul Hancock (2023)

About: Create a synthetic sky catalogue where:

- Stars should have randomized sky positions around the Andromeda galaxy
- Positions should fall within 1 degree of the central location
- Each star should have a unique ID
- The star ID and position should be saved in a csv file to be analyzed by other programs

'''

import math
import random
import matplotlib.pyplot as plt

# Determine Andromeda location in ra/dec degrees
# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

# convert to decimal degrees

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/math.cos(dec*math.pi/180)

nsrc = 1_000  # _000 # underscores are stripped out by interpreter

# make nsrc stars within 1 degree of Andromeda
# from random import *
ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + random.uniform(-1, 1))
    decs.append(dec + random.uniform(-1, 1))


# now write these to a csv file for use by my other program
f = open('../data/catalog.csv', 'w')
print("id,ra,dec", file=f)
for i in range(nsrc):
    print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
f.close()

# visualise
plt.scatter(ras[:], decs[:], marker='.', s=2)
plt.show()
