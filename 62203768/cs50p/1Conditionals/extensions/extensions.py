''' 
In a file called extensions.py, implement a program that prompts the user
for the name of a file and then outputs that file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.
'''

# Prompt user
name = input("Name of file: ").strip().lower()

# Parse input
ext = name.split(".")

# Validate and output
if ext[-1] in ["jpg", "jpeg"]:
    print("image/jpeg")
if ext[-1] in ["gif", "png"]:
    print(f"image/{ext[-1]}", end="")
elif ext[-1] in ["pdf", "zip"]:
    print(f"application/{ext[-1]}")
elif ext[-1] in ["txt"]:
    print(f"text/plain")
else:
    print("application/octet-stream")
