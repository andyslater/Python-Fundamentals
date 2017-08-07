#
# list and set comprehensions
#

words = "why sometimes I have believed I have several facts".split()
words

[len(word) for word in words]   # LIST
{len(word) for word in words}   # SET

# this does not seem to work
# x = (len(word) for word in words) # TUPLE -- NO instead this is a Generator comprehensions and has lazy evaluation -- iteration protocols for examples
# print(x)

# dictionary
from pprint import pprint as pp

country_to_capital = {'United kingdom': 'london',
                      'brazil': 'brasilia',
                      'Sweden': 'Stockholm'}
pp(country_to_capital)

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)

import os
import glob

# GLOB GETS ALL FILES OF .PY
# patha and st-size get the path and size of the file
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}

pp(file_sizes)


# filtering on the iterator
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

# numbers with only 2 divisors
primes = [x for x in range(101) if is_prime(x)]  #
primes

# numbers with only 3 divisors
three_divisors = {x*x:[1,x,x*x] for x in range(101) if is_prime(x) }
pp(three_divisors)

# zipping 2 or more lists together
cities = ['boston','ny','southbury','somers','norwalk','stamford']
[print(n) for n in cities]
[print(i, cities[i]) for i in range(len(cities))]

for i in enumerate(cities):
    print(i)

ids = [i for i in range(len(cities))]

for i in zip(ids,cities,ids):
    print(i)


# multiple assignments
a, b = 12, 14

 # swapping
 b,a = a,b
 print(a,b)





