#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title ETH Gas
# @raycast.mode silent
#
# Optional parameters:
# @raycast.icon ⛽️
# @raycast.packageName Ethereum
#
# Documentation:
# @raycast.description Check the live Ethereum gas price from Etherscan
# @raycast.author Nicholas Charriere
# @raycast.authorURL https://twitter.com/nichochar

import sys
import requests 


if __name__ == '__main__':
    response = requests.get('https://gas.best/stats')
    data = response.json()
    live = f"{data['pending']['fee']} gwei"
    one_hour = f"{data['forecast']['1 hour']} gwei"

    result = f"{live} ⏰ ${one_hour} estimated in one hour"
    print(result)
    sys.exit(0)
