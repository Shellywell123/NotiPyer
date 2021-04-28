##########################################
# foundations of a notification email bot
##########################################
#
# TODO list
#       make dummy email account for bot
#       create html scraper
#       create html searcher
#       find a way to continously run the script (on a pi ?)

def get_page_html_contents(url):
    """
    """
    # beautiful soup / requests

    # import requests
    # from bs4 import BeautifulSoup

    # response = requests.get(url) # will return 200 if allowed access    
    # html = BeautifulSoup(response.text, "html.parser") 

    from requests_html import HTMLSession
    from bs4 import BeautifulSoup
     
    # create an HTML Session object
    session = HTMLSession()
     
    # Use the object above to connect to needed webpage
    resp = session.get(url)
     
    # Run JavaScript code on webpage
    resp.html.render(sleep=1, keep_page=True)

    #print(resp.html.html)

    soup = BeautifulSoup(resp.html.html, "lxml")
    html = soup
#print(soup)
    return html


def notipy(rec_address,email_contents):
    """
    send email to rec_address contating email_contents
    """
    import smtplib, ssl

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "my@gmail.com"
    password = input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # TODO

################################################

product_url = "https://www.amazon.co.uk/SanDisk-Ultra-Flash-Drive-Read/dp/B083ZS4HYD/ref=psdc_430554031_t1_B07NS1Y9K3?th=1"

html = get_page_html_contents(product_url)
sizes = html.findAll('a')
for size in sizes:
    #if str(size)[:6]=='<li id':
    print(size)

# if product in stock then notipy