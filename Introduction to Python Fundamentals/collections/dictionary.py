#
# unordered mapping from unique immutable keys to mutable values

# keys can be stings, numbers, and tuples. Cannot be lists

###
### collection is like dictionary excpet a little more powerful, can return the result of a function if an unknown key is read
###

# create a default type and value for a dictinary value where the key is not found
dct = {}
print(dct[1234])

from collections import defaultdict
dct = defaultdict(int)
print(dct[1234])


a = {'fname': 'andy', 'lname': "Slater"}
print(a)
print(a['fname'])   # to index into the dictionary, you use [] around the key

print(a['badkey'])  # this will trow an error
print( a.get('badkey','default value'))  # better way to get a value that may not be there in one line



#make a list
a = dict( (('a',1), ('b',2), ((1,2,3),'tuple is key') ) )
print(a, a['a'], a['b'], a[(1,2,3)])

for k in ('a','b',(1,2,3)):
    print(a[k])

keys = list(('b','a','b'))
keys.sort()
print(keys)
for k in keys:
    print(a[k])

#
#

names = ['a', 'b', 'c']
sizes = [1, 2, 3]
adict = dict( zip(names,sizes) )


bdict = { n*2 : s for n,s in zip(names,sizes) }
print(bdict)


#
#
a = dict(a=1, b=2, c='charlie')
print(a)

# copy dictionay
a = dict(a=1, b=2, c='charlie')
b = a.copy()
print(b)
c = dict(a)
print(c)
print(not a is b, a == b)

f = dict(a=2,b=4,d='ggg')
f.update(a) # will add items an a dict to f missing and will update exisiting
print(f)
print(f['a'])

print(NOT 'ggg' in f)  # the values are not included in the f list
print(['a','b'] in f)  # the keys are included in the f list




#iterating through dictionary
for key in f:
    print(key, f[key])


# for key in list(f.keys()).sort():  # not sure why this does not work
#    print(key, f[key])

a = list(f.keys()).sort()
print(a) # why is a None and not a sorted lisst

# there must be a better way to do this
a = list(f.keys())
a.sort()
a = tuple(a)
print(a)
for key in a:
    print(key)
#    print(key, f[a]) # this does not work either


for keyvalue_tuple in f.items():
    print(keyvalue_tuple)

for key,value in f.items():
    print(key,value)


# keys inclusion test
f = {"fname": "andy", "lname": "slater"}
print( 'fname' in f, not 'andy' in f)
 
f = dict(fname='andy', lname='slater')
print( 'fname' in f, not 'andy' in f)
 
f = dict( a=[1,2], b=(3,4))
from pprint import pprint as pp
pp(f)
print(f)


