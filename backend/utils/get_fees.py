import json
import requests

from dotenv import dotenv_values
from pocketbase import PocketBase 


# instantiate pb client
# authenticate admin user
# return instance for use
pb_url = dotenv_values('.env').get('PB_URL')
admin_user = dotenv_values('.env').get('PB_ADMIN_USERNAME')
admin_password = dotenv_values('.env').get('PB_ADMIN_PASSWORD')
pb = PocketBase(pb_url)
pb.admins.auth_with_password(admin_user, admin_password)

# https://blockstream.info/api/mempool
# api call to blockstream server:
response = requests.get('https://blockstream.info/api/fee-estimates')
response_data = json.loads(response.text)

to_store = ['1','3','6','20']

for target_block in to_store:
    fee_rate = response_data.get(target_block)
    pb.collection("fee_data").create(
        { 
            "target_blocks" : target_block, 
            "fee_rate": fee_rate 
        }
    )