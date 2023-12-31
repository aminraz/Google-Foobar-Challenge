def append_prime_list(prime_list, n):
    """Return wether the n is prime or not."""
    """Additionaly, it updates the list of prime numbers up to n. 
    To speed up the process, only prime numbers up to n**.5 are checked."""

    for i in prime_list:
        if i > n**0.5 + 1:
            prime_list.append(n)
            return True
        else:
            if n % i == 0:
                return False
    prime_list.append(n)
    return True


def listprime():
    """Find prime numbers and concatenate in a string."""
    num = 3
    p_list = [2]
    s_prime = "2"
    while len(s_prime) < 10005:
        check_prime = append_prime_list(p_list, num)
        if check_prime:
            s_prime += str(num)
        num += 1
    return s_prime


id_string = listprime()


def solution(n):
    """Provide IDDs from the string of prime numbers."""
    global id_string
    if n > 10000 or n < 0:
        return "Input should be between 0 to 1000 (inclusive)"
    return id_string[n : n + 5]
