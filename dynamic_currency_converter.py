#Build a currency converter that takes user input for the amount and converts it to another currency.

import requests

url = "https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD"
key = ""

def get_currency():
    start_currency = input("What currency do you have? fx USD ")
    start_amount = input(f"How much {start_currency} do you have?")
    end_currency = input(f"What currency do you want?")

    api = f"https://v6.exchangerate-api.com/v6/{key}/latest/{start_currency}"
    response = requests.get(api)
    data = response.json()

    conversion_rate = data["conversion_rates"][end_currency]

    return f"{str(start_amount)} {start_currency} is the same as {float(conversion_rate) * float(start_amount)} {end_currency}"

    
print(get_currency())
