import csv
from typing import Dict

# Get the phone number price for the country 
def nums_price_from_country(country: str, num_type: str) -> float:
    with open('csv/nums.csv','r') as file:
        for row in csv.DictReader(file):
            if row["Country"] == country and row["Phone Number Type"] == num_type:
                #return row
                return row["Phone Number Price / month"]
            
# Get the price for voice minutes
def voice_price_from_country(country: str) -> Dict:
    price : Dict = {}
    with open('csv/voice.csv', 'r') as file:
        for row in csv.DictReader(file):
            if row["Country"] == country:
                price.update({row["Description"] : row["Price / min"]})
            if country in row["Description"]:
                price.update({row["Description"] : row["Price / min"]})
        return price
    
# Get the prices for the bulk quantities
def bulk_price(quant: float, price: float) -> float:
    return quant * price

def bulk_voice(quant: float, prices: Dict) -> Dict:
    bulks = {}
    for desc, price in prices.items():
        bulks.update({desc : f"{float(price) * quant}"})
    return bulks