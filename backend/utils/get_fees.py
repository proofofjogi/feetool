# get fees from an RPC connection
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Get RPC credentials from environment variables
rpc_user = env_vars.get('RPC_USER')
rpc_password = env_vars.get('RPC_PASSWORD')

print(rpc_user, rpc_password)