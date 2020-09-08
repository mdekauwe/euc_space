#!/usr/bin/env python

"""
For the Eucs that we have traits for, plot their distribution and output the
MAT and MAP

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (07.11.2020)"
__email__ = "mdekauwe@gmail.com"

import pandas as pd
import sys
import numpy as np
import os


def main(eucs_we_have):

    fname = "data/euc_latlong_butt.csv"
    df = pd.read_csv(fname)

    names = np.unique(eucs_we_have)


    rows = []

    for j,spp in enumerate(names):

        df_sp = df[df["species"] == spp]
        spp_count = len(df_sp)

        if spp_count > 1:
            vals = []
            vals2 =[]
            lats_needed = df_sp["latitude"].values
            lons_needed = df_sp["longitude"].values
            Tmin = 99999.
            Tmax = -99999.
            for i in range(len(df_sp)):
                latx = float(lats_needed[i])
                lonx = float(lons_needed[i])

                rows.append([spp, latx, lonx])

    dfl = pd.DataFrame(rows, columns=['species','lat','lon'])
    dfl = dfl.drop_duplicates()

    dfl.to_csv("species_locations.csv", index=False)

def x_round(x):
    # Need to round to nearest .25 or .75 to match the locations in CRU
    val = round(x * 4.0) / 4.0
    valx = str(val).split(".")
    v1 = valx[0]
    v2 = valx[1]

    if v2 <= "25":
        v2 = "25"
    else:
        v2 = "75"
    valx = float("%s.%s" % (v1, v2))

    return (valx)


if __name__ == "__main__":
    #"""
    eucs_i_have = ['Eucalyptus accedens',\
                    'Eucalyptus albida',\
                    'Eucalyptus blakelyi',\
                    'Eucalyptus camaldulensis',\
                    'Eucalyptus capillosa',\
                    'Eucalyptus cladocalyx',\
                    'Eucalyptus crebra',\
                    'Eucalyptus diversicolor',\
                    'Eucalyptus dunnii',\
                    'Eucalyptus globulus',\
                    'Eucalyptus globulus',\
                    'Eucalyptus gomphocephala',\
                    'Eucalyptus grandis',\
                    'Eucalyptus largiflorens',\
                    'Eucalyptus macrorhyncha',\
                    'Eucalyptus marginata',\
                    'Eucalyptus melliodora',\
                    'Eucalyptus obliqua',\
                    'Eucalyptus populnea',\
                    'Eucalyptus saligna',\
                    'Eucalyptus sideroxylon',\
                    'Eucalyptus tereticornis',\
                    'Eucalyptus tetrodonta',\
                    'Eucalyptus viminalis',\
                    'Eucalyptus wandoo']
    #"""

    # brendan's list
    eucs_we_have = ['Eucalyptus cladocalyx',\
                    'Eucalyptus crebra',\
                    'Eucalyptus dunnii',\
                    'Eucalyptus saligna',\
                    'Eucalyptus tetricornis',\
                    'Eucalyptus grandis',\
                    'Eucalyptus melliodora',\
                    'Eucalyptus sideroxylon',\
                    'Eucalyptus teriticornis',\
                    'Eucalyptus grandis',\
                    'Eucalyptus viminalis',\
                    'Eucalyptus sideroxylon',\
                    'Eucalyptus blakelyi',\
                    'Eucalyptus macrorhyncha',\
                    'Eucalyptus melliodora',\
                    'Eucalyptus largiflorens',\
                    'Eucalyptus populnea',\
                    'Eucalyptus miniata',\
                    'Eucalyptus tetradonta',\
                    'Eucalyptus fibrosa',\
                    'Eucalyptus moluccana',\
                    'Eucalyptus teriticornus',\
                    'Eucalyptus dumosa',\
                    'Eucalyptus socialis',\
                    'Eucalyptus obliqua',\
                    'Eucryphia lucida',\
                    'Eucalyptus salmonophloia',\
                    'Eucalyptus salubris',\
                    'Eucalyptus dalrympleana',\
                    'Eucalyptus laevopinea',\
                    'Eucalyptus pauciflora']

    eucs_we_have = eucs_i_have + eucs_we_have
    eucs_we_have = set(eucs_we_have)
    eucs_we_have = list(eucs_we_have)

    main(eucs_we_have)
