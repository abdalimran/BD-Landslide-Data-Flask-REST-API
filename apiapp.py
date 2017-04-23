from flask import Flask
from flask import jsonify

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import year_vs_nlandslides
import types_vs_fatalities
import trigger_vs_type_mud
import trigger_vs_type_land
import month_vs_nlandslides
import city_vs_nlandslides

app = Flask(__name__)

@app.route("/")
def hello():
    return "Wellcome to Landslide Data for Bangladesh API"

@app.route("/visualizations")
def getVisualizations():
    visualizations = {
        "year_vs_nlandslides":"https://github.com/abdalimran/Bangladesh-Landslide-Data-Analysis/raw/master/01_year_vs_nlandslides.jpg",
        "month_vs_nlandslides":"https://github.com/abdalimran/Bangladesh-Landslide-Data-Analysis/raw/master/02_month_vs_nlandslides.jpg",
        "city_vs_nlandslides":"https://github.com/abdalimran/Bangladesh-Landslide-Data-Analysis/raw/master/03_city_vs_nlandslides.jpg",
        "landslide_type_vs_trigger":"https://github.com/abdalimran/Bangladesh-Landslide-Data-Analysis/raw/master/04_landslide_type_vs_trigger.jpg",
        "mudslide_type_vs_trigger":"https://github.com/abdalimran/Bangladesh-Landslide-Data-Analysis/raw/master/05_mudslide_type_vs_trigger.jpg",
        "fatalities_yr_types":"https://github.com/abdalimran/Bangladesh-Landslide-Data-Analysis/raw/master/06_fatalities_yr_types.jpg"
    }
    return jsonify(visualizations)

@app.route("/bd-landslides-data")
def getData():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    data = {
        "longitude":data['longitude'].values.tolist(),
        "latitude":data['latitude'].values.tolist(),
        "cities":data['city'].values.tolist(),
        "location_accuracy_km":data['location_accuracy_km'].values.tolist()
    }
    return jsonify(data)


@app.route("/news-feeds")
def getNewsFeeds():
    data = pd.read_csv('Bangladesh_Landslide_Cleaned_Data.csv')

    clean_links = data['source_link'].dropna()
    news = {
        "feeds":clean_links.values.tolist()
    }
    return jsonify(news)


if __name__ == "__main__":
    app.run()