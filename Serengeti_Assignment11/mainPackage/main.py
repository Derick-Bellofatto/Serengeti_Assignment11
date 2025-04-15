# mainPackage/main.py

from utilitiesPackage.DataCleaner import *

def main():
    input_csv = "data/fuelPurchaseData.csv"
    api_key = "3508b790-162b-11f0-b9cf-5b5cb0986f53"  # Be sure this still has uses
    cleaner = DataCleaner(input_path=input_csv, output_folder="data", api_key=api_key)
    cleaner.run_cleanup()
    print(" Data cleanup complete. Check 'cleanedData.csv' and 'dataAnomalies.csv' in the data folder.")

if __name__ == "__main__":
    main()


