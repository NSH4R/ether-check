import requests
from bs4 import BeautifulSoup
import re
import json
from solc import compile_source

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def remove_comment(text):
    pattern = r"/\*\*.*?\*/"
    ctext = re.sub(pattern, '', text, flags=re.DOTALL)

    pattern = r"/\*.*?\*/"
    ctext = re.sub(pattern, '', ctext, flags=re.DOTALL)

    pattern = r"//.*?$"
    clean_text = re.sub(pattern, '', ctext, flags=re.MULTILINE)

    # clean_text = ctext.split('\n')
    #
    # while clean_text and clean_text[0].strip() == '':
    #     clean_text.pop(0)

    return clean_text


def get_code(url):
    response = requests.get(url, headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        pre_tags = soup.find('pre')
        for pre_tag in pre_tags:
            contract_code = pre_tag.get_text()
        return remove_comment(contract_code)
    else:
        raise ValueError(f"Failed to fetch contract source code from {url}")

def get_ast(url):
    compiled_code = compile_source(get_code(url))

    # Извлекаем AST из выходных данных JSON
    json_ast = json.loads(compiled_code)["contracts"]

    # Доступ к AST для каждого контракта
    for contract_name, contract_data in json_ast.items():
        ast = contract_data["abi"]

    return(ast)

get_ast('https://etherscan.io/address/0x4B274807e2Cf091eAFCe26390f7FBeC626D4b0ab#code')