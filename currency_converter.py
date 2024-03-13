"""Takes in dollar amount and converts it to country of choice."""

import requests
def convert(initial_amount):
    api_url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_uZ84G1zfwrgWecrmEmdMZDOFHqct3emozvynpLTi"
    response = requests.get(api_url)
    data = response.json()

    conversion_amount = 0.0
    for key in data['data']:
        if key == "INR":
            conversion_amount = float(initial_amount) * float(data['data'][key])
    rounded_amount = str(round(conversion_amount, 2))

    #print("Your new amount after conversion to " + country  + " is " + str(rounded_amount))
