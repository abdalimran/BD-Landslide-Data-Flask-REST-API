import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    year_occurence = data['year'].value_counts()
    year_occurence = year_occurence.sort_index()

    years = year_occurence.index
    y_occurrences = year_occurence.values

    y_pos = np.arange(len(years))
    
    plt.bar(y_pos, y_occurrences, align='center')
    plt.xticks(y_pos, years)
    plt.xlabel('Years')
    plt.ylabel('Number of Landslides')
    plt.title('Year vs Number of Landslides')
    plt.tight_layout()

    plt.rcParams['axes.facecolor']='#e0f2f1'
    plt.rcParams['savefig.facecolor']='#e0f2f1'

    plt.savefig('01_year_vs_nlandslides.png', dpi = 1000)
    #plt.show()