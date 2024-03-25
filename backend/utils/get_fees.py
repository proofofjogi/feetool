# get fees from an RPC connection
from dotenv import dotenv_values
from bitcoinrpc import BitcoinRPC
import asyncio

# Load environment variables from .env file
env_vars = dotenv_values('.env')



# Get RPC credentials from environment variables
rpc_user = env_vars.get('RPC_USER')
rpc_passwd = env_vars.get('RPC_PASSWORD')


rpc = BitcoinRPC.from_config("http://localhost:8332", (rpc_user, rpc_passwd))


async def main():
    async with rpc:
        print(await rpc.getconnectioncount())

if __name__ == "__main__":
    asyncio.run(main())
