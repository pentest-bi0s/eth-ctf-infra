import os
import subprocess

USER_ETH_BALANCE = int(os.getenv("USER_ETH_BALANCE", "0"))
SETUP_ETH_BALANCE = int(os.getenv("SETUP_ETH_BALANCE", "0"))
EXTRA_BALANCE = int(1e18) 

total_wei = USER_ETH_BALANCE + SETUP_ETH_BALANCE + EXTRA_BALANCE
total_eth = total_wei / 1e18


subprocess.run([
    "anvil",
    "-a", "1",
    "--balance", str(int(total_eth)),
    "--host", "0.0.0.0"
])