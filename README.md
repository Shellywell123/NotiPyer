# NotiPyer
Python 3 email bot for notifications 
  - current uses are for checking avaliable sizes of a product on amazon
  - email bot feature in development

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
## Usage
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
