# File Name : AnomalyHandler.py
# Student Name: Matthew Boutros, Derick Bellofatto
# email:  boutromw@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  4/16/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment involves cleaning and formatting a fuel purchase dataset by removing duplicates, filtering anomalies, correcting missing zip codes using an API, and writing the cleaned data to structured CSV files.

# Brief Description of what this module does: Separates rows with Pepsi purchases from the dataset and saves them to a separate anomalies file.
# Citations: chatgpt.com - generate certain code, zipcodebase.com - understanding their documentation

# Anything else that's relevant:

import pandas as pd
import os

class AnomalyHandler:
    def __init__(self, df):
        self.df = df
        self.anomalies = pd.DataFrame()
        self.cleaned = pd.DataFrame()

    def separate_pepsi_purchases(self, column="Fuel Type"):
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        self.anomalies = self.df[self.df[column].str.lower() == "pepsi"]
        self.cleaned = self.df[self.df[column].str.lower() != "pepsi"]

    def get_cleaned_data(self):
        return self.cleaned

    def save_anomalies(self, output_folder="data", filename="dataAnomalies.csv"):
        os.makedirs(output_folder, exist_ok=True)
        anomaly_path = os.path.join(output_folder, filename)
        self.anomalies.to_csv(anomaly_path, index=False)


