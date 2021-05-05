def get_sizes(product_url):
    """
    """
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver import Firefox

    import bs4
    import json

    # added by ben for wsl
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = True

    ff_opts = Options()
    ff_opts.add_argument("--headless")
    driver = webdriver.Firefox(options=ff_opts, executable_path="./geckodriver")

    # get page
    driver.get(product_url)

    # read source
    pagesrc = driver.page_source

    # quit driver
    driver.quit()

    # parse tree
    bs = bs4.BeautifulSoup(pagesrc, "html.parser")

    # filter buttons
    price_buttons = bs.findAll(
        lambda tag: tag.name == "li"
        and "id" in tag.attrs
        and "size_name_" in tag.attrs["id"]
    )


    if price_buttons:

        sizes = [tag.find("p").text for tag in price_buttons]

    else:

        datatag = bs.findAll(
            lambda tag: tag.name == "script"
            and "data-a-state" in tag.attrs
            and "dim-val-list" in tag.attrs["data-a-state"]
        )

        content = json.loads(datatag[0].contents[0])
        sizes = content["size_name"]

    print("Available sizes are:")
    for i in sizes:
        print("  - ", i)

    return sizes