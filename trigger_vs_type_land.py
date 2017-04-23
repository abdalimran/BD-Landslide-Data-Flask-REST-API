import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    landslide_type = list(data['landslide_type'])
    landslide_trigger = list(data['trigger'])

    landslide_type_trigger = pd.DataFrame({'landslide_type': landslide_type, 'trigger': landslide_trigger})
    landslide_type_trigger = landslide_type_trigger.sort_values(by=['landslide_type'], ascending=True)

    landslide_df = landslide_type_trigger.iloc[:29]
    mudslide_df = landslide_type_trigger.iloc[29:]

    landslide_trigger_occ = landslide_df['trigger'].value_counts()
    mudslide_trigger_occ = mudslide_df['trigger'].value_counts()


    plt.axis("equal")
    plt.pie(
        list(landslide_df['trigger'].value_counts().values),
        labels=list(landslide_df['trigger'].unique()),
        autopct="%1.1f%%",
        explode = (0.05, 0, 0),
        startangle=90
    )
    plt.title("Trigger percentage of Landslide")

    plt.rcParams['axes.facecolor']='#e0f2f1'
    plt.rcParams['savefig.facecolor']='#e0f2f1'

    plt.tight_layout()
    plt.savefig('04_landslide_type_vs_trigger.png', dpi = 1000)

    # plt.show()