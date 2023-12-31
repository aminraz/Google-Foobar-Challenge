def comb(num_list, l):
    """Find all combinations of numbers from num_list with the length l."""
    """Order is not important."""
    comb_list = []

    def find_comb(start, path):
        """Loop through the list."""
        # This is a recursive function.
        # Every combination is stored as a tuple in comb_list.
        if l == len(path):
            comb_list.append(tuple(path))
            return
        """In this foor loop, we advance to the next entry
        in the list and start from the new position. We 
        do the same thing over and over again
        until we reach the length of l til the end of the list."""
        for i in range(start, len(num_list)):
            find_comb(i + 1, path + [num_list[i]])

    find_comb(0, [])
    return comb_list


def multiple(n):
    """Determine wether n is divisable by 3."""
    if sum(n) % 3 == 0:
        return True
    else:
        return False


def solution(num):
    for i in range(0, len(num)):
        # We start by the longest list from the num.
        comb_list = comb(num, len(num) - i)
        codes = []
        for j in range(0, len(comb_list)):
            if multiple(comb_list[j]):
                codes.append(sorted(comb_list[j], reverse=True))
        if codes:
            return int("".join(map(str, max(codes))))
    if not codes:
        return 0
