# iterables, generators, and generator comprehensions



iterator = iter(['sprint', 'summer', 'winter', 'fall' ])

next(iterator)
next(iterator)
next(iterator)
next(iterator)


def first(iterablex):
    iterator = iter(iterablex)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

first(iterable) # notice that can se the same list (iterable) because when that list used to call first, first sets a new ierator on that list
first(iterable)
first(iterable)
first(iterable)

first(set()) # empty set


#
# can pass in the iterator instead of the iterable
#
def first_iterator(iteratorx):
    try:
        return next(iteratorx)
    except StopIteration:
        raise ValueError("iterator is empty")

iterable = ['spring', 'summer', 'winter', 'fall' ]
iterator2 = iter(iterable)
iterator2_1 = iterator2
iterator3 = iter(iterable)

i2 = first_iterator(iterator2)
i2
i2 = first_iterator(iterator2_1)
i2
i3 = first_iterator(iterator3)
i3

########################################
#
# GENERATORS
#

# not the code stops at the yield and then resumes at the next line the next time it is called
def gen123():
    print("about to yeild 1")
    yield 1

    print("about to yeild 2")
    yield 2

    print("about to yeild 3")
    yield 3


g = gen123()
print(g) # just a pointer to a function

next(g)
next(g)
next(g)
next(g)

# each instance is a new point to a new generator function
g = gen123()
h = gen123()
NOT g is h 


###################################################
#
# pipeline 
#   take -- grabs only the next 3 items in the list to process
#   distinct -- returns only the next unique value
# by pipelineing these together, we can process only the next 3 unique values an avoid reading in the entire list to first get the distinct values, and then run that through the the take function
#
def distinct(iterable):
    seen = set()    # apparently this only gets executed the first time this function is called
    for item in iterable:
        if item in seen:
            continue #back to the top of the loop
        yield item
        seen.add(item)


def take(count, iterable):
    # return only the first 3 values
    counter = 0   # note that this seems to only be executed on the first pass

    for item in iterable:
        if count == counter:
            return
        counter += 1
        yield item


def run_distinct(iterable):
    # return only unique values
    for item in distinct(iterable):
        print(item)

# ok pipeline them together to get the first 3 unique
def run_pipeline(iterable):
    for item in take( 3, distinct(iterable) ):
        print(item)


# just get the next 3 uniquie
run_distinct([5,7,7,5,7,5,8,3,8,4,22])

run_pipeline([5,7,7,5,7,5,8,3,8,4,22])



#
#
#  GENERATOR COMPREHENSIONS
#       lazy evaluatoin with generators
#

million_squares = (x*x for x in range(1, 1000001))
#list(million_squares) # list forces the execution of the entire generator, this wouldbe about 40 MB


for square in (x*x for x in range(1, 1000001)):
    if square > 1000:
        break
    print(square)

sum(x*x for x in range(1,1000001)) # sum the first 1M squares in about 1 second

#
# itertools https://docs.python.org/3/library/itertools.html
#
from itertools import islice, count, chain

thousand = islice((x for x in count()), 25)
thousand
list(thousand)     


#
from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

any(is_prime(x) for x in range(200, 400))
all(names == names.title() for names in ['Andy', 'Jillian','cam'])

# zip and chain data together
monday = [1,2,3,4]
tuesday = [5,6,7,8,9]
wednesday = [10,11,12,13]
zip(monday,tuesday) # generator that zips the lists together, drops the ones without a pair. also it does not add any more memory!!
x = zip(monday,tuesday)
list( x )
list(x)  # because its a generator the second returns empty list

for temps in zip(monday,tuesday,wednesday):
    print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format( min(temps), max(temps), sum(temps) / len(temps)))

# chain is a generator that concatenates data but incredibly does not copy the data!!! very cool
for temps in chain(monday,tuesday,wednesday):
    print(temps)

all(t>0 for t in chain(monday,tuesday,wednesday))





