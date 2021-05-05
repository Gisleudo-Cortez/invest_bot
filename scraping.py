import time
from selenium import webdriver
from loguru import logger
from selenium.common.exceptions import WebDriverException 
import sys

logger.add(sys.stderr, format="{time} - {level} - {message}", filter="my_module", level="INFO")


indexes_urls = {
    'ifiz':'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IFIX?language=pt-br',
    'ibov':'https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br'
}

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu') 
options.headless = True

options.add_experimental_option("prefs", {
            "download.default_directory": "/home/falcon/Documents/workspace/python/invest_bot/data",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })


browser = webdriver.Chrome(chrome_options=options)

def extract_files():
    for index in indexes_urls:
        logger.info(f'Extraindo: {index}')
        try:
            browser.get(indexes_urls[index])
            time.sleep(3)
            browser.find_element_by_link_text('Download').click()
            time.sleep(3)
        except WebDriverException as e:
            logger.error(f'Erro ao extratir {index} - Erro: {e}')
        logger.success(f'{index} - Extracao Finalizada')
    browser.close()