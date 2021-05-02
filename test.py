from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefoxpoke


import bs4

ff_opts = Options()
ff_opts.add_argument("--headless")

driver = webdriver.Firefox(options=ff_opts, executable_path="./geckodriver")

product_url = "https://www.amazon.co.uk/SanDisk-Ultra-Flash-Drive-Read/dp/B083ZS4HYD/ref=psdc_430554031_t1_B07NS1Y9K3?th=1"

# get page
driver.get(product_url)

# read source
pagesrc = driver.page_source

# quit driver
driver.quit()

# parse tree
bs = bs4.BeautifulSoup(pagesrc, "html.parser")

# filter buttons
price_buttons = bs.findAll(lambda tag: tag.name == "li" and "id" in tag.attrs and "size_name_" in tag.attrs["id"])

sizes = [
    tag.find("p").text for tag in price_buttons
]

print("Available sizes are:")
for i in sizes: 
    print("  - ", i)