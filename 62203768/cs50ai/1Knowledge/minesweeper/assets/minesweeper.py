import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # If the number of cells equals the count and the count is greater than zero
        if len(self.cells) == self.count and self.count != 0:
            # All remaining cells must be mines
            return self.cells
        # If not, return an empty set
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # If the count is zero
        if self.count == 0:
            # All remaining cells must be safe
            return self.cells
        # If not, return an empty set
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # If the current cell is still in the sentence
        if cell in self.cells:
            # Remove the cell from the sentence
            self.cells.remove(cell)
            # Update the count and return
            self.count -= 1
            return

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # If the current cell is still in the sentence
        if cell in self.cells:
            # Remove the cell from the sentence and return
            self.cells.remove(cell)
            return


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        '''
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        '''
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Mark cell as move made
        self.moves_made.add(cell)
        # Mark cell as safe
        self.mark_safe(cell)

        # Set to store cells whose status is not known
        unknowns = set()

        # Loop over neighbouring rows and columns
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore if looking at original cell or if cell safe
                if (i, j) == cell or (i, j) in self.safes:
                    continue

                # If cell is known mine, update count
                if (i, j) in self.mines:
                    count -= 1
                # If cell within grid and not safe or mine, append it to list of unknowns
                if (0 <= i < self.height) and (0 <= j < self.width) and ((i, j) not in self.safes) and ((i, j) not in self.mines):
                    unknowns.add((i, j))

        # Update knowledge base with new Sentence
        self.knowledge.append(Sentence(unknowns, count))

        # Boolean indicates whether knowledge base has changed
        KB_changed = True

        # While there are changed
        while KB_changed:
            # Reset boolean
            KB_changed = False

            # Get safes and mines from knowledge base
            safes = set()
            mines = set()
            for sentence in self.knowledge:
                safes = safes.union(sentence.known_safes())
                mines = mines.union(sentence.known_mines())

            # Mark safes and mines
            if safes:
                KB_changed = True
                for safe in safes:
                    self.mark_safe(safe)
            if mines:
                KB_changed = True
                for mine in mines:
                    self.mark_mine(mine)

            # Remove empty sentences
            empty = Sentence(set(), 0)
            self.knowledge[:] = [x for x in self.knowledge if x != empty]

        # Check for any new conclusions based on latest knowledge

        for sentence_x in self.knowledge:
            for sentence_y in self.knowledge:
                # If sentences are identical
                if sentence_x == sentence_y:
                    continue

                # Create new Sentence based on new information
                if sentence_x.cells.issubset(sentence_y.cells):
                    new_cells = sentence_y.cells - sentence_x.cells
                    new_count = sentence_y.count - sentence_x.count
                    new_sentence = Sentence(new_cells, new_count)

                    # Add to knowledge base
                    if new_sentence not in self.knowledge:
                        KB_changed = True
                        self.knowledge.append(new_sentence)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Loop over known safe cells
        # If cell not in known moves, return it
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        # If no safe moves are possible
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        if len(self.moves_made) + len(self.mines) == self.height * self.width:
            return None

        while True:
            # Select random coordinates
            i = random.randrange(self.height)
            j = random.randrange(self.width)

            # Variable to store cell as single argument
            cell = (i, j)

            if cell not in self.moves_made and cell not in self.mines:
                return cell