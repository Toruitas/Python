__author__ = 'Stuart'

# pg 11. Since n*n%2==0 for evens, and boolean False == 0... this if not n*n%2 means: if not False
even_squares = [n*n for n in range(1, 11) if not n*n % 2]

