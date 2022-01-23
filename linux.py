import os, platform
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# ----------------------- CONFIGURATION --------------------------
coinmarketcap_api = "YOUR_COINMARKETCAP_API_KEY"
usd_upload_price = 0       # Unpload bandwidth price in USD
usd_download_price = 25    # Download bandwidth price in USD
usd_storage_price = 0.5    # Storage price in USD
collateral_ratio = 2       # Recommended collateral ratio between 1.5 and 2.
# ----------------------- CONFIGURATION --------------------------

# Returns the USD/SC price listed in coinmarketcap.com
def siacoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'symbol': 'SC',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': coinmarketcap_api,
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price = data["data"]["SC"]["quote"]["USD"]["price"];
        return price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

download_price = usd_download_price / siacoin_price()
print("> Download price updating...", download_price, "SC")

upload_price = usd_upload_price / siacoin_price()
print("> Upload price updating...  ", upload_price, "SC")

storage_price = usd_storage_price / siacoin_price()
print("> Storage price updating... ", storage_price, "SC")

collateral = storage_price * collateral_ratio
print("> Collateral updating...    ", collateral, "SC")

print("siac host config mindownloadbandwidthprice " + str(download_price) + " SC")
if platform.system() == "Linux":
    os.system("siac host config mindownloadbandwidthprice " + str(download_price) + "SC")
    os.system("siac host config minuploadbandwidthprice " + str(upload_price) + "SC")
    os.system("siac host config minstorageprice " + str(storage_price) + "SC")
    os.system("siac host config collateral " + str(collateral) + "SC")
if platform.system() == "Windows":
    print("Error: windows is not supported")
