# utilitiesPackage/DataCleaner.py
 
from .CSVProcessor import CSVProcessor
from .AnomalyHandler import AnomalyHandler
from .ZipCodeAPI import ZipCodeAPI
 
import os
 
class DataCleaner:
    def __init__(self, input_path, output_folder="data", api_key=None):
        self.input_path = input_path
        self.output_folder = output_folder
        self.api_key = api_key
 
    def run_cleanup(self):
        # Step 1: Load and prepare data
        processor = CSVProcessor(self.input_path)
        processor.format_gross_price()
        processor.remove_duplicates()
 
        # Step 2: Remove and save Pepsi anomalies
        handler = AnomalyHandler(processor.get_dataframe())
        handler.separate_pepsi_purchases(column="Fuel Type")
        handler.save_anomalies(output_folder=self.output_folder)
 
        # Step 3: Work on cleaned data
        cleaned_df = handler.get_cleaned_data()
 
        # Step 4: Fix zip codes in "Full Address"
        if self.api_key:
            zip_fixer = ZipCodeAPI(cleaned_df, api_key=self.api_key, address_column="Full Address")
            zip_fixer.fix_missing_zip_codes(max_fixes=5)
            cleaned_df = zip_fixer.get_dataframe()
        else:
            print("No API key provided , skipping zip code fixing.")
 
        # Step 5: Save cleaned data
        os.makedirs(self.output_folder, exist_ok=True)
        output_path = os.path.join(self.output_folder, "cleanedData.csv")
        cleaned_df.to_csv(output_path, index=False)
