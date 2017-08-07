#
# this is from pluralsight, python fundamentals,collections chapter
#

# tuples
# immutable sequences -- objects cannot be replaced or removed
t = ("n", 5, 5.5)
print(t)
print(t[0])

t = t + t +(6,"ted")
print(t)

t = (1,2,3) *2
print(t)

t = (('a','b'), ('c','d'), ('e','f'))
print(t)
print(t[0][1])

t = t(5,) # sigle item tuple
t = () # empty tuple

def minmax(t):
    return min(t), max(t)

minmax((5,3,2,6))
minmax([5,3,2,6])

#
# tuple unpacking
#
lower, upper = minmax((4,5,1,9.15,15))  
print(lower, upper)

# prety powerful right here!
# rest get  alist of the rest
lower, lower2, *rest, upr = (1,2,3,4,5,6)
print(lower,rest,upr)

lower, lower2, l3, *rest = (1,2,3,4,5,6)
print(lower,lower2, l3, rest)



(a,(b,(c,d))) = (4,(5,(6,7)))
print(a,b,c,d)

a,b = b,a
print(a,b,c,d)


# TUPLE convrsions
t = tuple([1,2,3,4])
print(t)

t = tuple("blaster")
print(t)
for v in t:
    print(v)


# testing
print( 'i' not in tuple('blaster'))
print( 'a' in tuple('blaster'))

for v in (1,2,3,4):
    print(v)

