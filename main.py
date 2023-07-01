import requests
from bs4 import BeautifulSoup
import re
import json
import solcx
import solcast
from solcx import compile_source


url = 'https://etherscan.io/address/0xA2f0A263410C4b045F26035190a3FC54215e0ee4#code'


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_code(url):
    response = requests.get(url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        pre_tags = soup.find('pre', class_='js-sourcecopyarea editor', id='editor', string=True)
        print(isinstance(pre_tags, str))
        return pre_tags
    else:
        raise ValueError(f"Failed to fetch contract source code from {url}")


def get_ast(code):
    output_json = solcx.compile_source(code)
    print(output_json)
    ast_node = solcast.from_standard_output(output_json)


get_ast(get_code('https://etherscan.io/address/0xA2f0A263410C4b045F26035190a3FC54215e0ee4#code'))

