from arbiscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x49edf201c1e139282643d5e7c6fb0c7219ad1db7'

api = Account(address=address, api_key=key)
transactions = api.get_all_transactions(offset=10000, sort='asc',
                                        internal=False)

print(transactions[0])
