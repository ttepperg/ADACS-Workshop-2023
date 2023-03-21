#! /usr/bin/env python
"""

Author: Paul Hancock (2023)

About: Create a synthetic sky catalogue where:

- Stars should have randomized sky positions around the Andromeda galaxy
- Positions should fall within 1 degree of the central location
- Each star should have a unique ID
- The star ID and position should be saved in a csv file to be analyzed by other programs

"""

import math
import random
import argparse
import matplotlib.pyplot as plt

# Determine Andromeda location in ra/dec degrees
# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'
NUM_STARS = 1_000  # _000 # underscores are stripped out by interpreter


# def get_radec(ra: str, dec: str) -> (float, float):  # using typing
def get_radec():
    """
    Calculate the right-ascension and declination in degrees
    _ra,_dec: 2-tuple with ra and dec in degrees
    """
    d, m, s = DEC.split(':')
    _dec = int(d) + int(m) / 60 + float(s) / 3600
    h, m, s = RA.split(':')
    _ra = 15 * (int(h) + int(m) / 60 + float(s) / 3600)
    _ra = _ra / math.cos(_dec * math.pi / 180)
    return _ra, _dec


def make_stars(num, ra, dec):
    """
    Create an ensemble of stars with random coordinates one degree around (ra,dec)
    num: number of stars
    ra, dec: sky coordinates in degree
    ras, decs: two lists with ra and dec values for each star
    """
    ras = []
    decs = []
    for dummy in range(num):
        ras.append(ra + random.uniform(-1, 1))
        decs.append(dec + random.uniform(-1, 1))
    return ras, decs


def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest='ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest='dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser


def main():
    """
    Run the script
    :return: None
    """
    # convert sky coordinates to decimal degrees
    # ra, dec = get_radec(RA, DEC)

    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec

    # generate ensemble of stars within 1 degree of Andromeda
    ras, decs = make_stars(NUM_STARS, ra, dec)

    # now write these to a csv file for use by my other program
    out_dir = '/Users/tepper/tutorials/ADACS-Workshop-2023/project/data/'
    out_file = options.out
    f_name = open(f'{out_dir}/{out_file}', 'w', encoding='ascii')
    print("id,ra,dec", file=f_name)
    for i in range(NUM_STARS):
        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f_name)
    f_name.close()

    # visualise
    plt.scatter(ras[:], decs[:], marker='.', s=2)
    plt.xlabel('RA (deg)')
    plt.ylabel('Dec (deg)')
    plt.show()


if __name__ == '__main__':
    main()
