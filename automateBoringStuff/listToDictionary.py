def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print("Total number of items: " + str(itemTotal))

def addToInventory(inventory, addedItems):
    for i in dragonLoot:
        print(i)


inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

choice = input('Press E to view inventory.')
if choice == 'e':
    displayInventory(inv)



