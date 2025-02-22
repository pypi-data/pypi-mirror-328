from ooga_booga_python.models import SwapParams

from .client import OogaBoogaClient
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

async def main():
    client = OogaBoogaClient(
        api_key=os.getenv("OOGA_BOOGA_API_KEY"),
        private_key=os.getenv("PRIVATE_KEY")
    )

    TOKEN_IN = "0xFCBD14DC51f0A4d49d5E53C2E0950e0bC26d0Dce"  # HONEY MAINNET
    TOKEN_OUT = "0x6969696969696969696969696969696969696969"  # wBEAR MAINNET
    EXECUTOR = "0xa154CCD02848068ceC1c16B3126EBb2BE73553Ed"
    BURNER_ADDY = "0x376FE9E861201112B87B3131c04E6D85AD204Fb0"

    swapParams = SwapParams(
        tokenIn=TOKEN_IN,
        amount=1000000000,
        tokenOut=TOKEN_OUT,
        to=BURNER_ADDY
    )

    await client.approve_allowance(TOKEN_IN)
    # await client.swap(swapParams)

    # # Example: Fetch token list
    # tokens = await client.get_token_list()
    # for token in tokens:
    #     print(f"Name: {token.name}, Symbol: {token.symbol}")

asyncio.run(main())