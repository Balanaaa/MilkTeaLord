rivers=['Yellow River','Yangzte River','The Nile River']
print(rivers[0])
print(rivers[-1])
message="The second longest river in China is " + rivers[0] + "."
print(message)
rivers1=['Yellow River','Yangzte River','TheNile River']
rivers1[1]='The Mekong River'
print(rivers1)
rivers1,insert(0,'The Mississippi River')
print(rivers1)
rivers1.insert(o,'The mississippi River')
print(rivers1)
del rivers1[0]
print(rivers1)
popped_revers1= rivers1.pop()
print(popped_revers1)
favorite_river=rivers1.pop(0)
print('My favorite river is '+ favorite_river + '.')
rivers1.remove('The Nile River')
print(rivers1)
rivers2=['Yellow River','Yangzte River','The Nile River']
rivers2.sort()
print(rivers2)
rivers2.sort(reverse=True)
print(rivers2)
rivers2.reverse()
print(rivers2)