# Import library for access to command-line
import sys

def main():
    # Validate command-line input
    check_cl_args( )
    # Try to open
    try:
        with open(f"{sys.argv[1]}", "r") as file:
            # Loop through lines and eliminate non code
            line_list = file.readlines()
        # Variable to store count of lines of code
        count = 0
        for line in line_list:
            if not check_lines(line):
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

# Function to check command-line arguments
def check_cl_args():
    # Check argument count
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check it is a Python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_lines(line):
    return True if line.isspace() or line.strip().startswith('#') else False


if __name__ == "__main__":
    main()