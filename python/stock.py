# Parsing data without csv module
'''
path = "GOOG.csv"
lines = [line for line in open(path)]
print(lines[0], end='') # Date,Open,High,Low,Close,Adj Close,Volume
# Each line is a single string with a newline symbol on the end of it
# Split into separate strings and put that in a variable
dataset = [line.strip().split(',') for line in open(path)]
print(dataset[1], end='')
# ['2021-11-15', '150.000000', '150.477005', '148.652496', '149.388000', '149.388000', '16248000']
# Which is still just a list of strings
'''
# Now with csv module
from datetime import datetime
import csv
path = "GOOG.csv"
''''
file = open(path, newline='')
reader = csv.reader(file)
'''
# OR
reader = csv.reader(open(path, newline=''))
header = next(reader)   # The 1st line contains the headers
'''
data = [row for row in reader]
print(header)
# ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
print(data[0])
# ['2021-11-15', '150.000000', '150.477005', '148.652496', '149.388000', '149.388000', '16248000']
# Still all in string format
'''
# So
# Create empty list
data = []
# Iterate over lines in read file
for row in reader:
    # row = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    date = datetime.strptime(row[0], f"%Y-%m-%d")
    # strptime short for stringparsetime(1st arg: string, 2nd arg: expected format)
    # Next, convert the open, high, low, close and adj close strs to floats
    # Using open_price as open is a builtin function in Python
    open_price = float(row[1])
    # Price the stock opened at
    high = float(row[2])
    # Highest price of the stock that day
    low = float(row[3])
    # Lowest price of the stock that day
    close = float(row[4])
    # Price the stock closed at
    adj_close = float(row[5])
    # Alternative adjusted close
    volume = int(row[6])
    # The number of shares of stock traded that day
    # Append list containing these values to data list
    data.append([date, open_price, high, low, close, adj_close, volume])
# Print first row
print(data[0])