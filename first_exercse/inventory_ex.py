inventory = {
    'gold'      : 500,
    'pouch'     : ['flint', 'twine', 'gemstone'],
    'backpack'  : ['xylophone','dagger','bedroll', 'bread loaf']
}

#adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple','small ruby', 'tree-toed sloth']


#sorting the list found under the key 'pouch'
inventory['pouch'].sort()

#1. inventory 'pocket' key create
inventory['pocket'] = 'new key'

#2. new pocket list ['seashell','strange berry','lint']
inventory['pocket'] = ['seashell','strange berry','lint']

#3. backpack key value is sorted for sort() function
inventory['backpack'].sort()

#4. eliminate dagger to backpack key. used .remove('dagger')
inventory['backpack'].remove('dagger')

#5. gold value = add 50 and save
inventory['gold'] += 50

print (inventory)