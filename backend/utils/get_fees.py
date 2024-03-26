# using requests
from dotenv import dotenv_values
import json
import requests

# Set up your Bitcoin Core RPC connection
rpc_user = dotenv_values('.env').get('RPC_USER')
rpc_password = dotenv_values('.env').get('RPC_PASSWORD')
rpc_url = "http://localhost:8332"

# Define the parameters for the estimateSmartFee RPC call
def get_feerate(conf_target, estimate_mode):
    # Build the JSON-RPC request
    request_data = {
        "jsonrpc": "1.0",
        "method": "estimatesmartfee",
        "params": [conf_target, estimate_mode]
    }

    # Send the request and parse the JSON response
    response = requests.post(rpc_url, json.dumps(request_data), auth=(rpc_user, rpc_password))
    
    print(response.text)

    feerate =  json.loads(response.text).get('result').get('feerate')
    return feerate

confirm_targets = [1,3,6,20]

for block_num in confirm_targets:
    result = get_feerate(block_num, "CONSERVATIVE")
    
    # store data now, needs pocketbase to work
    print(result)




# using a library
# from bitcoinrpc import BitcoinRPC
# import asyncio

# from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# # establish rpc connection to local node
# def connect():
#     return \
#         BitcoinRPC.from_config(
#             "http://localhost:8332", 
#             ( 
#                 dotenv_values('.env').get('RPC_USER'), 
#                 dotenv_values('.env').get('RPC_PASSWORD') 
#             ) 
#         )

# async def main():
#     rpc = connect()
#     async with rpc:
#         fee_info = await rpc.estimatesmartfee(6)  
#         print(fee_info)

# if __name__ == "__main__":
#     asyncio.run(main())

# # can use subprocess
# # bitcoin-cli estimatesmartfee 6