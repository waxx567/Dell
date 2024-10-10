# Extract user name after given Twitter URL
# Imports regular expressions library
import re
# Asks user input and strips whitespace from answer
url = input("URL: ").strip()
# Validate input and print
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# Explained

# Asks user input and strips whitespace
''' url = input("URL: ").strip()'''
# A str in Python comes with method .replace() like .split() or .strip()
# The first argument is replaced by the second
''' username = url.replace("https://twitter.com/", '')
    print("Username: {username})'''
# Input: My username is https://twitter.com/davidmalan
# Output: Username: My username is davidmalan
''' username = url.removeprefix("https://twitter.com/")
    print("Username: {username})'''
# Input: My username is https://twitter.com/davidmalan
# Output: Username: My username is https://twitter.com/davidmalan

# Regex
# Imports regular expressions library
'''import re'''
# Asks user input and strips whitespace
'''url = input("URL: ").strip()'''
# re.sub(pattern, repl, string, count=0, flags=0)
# Meaning pattern to find, replacement string, string to substitute on, [last 2 not NB for now]
# Substitute domain name, put output in variable and print
''' username = re.sub(r"https://twitter.com/", '', url)
    print(f"Username: {username}")'''
# Put ^ to match from beginning of string but no $ because need to tolerate user name there
# Add a \ before the . so the . is taken literally
'''username = re.sub(r"^https://twitter\.com/", '', url)'''
# To tolerate http as well, put ? meaning 0 or 1 of the char before
'''username = re.sub(r"^https?://twitter\.com/", '', url)'''
# Also need to tolerate www. being there or not so
'''username = re.sub(r"^https?://(www\.)?twitter\.com/", '', url)'''
# People mostly don't type http:// or https:// so make them optional
''' username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", '', url)
    print(f"Username: {username}")'''
# The regex below taken from above now using search and adding .+$
# Put parentheses around the expression that denotes the user name
# So it can be found in a variable that is also assigned here
''' matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)'''
''' if matches:'''
# Walrus operator (:=) combines the 2 lines above into one
''' if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):'''
# The () around www\. means whatever it returns is matches.group(1) so
'''     print(f"Username:", matches.group(2))'''
# Not ideal so ?: at the beginning of () means don't capture this
''' if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):'''
# But .+ is a bit too tolerant as Twitter only accepts [a-zA-Z0-9_] so
'''if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
        print(f"Username:", matches.group(1))'''
# As above, so below