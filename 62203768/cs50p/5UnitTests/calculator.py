def main():
    x = int(input("Number: "))
    print("Number squared is", square(x))

def square(n):
    return n * n
# change the ^ multiplication sign (*) above to a plus sign


''' Do the following pro-actively to make sure that when you import your square function from another file, main itself is not called automatically '''
if __name__ == "__main__":
    main()