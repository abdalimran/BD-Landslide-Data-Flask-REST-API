import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    month_occurence = data['month_number'].value_counts()
    month_occurence = month_occurence.sort_index()

    month_label = ['','January','February','March','April','May','June','July','August','September','October','November','December']

    months =  []
    m_occurrences = []

    for i in month_occurence.index:
        months.append(month_label[i])
        m_occurrences.append(month_occurence[i])


    y_pos = np.arange(len(months))
    
    plt.barh(y_pos, m_occurrences, align='center', color='darkslategrey')
    plt.yticks(y_pos, months)
    plt.ylabel('Months')
    plt.xlabel('Number of Landslides')
    plt.title('Month vs Number of Landslides')
    plt.tight_layout()

    plt.rcParams['axes.facecolor']='#e0f2f1'
    plt.rcParams['savefig.facecolor']='#e0f2f1'

    plt.savefig('02_month_vs_nlandslides.png', dpi = 1000)
    # plt.show()