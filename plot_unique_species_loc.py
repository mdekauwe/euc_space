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
import matplotlib.pyplot as plt
import os
import cartopy.crs as ccrs
import matplotlib.patches as mpatches

def main():

    fname = "species_locations.csv"
    df = pd.read_csv(fname)

    names = np.unique(df.species)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())


    import seaborn as sns
    #colours = sns.color_palette("tab20b", len(names))
    colours = sns.color_palette("tab20", len(names))

    for j,spp in enumerate(names):

        df_sp = df[df["species"] == spp]
        spp_count = len(df_sp)


        if spp_count > 1:
            vals = []
            vals2 =[]
            lats_needed = df_sp["lat"].values
            lons_needed = df_sp["lon"].values
            
        ax.plot(lons_needed, lats_needed, ls=" ", marker='o', color=colours[j],
                markersize=0.5, alpha=0.5, label=spp)





    lables_patches = []
    for j,spp in enumerate(names):
        add_patch = plt.scatter([],[], color=colours[j], label=spp)
        lables_patches.append(add_patch)

    ax.legend(lables_patches, names, numpoints=1, loc='upper center',
              bbox_to_anchor=(0.25, 0.25), ncol=3,framealpha=1.0,
              frameon=True, fontsize=5)

    ax.coastlines()

    fig.savefig("euc_unique_locations.png", dpi=130)




if __name__ == "__main__":

    main()
