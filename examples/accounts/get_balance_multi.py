from arbiscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = ['0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a',
           '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a']

api = Account(address=address, api_key=key)
balances = api.get_balance_multiple()
print(balances)
