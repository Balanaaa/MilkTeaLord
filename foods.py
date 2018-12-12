foods = ['apple','orange','pineapple','peach','banana']
for food in foods:
	print ('We have '+food)

foods[2] = 'coconut'
print ('I want '+foods[2])
print ('Sorry, You are not able to change the food!')
foods[2] = 'pineapple'
foods[1] = 'orange'
foods[0] = 'coconut'
for food in foods:
	print ('We now have '+food)