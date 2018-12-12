noodles = ['Chinese noodles','spaghetti','special noodles']
friend_noodles = ['Chinese noodles','spaghetti','special noodles']

for noodle in noodles:
	print ('I like '+noodle)
print ('I really love '+noodles[1])
print ('I really love '+noodles[0])
print ('I really love '+noodles[2])
print ('\n')



noodles.append('delicious noodle')
friend_noodles.append('sichuan noodle')



for noodle in noodles:
	print ('I like '+noodle)
for noodle1 in friend_noodles:
	print ('My friend like '+noodle1)