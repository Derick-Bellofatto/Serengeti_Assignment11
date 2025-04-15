# utilitiesPackage/AnomalyHandler.py

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


