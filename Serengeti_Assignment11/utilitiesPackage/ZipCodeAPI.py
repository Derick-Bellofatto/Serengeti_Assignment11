
# utilitiesPackage/ZipCodeAPI.py
 
import requests
import pandas as pd
import re
 
class ZipCodeAPI:
    def __init__(self, df, api_key, address_column="Full Address"):
        self.df = df
        self.api_key = api_key
        self.address_column = address_column
        self.api_url = "https://app.zipcodebase.com/api/v1/code/city"
 
    def fix_missing_zip_codes(self, max_fixes=5):
        fixes = 0
 
        for idx, row in self.df.iterrows():
            full_address = row[self.address_column]
 
            if self._has_zip(full_address):
                print(f"Row {idx} already has zip")
                continue
 
            city = self._extract_city(full_address)
            if not city or len(city) < 2:
                print(f"Row {idx} skipped due to bad city: {city}")
                continue
 
            print(f"Row {idx} - Extracted city: {city}")
 
            try:
                zip_code = self.get_zip_from_city(city)
                if zip_code:
                    street = self._extract_street(full_address)
                    new_address = f"{street}, {city}, OH {zip_code}"
                    self.df.at[idx, self.address_column] = new_address
                    fixes += 1
                    print(f"Zip added: {zip_code} (fix count: {fixes})")
 
                    if fixes >= max_fixes:
                        print("Reached 5 fixes. Breaking loop.")
                        break
                else:
                    print(f"No zip code returned for {city}")
            except Exception as e:
                print(f"Error fixing address at row {idx}: {e}")
 
    def _has_zip(self, address):
        return bool(re.search(r"\b\d{5}(?:-\d{4})?\b", address))
 
    def _extract_city(self, address):
        try:
            parts = [p.strip() for p in address.split(",")]
            if len(parts) >= 2:
                return parts[-2]
        except Exception:
            return None
        return None
 
    def _extract_street(self, address):
        try:
            parts = [p.strip() for p in address.split(",")]
            return parts[0] if parts else address
        except Exception:
            return address
 
    def get_zip_from_city(self, city, country="US"):
        if not self.api_key:
            print("No API key provided.")
            return None
 
        params = {
            "apikey": self.api_key,
            "city": city,
            "country": country
        }
 
        try:
            response = requests.get(self.api_url, params=params, timeout=5)
            print(f"API call to {self.api_url} for city: {city}, status code: {response.status_code}")
 
            if response.status_code == 200:
                data = response.json()
                print(f"API response: {data}")
 
                zips = data.get("results", [])
                if zips and isinstance(zips, list):
                    return zips[0]
                else:
                    print(f"No zip found in results for city: {city}")
            else:
                print(f"API request failed with status {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Exception during API call: {e}")
 
        return None
 
    def get_dataframe(self):
        return self.df