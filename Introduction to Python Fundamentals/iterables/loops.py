

for i in range(5):
    print(i)
else:
    print('no break')



i = 0
while i < 10:
    print(i)
    i += 1
    if i == 5:
        continue
    if i == 7:
       break
else:
    print('no break')

