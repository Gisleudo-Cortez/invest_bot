import time
from selenium import webdriver


indexes_urls = {
    'ifiz':'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IFIX?language=pt-br',
    'ibov':'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
}


options = webdriver.ChromeOptions()

options.add_experimental_option("prefs", {
            "download.default_directory": "/home/falcon/Documents/workspace/python/invest_bot/src/data",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })


browser = webdriver.Chrome(chrome_options=options)

for index in indexes_urls:
    browser.get(indexes_urls[index])
    time.sleep(3)
    browser.find_element_by_link_text('Download').click()
    time.sleep(3)

browser.close()