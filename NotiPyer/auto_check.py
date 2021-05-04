import threading
from NotiPyer import check_amazon

def repeat(product_url,check_every_N_mins):
  """
  """
  minute = 60
  threading.Timer(check_every_N_mins*minute, printit).start()

  # check url - currenlty using amazon example
  sizes = check_amazon.get_sizes(product_url)  

  #if case == True:
  #  email me 
  cases = ['1 TB','1000 GB']
  for case in cases:
    if case in sizes:
        print('instock!')
        # then email 
