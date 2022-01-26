# What is Sia Automation

Sia Host has no built-in functionality to use currencies like USD and EUR as price reference. You can set prices in Siacoin (SC), and that
is what this tool allows you to do, to stablish prices in a fiat currency to avoid volatibility.

# Setup for Ubuntu 20.0.4 LTS

### Installation

Download the script from github.  
`sudo git clone https://github.com/0xDreiker/sia-automation`

Navigate to the folder  
`cd sia-automation`

And give execution permissions to the script.  
`sudo chmod 755 linux.py`

### Configuration

Create a CMC API key. You have to register in https://coinmarketcap.com/api/

Open the config.yaml file in the sia-automation folder.  
`sudo nano config.yaml`

You will find something like this. Paste the Coinmarketcap API and modify the price parameters as you like.
```
# Register in https://coinmarketcap.com/api/ to get an API key.
coinmarketcap_api: "YOUR_COINMARKETCAP_API_KEY"

usd_upload_price: 0        # Price in USD per TB of bandwidth upload.
usd_download_price: 25     # Price in USD per TB of bandiwdth download.
usd_storage_price: 0.5     # Price in USD per TB of stored data.
collateral_ratio: 2        # Recommended collateral ratio between 1.5 and 2.
```
### Creating a cronjob

Open crontab to add a cronjob every 24 hours.  
`sudo nano crontab -e`  

And add this at the end of the file  
`0 0 * * * python3 path/to/your/folder/linux.py`

Try to run the script manually and see if it works.  
`python3 linux.py`
