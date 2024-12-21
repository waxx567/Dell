# Introducing functions doesn't change anything but gives us more control
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    # name = input("Name: ")
    # return name
    # or better
    return input("Name: ")


def get_house():
    # house = input("House: ")
    # return house
    return input("House: ")


if __name__ == "__main__":
    main()