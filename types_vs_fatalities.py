import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    years = list(data['year'])
    types = list(data['landslide_type'])
    fatalities = list(data['fatalities'])

    ytf_df = pd.DataFrame({"years":years,"types":types,"fatalities":fatalities})

    ytf_df = ytf_df.sort_values(by=['types'], ascending=True)

    landslide_ytf_df = ytf_df.iloc[:29]
    mudslide_ytf_df = ytf_df.iloc[29:]

    mudslide_fat_yr = []
    for y in data['year'].unique():
        mudslide_fat_yr.append(mudslide_ytf_df.loc[mudslide_ytf_df['years'] == y, 'fatalities'].sum())

    landslide_fat_yr = []
    for y in data['year'].unique():
        landslide_fat_yr.append(landslide_ytf_df.loc[landslide_ytf_df['years'] == y, 'fatalities'].sum())

    N = len(data['year'].unique())

    ind = np.arange(N)
    width = 0.35 

    ax = plt.subplot()
    land_fat_yr = ax.bar(ind, landslide_fat_yr, width, color='tomato')
    mud_fat_yr = ax.bar(ind+width, mudslide_fat_yr, width, color='navy')

    ax.set_ylabel('Number of Fatalities')
    ax.set_xlabel('Year')
    ax.set_title('Fatalities Every Year by Landslide Types')
    ax.set_xticks(ind + width / 2)
    ax.set_yticks(np.arange(min(mudslide_fat_yr), max(landslide_fat_yr)+1, 10))
    ax.set_xticklabels(data['year'].unique())
    ax.legend((land_fat_yr[0], mud_fat_yr[0]), ('Landslides', 'Mudslides'))

    plt.tight_layout()
    plt.savefig('06_fatalities_yr_types.png', dpi = 1000)

    # plt.show()