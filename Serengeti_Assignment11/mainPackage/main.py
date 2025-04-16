# File Name : main.py
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

from utilitiesPackage.DataCleaner import *

def main():
    input_csv = "data/fuelPurchaseData.csv"
    api_key = "3508b790-162b-11f0-b9cf-5b5cb0986f53"  # Be sure this still has uses
    cleaner = DataCleaner(input_path=input_csv, output_folder="data", api_key=api_key)
    cleaner.run_cleanup()
    print(" Data cleanup complete. Check 'cleanedData.csv' and 'dataAnomalies.csv' in the data folder.")

if __name__ == "__main__":
    main()


