#Fantasy Game Inventory

'''You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are 
string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. 
For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 
torches, 42 gold coins, and so on. Write a function named displayInventory() that would take any possible “inventory” and display it 
like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    num_item = 0
    for k, v in inventory.items():
        print(str(v), ' ', k)
        num_item += v
    print('Total number of items:', num_item)

displayInventory(stuff)

#List to Dictionary Function for Fantasy Game Inventory

'''Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the 
player’s inventory (like in the above project) and the addedItems parameter is a list like; 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can 
contain multiples of the same item.'''

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
        #if item not in inventory.keys():
        #   inventory[item] = 1
        #else:
        #    inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
print(displayInventory(inv))
