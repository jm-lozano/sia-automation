# Setup for Ubuntu 20.0.4 LTS

1 Download the script from github.  
`sudo git clone https://github.com/0xDreiker/sia-automation`

Navigate to the folder  
`cd sia-automation`


And give execution permissions to the script.  
`sudo chmod 755 linux.py`

2 Modify the prices in config.yaml  
`sudo nano config.yaml`

3 Open crontab to add a cronjob every 24 hours.  
`sudo nano crontab -e`  

And add this at the end of the file  
`0 0 * * * path/to/your/folder/linux.py`

Run the script manually to see if it works.  
`python3 linux.py`