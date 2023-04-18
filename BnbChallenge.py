# For the Stake Cake Pool, which currently has > 250,000,000 CAKE staked to it, find the
#following information:
  #i. When was the current staking contract deployed onto mainnet? Please link to
  #the transaction in which it was deployed.
  
 # I begun by going to https://pancakeswap.finance/pools
# Then i went to: View Contract
# This took me to the LINK https://bscscan.com/address/0x45c54210128a065de780C4B0Df3d16664f7f859e#events
#0x73feaa1eE314F8c655E354234017bE2193C9E24E 
  
 # To find the transaction where it was deployed: 
 # I went to the LINK above, and went on the right handside where there is the Contract Creator section.
 # On the right, is the transaction hash:
 # https://bscscan.com/tx/0xc0e636dcebeeed30525f1ca2214b93331fe2263adc87cd467d57d4ff04257d4d
  
  #ii. Where can we find the ABI and the Source Code for this contract?
  
  # Source code: 
  # Going to the LINK above, I went to the contract tab, and went down to the Contract Source Code section. The code is all there

  # ABI
  # To find the ABI, I went to the same LINK and contract tab, and scrolled down the page 
  
  #d. Write a script in your preferred language:
    #i. To query all deposit events for this contract. You do not need to query all of
    #them, but your code should facilitate us to query all deposit transactions.
    #ii. To query the Total Staked Amount of Cake historically from an archive node for a
    #specific Block Number.


# d - I was not able to get an API Key so instead im using an endpoint


import requests
import json

HTTP_PROVIDER_URL = "https://yolo-nameless-telescope.bsc-testnet.discover.quiknode.pro/3a3d11f5caf47d9ddd3ac5577b93cabdcee83faa/"
STAKING_CONTRACT = "0x45c54210128a065de780C4B0Df3d16664f7f859e"

# ABI for deposit events
ABI = {
  "anonymous": false,
  "inputs": [
    {
      "indexed": true,
      "internalType": "address",
      "name": "sender",
      "type": "address"
    },
    {
      "indexed": false,
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    },
    {
      "indexed": false,
      "internalType": "uint256",
      "name": "shares",
      "type": "uint256"
    },
    {
      "indexed": false,
      "internalType": "uint256",
      "name": "duration",
      "type": "uint256"
    },
    {
      "indexed": false,
      "internalType": "uint256",
      "name": "lastDepositedTime",
      "type": "uint256"
    }
  ],
  "name": "Deposit",
  "type": "event"
}

# Query deposit events
def query_deposit_events(from_block, to_block):
    url = f"https://bsc.getblock.io/mainnet?api_key={API_KEY}"
    headers = {"Content-Type": "application/json"}

    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_getLogs",
        "params": [
            {
                "address": STAKING_CONTRACT,
                "fromBlock": hex(from_block),
                "toBlock": hex(to_block),
                "topics": ["0x67d66f160bc93d92563fac76c9bce11a23dd68a369b576f1b941d5c7a17e3c3a"]
            }
        ]
    }
    response = requests.post(HTTP_PROVIDER_URL, json=data, headers=headers)
    result = json.loads(response.text)["result"]
    return result

# Query total staked amount at a specific block
def query_total_staked_amount(block_number):
    url = f"https://bsc.getblock.io/mainnet?api_key={API_KEY}"
    headers = {"Content-Type": "application/json"}

    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_call",
        "params": [
            {
                "to": STAKING_CONTRACT,
                "data": "0x7a9d506e"
            },
            hex(block_number)
        ]
    }
    response = requests.post(HTTP_PROVIDER_URL, json=data, headers=headers)
    result = int(json.loads(response.text)["result"], 16)
    return result

# Example usage
deposit_events = query_deposit_events(0, "latest")

# Replace 0 with the desired block number
desired_block_number = 0
total_staked_amount = query_total_staked_amount(desired_block_number)

# You can print the results for better understanding
print("Deposit events:", deposit_events)
print(f"Total staked amount at block {desired_block_number}:", total_staked_amount)
