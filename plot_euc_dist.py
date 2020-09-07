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

def main(eucs_we_have):

    (matx, mapx, latitudes, longitudes) = get_mat_data()

    fname = "data/euc_latlong_butt.csv"
    df = pd.read_csv(fname)

    names = np.unique(eucs_we_have)
    print(len(names))
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
            lats_needed = df_sp["latitude"].values
            lons_needed = df_sp["longitude"].values
            Tmin = 99999.
            Tmax = -99999.
            for i in range(len(df_sp)):
                latx = float(x_round(float(lats_needed[i])))
                lonx = float(x_round(float(lons_needed[i])))
                r = np.where(latitudes==latx)
                c = np.where(longitudes==lonx)
                mat = matx[r,c][0][0]
                map = mapx[r,c][0][0]
                vals.append(mat)
                vals2.append(map)
                if mat > Tmax:
                    Tmax = mat
                if mat < Tmin:
                    Tmin = mat
            Trange = Tmax - Tmin

            vals = np.asarray(vals)
            vals2 = np.asarray(vals2)

            if len(vals) == 0:
                continue
            else:
                Trange = np.max(vals) - np.min(vals)
                spp_count = len(vals)

        print(spp, np.mean(vals), np.mean(vals2))

        ax.plot(lons_needed, lats_needed, ls=" ", marker='o', color=colours[j],
                markersize=0.5, alpha=0.5, label=spp)





    lables_patches = []
    for j,spp in enumerate(names):
        add_patch = plt.scatter([],[], color=colours[j], label=spp)
        lables_patches.append(add_patch)

    ax.legend(lables_patches, names, numpoints=1, loc='upper center',
              bbox_to_anchor=(0.25, 0.2), ncol=3,framealpha=1.0,
              frameon=True, fontsize=6)

    ax.coastlines()

    fig.savefig("euc_with_traits_dist.png", dpi=130)



def is_outlier(points, thresh=3.5):
    """
    Returns a boolean array with True if points are outliers and False
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor.
    """
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

def get_mat_data():
    # Get MAT data
    nrows = 360
    ncols = 720
    latitudes = np.linspace(-89.75, 89.75, nrows)
    longitudes = np.linspace(-179.75, 179.75, ncols)
    fname = "/Users/mdekauwe/research/CRU_TS_v4_bioclim_MAT_MAP_AI/MAT_1960_2010.bin"
    matx = np.fromfile(fname).reshape(nrows, ncols)

    fname = "/Users/mdekauwe/research/CRU_TS_v4_bioclim_MAT_MAP_AI/MAP_1960_2010.bin"
    mapx = np.fromfile(fname).reshape(nrows, ncols)

    return (matx, mapx, latitudes, longitudes)

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

    eucs_we_have = ['Eucalyptus accedens',\
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
                    'Eucalyptus miniata',\
                    'Eucalyptus obliqua',\
                    'Eucalyptus platyphylla',\
                    'Eucalyptus populnea',\
                    'Eucalyptus saligna',\
                    'Eucalyptus sideroxylon',\
                    'Eucalyptus tereticornis',\
                    'Eucalyptus tetrodonta',\
                    'Eucalyptus viminalis',\
                    'Eucalyptus wandoo']
    main(eucs_we_have)
