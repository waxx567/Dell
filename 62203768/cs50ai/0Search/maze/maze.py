
'''
An implementation of the idea of maze solving.
'''

import sys

# Keep track of the current state, the previous state, and the action to be taken
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

'''StackFrontier and QueueFrontier classes each create an object that is able to store frontier data with functions - known as methods on that object - that can be used to manipulate the object.'''


# Implement a frontier as a stack ie. last in, first out data structure
class StackFrontier():

    # Create a frontier as an empty list initially
    def __init__(self):
        self.frontier = []

    # Add items to the frontier by appending them to the end of the list
    def add(self, node):
        self.frontier.append(node)

    # Check if the frontier contains a particular state
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    # Check if the frontier is empty
    def empty(self):
        return len(self.frontier) == 0

    # Remove items from the frontier
    def remove(self):
        # Check if the frontier is empty and raise an exception if it is
        if self.empty():
            raise Exception("empty frontier")
        # If the frontier is not empty
        else:
            # Assign the last item on the frontier list to a variable called node
            node = self.frontier[-1]
            # Remove that last item from the frontier list
            self.frontier = self.frontier[:-1]
            # Return the new node
            return node


# Implement a frontier as a queue ie. first in, first out data structure
class QueueFrontier(StackFrontier):
    '''Inherits from the stack frontier except the remove() method differs. Instead of items being removed from the end of the list, they will be removed from the beginning of the list.'''

    def remove(self):
        # Check if the frontier is empty and raise an exception if it is
        if self.empty():
            raise Exception("empty frontier")
        # If the frontier is not empty
        else:
            # Name the first item on the frontier list to a variable called node
            node = self.frontier[0]
            # Remove the first item from the frontier list
            self.frontier = self.frontier[1:]
            # Return the new node
            return node


# Interprets a maze-like text file and figures out how to solve it
class Maze():

    def __init__(self, filename):

        # Read the file and set the height and width of the maze
        with open(filename) as f:
            contents = f.read()

        # Validate the start and goal points
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determine the height and width of the maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of the walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    # Print the solution
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end='')
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()


    # Keep track of the neighbours
    def neighbors(self, state):
        row, col = state

        # All possible actions
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Ensure the actions are valid
        result = []
        for action, (r, c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action, (r, c)))
            except IndexError:
                continue
        return result


    # Find a solution to the maze if one exists
    # Figures how to get from point A to point B
    def solve(self):

        # Keep track of how many states have been explored
        self.num_explored = 0

        # Initialize the frontier to a starting position
        # Define a node that represents the start state
        start = Node(state=self.start, parent=None, action=None)
        # Choose either StackFrontier or QueueFrontier
        frontier = StackFrontier()
        # Initially, this frontier is going to contain the start state only
        frontier.add(start)

        # Initialize an explored set which is empty initially because nothing has been explored yet
        self.explored = set()

        # Keep looping through the frontier until a solution found
        while True:

            # Check if the frontier is empty and raise an exception if it is
            if frontier.empty():
                raise Exception("no solution")

            # If the frontier is not empty
            # Remove a node from the frontier
            node = frontier.remove()
            # Update the number of states that have been explored by adding 1 to the total as this one is now being explored
            self.num_explored += 1

            # If the state of this node is equal to the goal state
            if node.state == self.goal:
                # Follow the parent nodes to find the solution ie. backtrack through the parent nodes until there is no parent node left in order to figure out which actions were taken to get to the goal state
                # Initiate an empty list to store all of the actions taken
                actions = []
                # Initiate an empty list to store all of the cells explored
                cells = []

                # The following loop will look at the parent of every node and keep track of each of the parents, and of what action was taken to get from the parent node to the current node, until it reaches the first node, which has no parent
                while node.parent is not None:
                    # Update the lists
                    actions.append(node.action)
                    cells.append(node.state)
                    # Assign the parent node to the node variable
                    node = node.parent
                    # Return to the top of the while loop
                # Once the lists are populated, reverse those lists - the order they are in is the result of backtracking - so that the sequence now runs chronologically ie. from the initial state to the goal state
                actions.reverse()
                cells.reverse()
                # Update the solution to include the new information and return the solution as the goal
                self.solution = actions, cells
                return

            # If the state of this node is not equal to the goal state
            # Add the state to the explored set so that it does not get explored again
            self.explored.add(node.state)

            # Add neighbours to the frontier
            # Loop through all of the node's neighbours
            for action, state in self.neighbors(node.state):
                # If the neighbour state is not in the frontier and has not already been explored
                if not frontier.contains_state(state) and state not in self.explored:
                    # Define a node called child that represents this neighbour state
                    child = Node(state=state, parent=node, action=action)
                    # Add the new node to the frontier
                    frontier.add(child)


    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = 90, 171, 8

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                      fill=fill
                )

        img.save(filename)


if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze: ")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze.png", show_explored=True)





