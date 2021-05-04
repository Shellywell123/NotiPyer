# check url manually
product_url = "https://www.amazon.co.uk/SanDisk-Ultra-Flash-Drive-Read/dp/B083ZS4HYD/ref=psdc_430554031_t1_B07NS1Y9K3?th=1"

from NotiPyer import check_amazon
sizes = check_amazon.get_sizes(product_url)

# check url every 15 mins
from NotiPyer import auto_check
auto_check.repeat(product_url,15)