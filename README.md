# Setup for Ubuntu 20.0.4 LTS

1 Download the script from github.
```
sudo git clone https://github.com/0xDreiker/sia-automation
```

2 Give execution permissions to the script.
```
cd sia-automation
sudo chmod 755 linux.py
```

3 Modify the prices in config.yaml
```
sudo nano config.yaml
```

4 Open crontab to add a cronjob every 24 hours.

```
sudo nano crontab -e
```
And add this at the end of the file.
```
0 0 * * * path/to/your/folder/linux.py
```

5 Run the script manually to see if it works.
```
python3 linux.py
```