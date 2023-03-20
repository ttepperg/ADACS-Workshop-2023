#! /usr/bin/env python
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
RA = '00:42:44.3'
DEC = '41:16:09'
NUM_STARS = 1_000  # _000 # underscores are stripped out by interpreter

def get_radec(ra:float,dec:float) -> (float,float): # using typing
    '''
    Calculate the right-ascension and declination in degrees
    :param RA (float): right-ascension in (h,m,s)
    :param DEC (float): declination in (d,m,s)
    :return: 2-tuple with ra and dec in degrees
    '''
    d, m, s = dec.split(':')
    _dec = int(d) + int(m) / 60 + float(s) / 3600
    h, m, s = ra.split(':')
    _ra = 15 * (int(h) + int(m) / 60 + float(s) / 3600)
    _ra = _ra / math.cos(_dec * math.pi / 180)
    return _ra, _dec

def make_stars(num,ra,dec):
    '''
    Create an ensemnble of tars with random coordinates one degree around (ra,dec)
    :param num: number of stars
    :return: two lists with ra and dec values for each star
    '''
    ras = []
    decs = []
    for dummy in range(num):
        ras.append(ra + random.uniform(-1, 1))
        decs.append(dec + random.uniform(-1, 1))
    return ras, decs

def main():
    '''
    Run the script
    :return: None
    '''
    # convert sky coordinates to decimal degrees
    ra, dec = get_radec(RA,DEC)

    # generate ensemble of stars within 1 degree of Andromeda
    ras, decs = make_stars(NUM_STARS,ra,dec)

    # now write these to a csv file for use by my other program
    f_name = open('../data/catalog.csv', 'w', encoding='ascii')
    print("id,ra,dec", file=f_name)
    for i in range(NUM_STARS):
        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f_name)
    f_name.close()

    # visualise
    plt.scatter(ras[:], decs[:], marker='.', s=2)
    plt.xlabel('RA')
    plt.ylabel('Dec')
    plt.show()

if __name__ == '__main__':
    main()