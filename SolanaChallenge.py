# Imports were a bit complicated because Solana and Solders packages are intertwined 

import json
import base58
from typing import List, Union

from solders.rpc.requests import GetProgramAccounts
from solders.rpc.filter import Memcmp
from solders.rpc.config import RpcProgramAccountsConfig, RpcAccountInfoConfig
from solana.rpc.api import Client
from solders.pubkey import Pubkey


# i. Finding the latest block:
solana_client = Client("https://api.mainnet-beta.solana.com")
latest_block = solana_client.get_latest_blockhash()
print(f"Latest block: {latest_block}")


# ii. Get a list of all Validators (or subset, but logic in code to get all)
validators_response = solana_client.get_vote_accounts()
validators = validators_response.value.to_json()

validators = json.loads(validators)
validators = validators['current']

print(validators)

# iii. First step was finding the largest validator:
# I used the above code to find the following

largest_validator = max(validators, key=lambda x: x['activatedStake'])
print("Largest validator:")
print(largest_validator)

# This prints out a few things, including the answer - 'votePubkey': 'DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a'
# This is corroborated by 'https://marinade.finance/validators/details/?vote_account=DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a'
# This validator has the highest active stake.

# I really struggled to get the list of delegators for this validator, trying lots of complicated code. 
# Then, i found the CLI command to get it instead: 

# This is the command: solana stakes DumiCKHVqoCQKD8roLApzR5Fit8qGV5fVQsJV9sTZk4a




