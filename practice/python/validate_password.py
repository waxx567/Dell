# Check the validity of a password
# At least 1 [a-z] and 1 [A-Z]
# At least 1 [0-9]
# At least 1 [$@#%]
# 6 to 16 chars
# Examples of valid password: p@sSw0rd or p4s$wOrd
# https://en.wikipedia.org/wiki/Regular_expression for explanation of regular expressions

import re
password = input("Enter password: ")
invalid = True

while invalid:
    if 6 > len(password) > 16 or re.search(r"^(\w+ $@#%&)$", password):
        break
    else:
        print("Password OK")
        invalid = False

if invalid:
    print("Password not OK")