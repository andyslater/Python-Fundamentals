# unordered collection of unique, immutable objects -- removes duplicates
# like a dictionary, but only keys

s = set() # gives an empty set

s = {1,4,5,'a', (1,2,3),'a'}
s.add(22)
print(s)

s.update([33,22,11])
print(s)

s.update({33,22,11,'rr'})
print(s)

s.remove('rrr') # gen KeyError if not in set
s.discard('rrr') # no error

# copy sets
s2 = s.copy()
s3 = set(s)
s4 = s 
print( s2,s3,s4)

print(not s is s2, s == s2, s is s4)

# set operators
blue_eyes = {'o','h','l','j','a'}
blond_hair = {'h','j','a','m','jo'}
taste = {'h','l','a','lo'}
o_blood = {'m','jo','l','o'}
b_blood = {'a','j'}
a_blood = {'h'}
ab_blood = {'jo','lo'}

print( blue_eyes.union(blond_hair) )
print( blue_eyes.intersection(blond_hair) )

# bond har but not blue eyes
print( blond_hair.difference(blue_eyes))

# one or the other but not both
print(blond_hair.symmetric_difference(blue_eyes))

# nothingin common (.isdisjoint)
