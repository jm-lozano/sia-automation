import os, platform, json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import yaml

# Reading config.yaml
with open("config.yaml", "r") as file:
    try:
        config = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

# ----------------------- CONFIGURATION --------------------------
coinmarketcap_api = config["coinmarketcap_api"]
usd_upload_price = config["usd_upload_price"]
usd_download_price = config["usd_download_price"]
usd_storage_price = config["usd_storage_price"]
collateral_ratio = config["collateral_ratio"]
storage_price_min = config["siacoin_storage_price_min"]
storage_price_max = config["siacoin_storage_price_max"]
# ----------------------- CONFIGURATION --------------------------

# Returns the USD/SC price listed in coinmarketcap.com
def get_siacoin_price():
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
        print("CMC Siacoin price is", price, "USD")
        return price
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num

siacoin_price = get_siacoin_price()
print("############ PRICE SETTINGS ############")
download_price = usd_download_price / siacoin_price
print("Download price updating to...", download_price, "SC")

upload_price = usd_upload_price / siacoin_price
print("Upload price updating to...  ", upload_price, "SC")

storage_price = usd_storage_price / siacoin_price
storage_price = clamp(storage_price, storage_price_min, storage_price_max)
print("Storage price updating to... ", storage_price, "SC")

collateral = storage_price * collateral_ratio
print("Collateral updating to...    ", collateral, "SC")

if platform.system() == "Linux":
    os.system("siac host config mindownloadbandwidthprice " + str(download_price) + "SC")
    os.system("siac host config minuploadbandwidthprice " + str(upload_price) + "SC")
    os.system("siac host config minstorageprice " + str(storage_price) + "SC")
    os.system("siac host config collateral " + str(collateral) + "SC")
if platform.system() == "Windows":
    print("Error: windows is not supported")
