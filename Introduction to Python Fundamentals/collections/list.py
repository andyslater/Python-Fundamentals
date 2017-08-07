
l = "show how to index into sequences".split()

print(l, len(l))

for i in range(len(l)):
    print( i, i-len(l), l[i] )


#can index going from the start using 0
print(l[0])

# can index from the end using -1 as the first locatoin
print(l[-1])

print(l[1:4]) # start and end, but not including the final index

print(l[1:-1]) # start index 1 (second itmem) and go to the last (but not include the last)

print(l[-2:0:-1]) # start at the last and go till just before the first

print(l[3:]) # start at 3 and go till end

print(l[:3]) # upto but not including the thrid element

# to copy the list
l2 = l[:]
lpointer = l
print( l is lpointer)
print(not l2 is l)
print(l2 == l)

# more readable ways to copy a list
l3 = l.copy()
print( l3, not l3 is l, l3 == l )
l4 = list(l)
print( l4, not l4 is l, l4 == l )

# be very careful of list repetion and shallow copies that will copy pointers to list embeded inside lists and not the actual values.

# indexing and counting with lists
w = "the quick brown fox jumped over the lazy dog".split()
print(w, w.index('fox'), w.count('the'), 'jumped' in w, 'xf' not in w, not 'xf' in w)

#index returns first index found
print(w.index('the'), w[1:].index('the'))



# removing stuff from lists
del w[2]
print(w)

w.remove('the')  # removes the first instance
print(w)

# inserting into list
w = "the brown fox jumped over the lazy dog".split()
w.insert(1,"quick")
print(w)

print(' '.join(w))

#reverse
w = "the quick brown fox jumped over the lazy dog".split()
w.reverse() # actually reverses the list, and returns None
print(w)

#sort
w = "the quick brown fox jumped over the lazy dog".split()
w.sort() # actually sorts the list, and returns None
print(w)

w = "the quick brown fox jumped over the lazy dog".split()
w.sort(key=len) # calls len function to use that as the function to sort by
print(w)

# comparing lists. compares from left to right. can compare a lot of differnet types, but they have to be the same time per comparison
print( [1,2,3] < [1,2,4])
print( [1,3,3] > [1,2,4])
print( ['b',2,3] > ['a',2,4])
print( [1, ['b',2,3], 3] > [1, ['a',2,4], 3])

