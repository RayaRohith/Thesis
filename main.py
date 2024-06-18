
from selenium import webdriver
import sys
from time import sleep

from dumputils import utils
from common import DEFAULT_FILTER
#from utils import 

i, url = sys.argv[1:3]
print(f'Visit {i} to {url}')
with webdriver.Firefox() as driver:
    sleep(2)
    site = url.split('//')[1].split('.')[0]
    fname = f'/home/mjuarezm/rep/uoc_crawler/web/results/{i}_{site}.pcap'
    with Sniffer(path=fname, filter=DEFAULT_FILTER):
        driver.get(url)
        sleep(5)
