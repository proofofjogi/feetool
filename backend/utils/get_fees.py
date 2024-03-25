# using requests
from dotenv import dotenv_values
import json
import requests

# Set up your Bitcoin Core RPC connection
rpc_user = dotenv_values('.env').get('RPC_USER')
rpc_password = dotenv_values('.env').get('RPC_PASSWORD')
rpc_url = "http://localhost:8332"

# Define the parameters for the estimateSmartFee RPC call
conf_target = 6
estimate_mode = "CONSERVATIVE"

# Build the JSON-RPC request
request_data = {
    "jsonrpc": "1.0",
    "id": "your_request_id",
    "method": "estimatesmartfee",
    "params": [conf_target, estimate_mode]
}

# Send the request and parse the JSON response
response = requests.post(rpc_url, json.dumps(request_data), auth=(rpc_user, rpc_password))
result = json.loads(response.text)

# Print the estimated fee rate in BTC/kB
print(result)
# print(f"Estimated fee rate: {result['feerate']} BTC/kB")


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