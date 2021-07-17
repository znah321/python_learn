# 4-3
for num in range(1, 21):
    print(num)

# 4-4
print()
list1 = [num for num in range(1, 1000001)]
# for value in list1:
#     print(value)

# 4-5
print('\nmin value: ' + str(min(list1)))
print('max value: ' + str(max(list1)))
print('sum value: ' + str(sum(list1)))

# 4-6
print()
list2 = [num for num in range(1, 21, 2)]
for value in list2:
    print(value)

# 4-7
print()
list3 = [num for num in range(3, 31, 3)]
for value in list3:
    print(value)

# 4-8
print()
list4 = [num**3 for num in range(1, 11)]
for value in list4:
    print(value)