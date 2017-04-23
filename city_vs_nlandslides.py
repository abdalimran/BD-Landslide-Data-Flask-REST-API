import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    city_occurence = data['city'].value_counts()
    city_occurence = city_occurence.sort_index()

    cities = city_occurence.index
    c_occurrences = city_occurence.values

    x = list(range(0,110,5))
    y = city_occurence

    plt.plot(x, y, marker='o',color='navy',linestyle='-')
    plt.xticks(x, cities, rotation='vertical')
    plt.ylim(0, 8)
    plt.xlabel('Cities')
    plt.ylabel('Number of Landslides')
    plt.title('City vs Number of Landslides')
    plt.tight_layout()

    plt.rcParams['axes.facecolor']='#e0f2f1'
    plt.rcParams['savefig.facecolor']='#e0f2f1'

    plt.savefig('../static/03_city_vs_nlandslides.png',dpi = 1000)
    # plt.show()