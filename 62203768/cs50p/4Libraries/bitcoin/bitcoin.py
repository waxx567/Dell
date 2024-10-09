# Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

# import libraries
import requests
import sys

# get value from command-line
# command-line argument count is 2
if len(sys.argv) == 2:
    # if second argument is a number
    try:
        value = float(sys.argv[1])
    # if second argument is not a number
    except:
        print("Command--line argument is not a number")
        sys.exit(1)
# if no second argument
else:
    print("Missing command-line argument")
    sys.exit(1)

# get current Bitcoin price and multiply by argv[1]
# try/except block handles exceptions
try:
    # request from website
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # variable points to json file within the website
    response = r.json()
    # refine search for information required
    bitcoin = response["bpi"]["USD"]["rate_float"]
    # calculate total by multiplying amount of coins wanted by current price of Bitcoin
    total_price = bitcoin * value
    # print answer
    print(f"${total_price:,.4f}")
# if try fails
except requests.RequestException:
    print("RequestException")
    sys.exit(1)