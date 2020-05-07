stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print("Total number of items: " + str(itemTotal))

choice = input('Press E to view inventory.')
if choice == 'e':
    displayInventory(stuff)



