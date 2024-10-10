# For else & while else

search = [1, 2, 3, 4, 5, 6, 7]
target = 7

# If
'''
for element in search:
    if element == target:
        print("I found it!")
        break
'''
# But you don't know if break because element found or because ran out of elements to look thru
# So
'''
found = False
for element in search:
    if element == target:
        print("I found it!")
        found = True
        break
if not found:
    print("I didn't find it!")
'''
# Try this:
for element in search:
    if element == target:
        print("I found it!")
        break
else:
    print("I didn't find it!")
# else will be triggered if we get thru for loop without breaking
# Same with a while loop
i = 0
while i < len(search):
    element = search[i]
    if element == target:
        print("I found it!")
        break
    i += 1
else:
    print("I didn't find it!")