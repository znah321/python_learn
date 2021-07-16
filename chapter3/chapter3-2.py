# 3-4
namelist = ['Tom', 'John', 'Alan']
for i in range(len(namelist)):
    print('I want to invite ' + namelist[i] + ' to have dinner together.')

# 3-5
print('\n' + namelist[-1] + ' can\'t come for some reasons.')
namelist[-1] = 'Nick'
print('Changed "Alan" to "Nick".')
for i in range(len(namelist)):
    print('I want to invite ' + namelist[i] + ' to have dinner together.')

# 3-6
print('\nAnd I find a bigger desk to have dinner.')
namelist.insert(0, 'Li Hua')
namelist.insert(2, "Zhang San")
namelist.append('Li Si')
for i in range(len(namelist)):
    print('I want to invite ' + namelist[i] + ' to have dinner together.')

# 3-7
print('\nDue to some reasons, I can only invite 2 guests.')
while len(namelist) > 2:
    namelist.pop()
for i in range(len(namelist)):
    print('I want to invite ' + namelist[i] + ' to have dinner together.')
del namelist[1]
del namelist[0]
print(namelist)
