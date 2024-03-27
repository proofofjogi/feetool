# this implementation uses requests
import json
import requests
from dotenv import dotenv_values
from pocketbase import PocketBase 

# Set up your Bitcoin Core RPC connection
rpc_url = dotenv_values('.env').get('RPC_URL')
rpc_user = dotenv_values('.env').get('RPC_USERNAME')
rpc_password = dotenv_values('.env').get('RPC_PASSWORD')

# Define the parameters for the estimateSmartFee RPC call
def get_feerate(conf_target, estimate_mode):
    # Build the JSON-RPC request
    request_data = {
        "jsonrpc": "1.0",
        "method": "estimatesmartfee",
        "params": [conf_target, estimate_mode]
    }
    # Send the request and parse the JSON response
    response = requests.post(
        rpc_url, json.dumps(request_data), auth=(rpc_user, rpc_password)
    )

    # return feerate
    btc_feerate = json.loads(response.text).get('result').get('feerate')
    # convert btc/kbyte to sats/vbyte
    sat_feerate = btc_feerate * 100000000 / 1000
    sat_feerate = int(sat_feerate)
    return sat_feerate


# instantiate pb client
# authenticate admin user
# return instance for use
pb_url = dotenv_values('.env').get('PB_URL')
admin_user = dotenv_values('.env').get('PB_ADMIN_USERNAME')
admin_password = dotenv_values('.env').get('PB_ADMIN_PASSWORD')
pb = PocketBase(pb_url)
pb.admins.auth_with_password(admin_user, admin_password)


# blocks to store fees for
confirm_targets = [1,3,6,20]
fee_data = []
for block_num in confirm_targets:
    # get data from core rpc, conservative estimate:
    fee_rate = get_feerate(
        block_num, "CONSERVATIVE"
    )
    # store data
    pb.collection("fee_data").create(
        {"target_blocks" : block_num, "fee_rate": fee_rate, "type": "CONSERVATIVE"}
    )

    # get data from core rpc, economical estimate:
    fee_rate = get_feerate(
        block_num, "ECONOMICAL"
    )
    # store data
    pb.collection("fee_data").create(
        {"target_blocks" : block_num, "fee_rate": fee_rate, "type": "ECONOMICAL"}
    )

