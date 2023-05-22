import requests
from bs4 import BeautifulSoup
import solcx

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_code (url):
    response = requests.get((url), headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        pre_tags = soup.find('pre')
        for pre_tag in pre_tags:
            contract_code = pre_tag.get_text()
        return contract_code
    else:
        raise ValueError(f"Failed to fetch contract source code from {url}")
get_code('https://etherscan.io/address/0x4B274807e2Cf091eAFCe26390f7FBeC626D4b0ab')