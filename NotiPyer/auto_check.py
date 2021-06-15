import threading
from NotiPyer import check_amazon

def new_size(sizes,search_sizes):
  """
  """
  for size in search_sizes:
    if size in sizes:
        print('instock!')

        email_contents= {
        'subject' : "NotiPyer Amazon Alert",
        'body'    : ' the sandisk 1tb usb is now avaliable',
        }

        return [True,email_contents]

   return [Fasle,0]
        

def repeat(product_url,check_every_N_mins):
  """
  """
  minute = 60
  threading.Timer(check_every_N_mins*minute, printit).start()

  # check url - currenlty using amazon example
  sizes = check_amazon.get_sizes(product_url)  

  # set condition/s
  search_sizes = ['1 TB','1000 GB']
  condition = new_size(sizes,search_sizes)

  if condition[0] == True:
    # then email 
    from NotiPyer import email
    email_contents = condition[1]
    email.send_email(email_contents)


  
