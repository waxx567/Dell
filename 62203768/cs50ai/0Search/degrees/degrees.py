# The latest version of Python you should use in this course is Python 3.11, as newer versions of Python are not yet fully compatible with some Python modules used in this course.

# Complete the implementation of the shortest_path function such that it returns the shortest path from the person with id source to the person with the id target.
# Assuming there is a path from the source to the target, your function should return a list, where each list item is the next (movie_id, person_id) pair in the path from the source to the target. Each pair should be a tuple of two strings.
# For example, if the return value of shortest_path were [(1, 2), (3, 4)], that would mean that the source starred in movie 1 with person 2, person 2 starred in movie 3 with person 4, and person 4 is the target.
# If there are multiple paths of minimum length from the source to the target, your function can return any of them.
# If there is no possible path between two actors, your function should return None.
# You may call the neighbors_for_person function, which accepts a person’s id as input, and returns a set of (movie_id, person_id) pairs for all people who starred in a movie with a given person.
# You should not modify anything else in the file other than the shortest_path function, though you may write additional functions and/or import other Python standard library modules.

# While the implementation of search in lecture checks for a goal when a node is popped off the frontier, you can improve the efficiency of your search by checking for a goal as nodes are added to the frontier: if you detect a goal node, no need to add it to the frontier, you can simply return the solution immediately.
# You’re welcome to borrow and adapt any code from the lecture examples. We’ve already provided you with a file util.py that contains the lecture implementations for Node, StackFrontier, and QueueFrontier, which you’re welcome to use (and modify if you’d like).

import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person IDs
names = {}

# Maps person IDs to a dictionary of: name, birth, movies (a set of movie IDs)
people = {}

# Maps movie IDs to a dictionary of: title, year, stars (a set of person IDs)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set(),
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set(),
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs kthat connect the source to the target.

    If no possible path, returns None.
    """

    # Keep track of the number of states that have been explored
    num_explored = 0

    # Initialize the frontier to the starting position with the first actor's name
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    # Initialize an empty set for explored states
    explored = set()

    # Keep looping through the frontier until a solution found
    while True:

        # If nothing is left in the frontier, there is no path
        if frontier.empty():
            raise Exception("no solution")

        # Choose a node from the frontier
        node = frontier.remove()
        # Update the number of states that have been explored
        num_explored += 1

        # Add the node to the explored set
        explored.add(node.state)

        # Add the person's neighbours to the frontier
        # Loop through the neighbours
        for movie_id, person_id in neighbors_for_person(node.state):
            # If the state is not in the frontier and has not been explored
            if not frontier.contains_state(person_id) and person_id not in explored:
                # Assign the state to the child variable
                child = Node(state=person_id, parent=node, action=movie_id)

                # If this state is the goal state
                if child.state == target:
                    # Follow the parent nodes to find the solution ie. backtrack through the parent nodes until there is no parent node left in order to figure out which actions were taken to get to the goal state
                    # Initialize empty lists to track movies, people and the solution
                    movies = []
                    people = []
                    # Initialize an empty list for the tuples that comprise the solution
                    solution = []

                    # The following loop will look at the parent of every node and keep track of each of the parents, and of what action was taken to get from the parent node to the current node, until it reaches the first node, which has no parent
                    while child.parent is not None:
                        # Update the movies and people lists
                        movies.append(child.action)
                        people.append(child.state)
                        # Assign the parent node to the child variable
                        child = child.parent
                        # Return to the top of the while loop
                    # Once the lists are populated, reverse those lists - the order they are in is the result of backtracking - so that the sequence now runs chronologically ie. from the initial state to the goal state
                    movies.reverse()
                    people.reverse()
                    # Zip the lists into a new zipped list
                    zipped_list = zip(movies, people)
                    for movie, person in zipped_list:
                        # Update the solution list
                        solution.append((movie, person))
                    # Return a list, where each list item is the next (movie_id, person_id) pair in the path from the source to the target. Each pair will be a tuple of two strings
                    return solution

                # Add the new node to the frontier
                frontier.add(child)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
