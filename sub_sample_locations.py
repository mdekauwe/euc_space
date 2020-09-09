#!/usr/bin/env python

"""
Sub-sample N locations from species dist

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (09.09.2020)"
__email__ = "mdekauwe@gmail.com"

import pandas as pd
import sys
import numpy as np
import os


def main():

    N = 10

    fname = "species_locations.csv"
    df = pd.read_csv(fname)

    names = np.unique(df.species)

    rows = []

    for j,spp in enumerate(names):

        df_sp = df[df["species"] == spp]
        df_sp = df_sp.sample(n=N).reset_index()
        spp_count = len(df_sp)
        for i in range(len(df_sp)):

            rows.append([spp, df_sp.lat[i], df_sp.lon[i]])

    dfl = pd.DataFrame(rows, columns=['species','lat','lon'])
    dfl.to_csv("species_locations_sub_sampled.csv", index=False)

if __name__ == "__main__":

    main()
