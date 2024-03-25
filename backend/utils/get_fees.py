# using requests
from dotenv import dotenv_values
import json
import requests

# Set up your Bitcoin Core RPC connection
rpc_user = dotenv_values('.env').get('RPC_USER')
rpc_password = dotenv_values('.env').get('RPC_PASSWORD')
rpc_url = "http://localhost:8332"

# Define the parameters for the estimateSmartFee RPC call
def call(conf_target, estimate_mode):
    # Build the JSON-RPC request
    request_data = {
        "jsonrpc": "1.0",
        "id": "your_request_id",
        "method": "estimatesmartfee",
        "params": [conf_target, estimate_mode]
    }

    # Send the request and parse the JSON response
    response = requests.post(rpc_url, json.dumps(request_data), auth=(rpc_user, rpc_password))

    feerate =  json.loads(response.text).get('result').get('feerate')
    return feerate

high_p = call(1, "CONSERVATIVE") 
medium_p = call(6, "CONSERVATIVE")
low_p = call(20, "CONSERVATIVE")



print(high_p, medium_p, low_p)
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