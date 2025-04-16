# File Name : CSVProcessor.py
# Student Name: Matthew Boutros, Derick Bellofatto
# email:  boutromw@mail.uc.edu, bellofdk@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:  4/16/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment involves cleaning and formatting a fuel purchase dataset by removing duplicates, filtering anomalies, correcting missing zip codes using an API, and writing the cleaned data to structured CSV files.

# Brief Description of what this module does: Handles reading the CSV file, formatting numeric columns, and removing duplicate rows.
# Citations: chatgpt.com - generate certain code, zipcodebase.com - understanding their documentation

# Anything else that's relevant:

import pandas as pd

class CSVProcessor:
    def __init__(self, filepath):
        # Force 'Transaction Number' to be read as string to avoid DtypeWarning
        self.filepath = filepath
        self.df = pd.read_csv(filepath, dtype={"Transaction Number": str}, low_memory=False)

    def format_gross_price(self, price_column="Gross Price"):
        if price_column in self.df.columns:
            self.df[price_column] = self.df[price_column].astype(float).round(2)

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def get_dataframe(self):
        return self.df

    def save(self, output_path):
        self.df.to_csv(output_path, index=False)

