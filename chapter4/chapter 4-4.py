# 4-10
list1 = list(range(9))
print('The first three items in the list are: ' + str(list1[:3]))
print('Three items from the middle of the list are: ' + str(list1[3:6]))
print('The last three items in the list are: ' + str(list1[6:]))

# 4-11
print()
pizzas = ['beef', 'sausage', 'bacon']
friend_pizza = pizzas[:]
pizzas.append('fruit')
friend_pizza.append('vegetable')
print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print('\nMy friend\'s favorite pizzas are: ')
for pizza in friend_pizza:
    print(pizza)
