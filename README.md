# NotiPyer
Python 3 email bot for notifications 
  - current uses are for email alerts apon avaliablity of amazon product sizes
  
## Setup
Install required Python packages
```py
pip3 install -r requirement.txt
```
get `geckodriver` for your machine
```bash
chmod +x get_gecko.sh
./get_gecko.sh
```
I reccomend to set up a second email account to send the alerts from, as you may have to 'allow less secure app access' within google account settings.  

edit `example-config.py` and rename it to `config.py` so the scripts can read it.

Once configured you can test the email function works by running:
```bash
python3 test_email.py
```

## Usage
Example for sending an alert once a product size becomes avaliable on amazon. It willl check every 15 mins if the usb stick is availible in the 1tb size.
```py
product_url = "https://www.amazon.co.uk/SanDisk-Ultra-Flash-Drive-Read/dp/B083ZS4HYD/ref=psdc_430554031_t1_B07NS1Y9K3?th=1"

from Notipyer import check_amazon
sizes = check_amazon.get_sizes(product_url)
```
output:
```bash
Available sizes are:
  -  16 GB
  -  32 GB
  -  64 GB
  -  128 GB
  -  256 GB
  -  512 GB
  ```
[an email alert will be sent once the '1tb' option becomes avalible]
