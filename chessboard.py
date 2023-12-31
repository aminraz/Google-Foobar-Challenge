import copy


class knight:
    """Create a class for knight in a chessboard."""

    def __init__(self, node=0):
        """Create a Knight instance."""
        self.y = node // 8
        self.x = node - 8 * (node // 8)

    def make_tuple(self):
        """Make a tuple from object."""
        return (self.x, self.y)

    def __eq__(self, other):
        """Define equivalence when location is the same."""
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """Print location of an object."""
        return "x = %d, y = %d" % (self.x, self.y)

    def neighbors(self):
        """Find the neighboring positions."""
        result = [
            (i + self.x, j + self.y) for i in [-2, 2] for j in [-1, 1]
        ]
        result += [
            (i + self.x, j + self.y) for j in [-2, 2] for i in [-1, 1]
        ]
        return result

    def update_queue(self, queue, prev, board):
        """Update the queue and prev lists.
        The 'queue' lists all nodes for checking
        and 'prev' is a dictionary for archiving their parent node.
        """
        locations = self.neighbors()
        for i in locations:
            if board.is_inside(*i) and (i not in queue):
                queue.append(i)
                prev[i] = self.make_tuple()

    def make_prev(self, board):
        """Build a list of parent nodes starting from self."""
        node = copy.copy(self)
        queue = [node.make_tuple()]
        prev = {}
        i = 0
        while True:
            node.update_queue(queue, prev, board)
            i += 1
            if i >= len(queue):
                break
            node.x = queue[i][0]
            node.y = queue[i][1]
        return prev

    def path_maker(self, destination, board):
        """Make the shortesat path between self and destination
        using prev dictionary."""
        if self == destination:
            return print("Your are already at your destination")
        prev = self.make_prev(board)
        path_length = 1
        while prev[destination.make_tuple()] != self.make_tuple():
            path_length += 1
            dis_reserved = copy.copy(destination)
            destination.x = prev[dis_reserved.make_tuple()][0]
            destination.y = prev[dis_reserved.make_tuple()][1]
        return path_length


class board:
    """Create chessboard."""

    def __init__(self, x=7, y=7):
        """Locate the length of the board."""
        self.x = x
        self.y = y

    def is_inside(self, x, y):
        """Check whether knight is inside the board."""
        return x >= 0 and x <= self.x and y >= 0 and y <= self.y


def solution(src, dest):
    """Give the least number of moves a knight needs
    to travel from 'src' to 'dest'."""
    i_loc = knight(src)
    o_loc = knight(dest)
    b = board()
    return i_loc.path_maker(o_loc, b)
