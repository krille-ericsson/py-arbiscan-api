from arbiscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x2a65aca4d5fc5b5c859090a6c34d164135398226'

api = Account(address=address, api_key=key)
blocks = api.get_blocks_mined_page(page=1, offset=10000, blocktype='blocks')
print(blocks)
