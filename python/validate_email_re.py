# This

import re

email = input("Email: ").strip()
print("Valid") if re.search(r"^\w+@(\w+\.)?\w+\.edu$",
                            email, re.IGNORECASE) else print("Invalid")

# Explained

# https://en.wikipedia.org/wiki/Regular_expression for explanation of expressions
# Validate user's .edu email address
# Get user input
# email = input("Email: ").strip()
# These two lines
'''username, domain = email.split('@')
print("Valid") if username and '.edu' in domain else print("Invalid")
# Meaning if there is a username and if domain has a . in it'''
# Are the same as these two
'''if '@' or ".edu" in email:'''
# Terminal input: malan@harvard.edu comes back valid for these an every subsequent variation
# Using regular expressions
#import re
# We start by searching for the @ on line 20
'''if re.search('@', email):'''
# Then add a . before - meaning any char except a newline
'''if re.search('.@', email):'''
# We add a * - meaning 0 or more repetitions and do the same on the other side of the @
'''if re.search(".*@.*", email):'''
# But 1 or more repetitions would be better and + is the re for that
'''if re.search(".+@.+", email):'''
# Add another . each side so not just one letter
'''if re.search("..+@..+", email):'''
# Now ha @ ha is valid but if you just add .edu
'''if re.search("..+@..+.edu", email):'''
# The re library will see the . as a re so malan@harvard?edu would be valid
# We need to add a \ which in re means to treat the char following as it really is
# But \ means something else to Python so Python must be told about that
# Hence the r (raw string) before the start of the string
'''if re.search(r"..+@..+\.edu", email):'''
# The next 2 symbols ^ means matches the start of string and $ the end
# So the user inputs an email address only, ie. exact match
'''if re.search(r"^..+@..+\.edu$", email):'''
# Now we need to handle multiple @'s so malan@@@@@harvard.edu becomes invalidated
# The meanings of the 1st ^, the $, the + and the \ with the r stay the same
# We remove the .'s and replace them with [^@] meaning any char except @
# So [@] would mean only @ and [@#$%&adrkhfu] would mean those. Put ^ in front to exclude
# So everything to the left of + can be any char but @
'''if re.search(r"^[^@]+@[^@]+\.edu$", email):'''
# The code so far is only tolerant of the @
# How to specify other stuff
# Only upper and lower case letters, numbers and underscores in the address
'''if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu$", email):'''
# Have not used ^ symbol at the beginning of this set, specifying not excluding
# That set [a-zA-Z0-9_] is so common it is abbreviated to \w so
'''if re.search(r"^\w+@\w+\.edu$", email):'''
# But this would accept MALAN@HARVARD.edu
# The re.search method comes with a 3rd argument called flags so
'''if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE)'''
# Some addresses have multiple dots in the domain name (subdomains) as per malan@cs50.harvard.edu
# Adding another \w+\. says allow for other word number underscore chars and a literal .
'''if re.search(r"^\w+@\w+\.\w+\.edu$", email, re.IGNORECASE)'''
# But that means we now HAVE to have a subdomain name
# We want to specify that  part of this package is optional
# Adding parentheses around this newly added expression separates the thought
'''if re.search(r"^\w+@(\w+\.)\w+\.edu$", email, re.IGNORECASE)'''
# Adding a ? after the parentheses means whatever is in them can repeat 0 or 1 times
# Could use * (meaning 0 or more) instead of ? if expecting more than 1
'''if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE)
    print("Valid")
else:
    print("Invalid")'''
# But I prefer this below to replace the last 3 lines
# print("Valid") if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE) else print("Invalid")
# As above, so below

# If you wanted to add to the .edu
'''if re.search(r"^\w+@\w+\.(edu|com|gov|org)$", email):'''
# If you wanted to tolerate whitespace
'''if re.search(r"^(\w\s)+@\w+\.(edu|com|gov|org)$", email):'''