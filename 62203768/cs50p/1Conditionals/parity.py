#x = int(input("x: "))

#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

def main():
    x = int(input("x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
# Try these 4 lines following:
    #if n % 2 == 0:
    #   return True
    #else:
    #    return False
# Or this 1:
    #return True if n % 2 == 0 else False
# Or this 1
    return n % 2 == 0

main()