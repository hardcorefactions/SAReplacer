import os

replaced = 0
store = "store.vexpvp.club"
domain = "vexpvp.club"

for file in os.listdir('Abilities'):
	file = 'Abilities/'+file
	with open(file, 'r') as f:
		content = []
		f = f.readlines()
		for line in f:
			if "skilled-dev.club" in line:
				content.append(line.replace('skilled-dev.club', domain))
				replaced+=1
				print(replaced)
			elif "store.youserver.com" in line:
				content.append(line.replace('store.youserver.com', store))
				replaced+=1
				print('Replaced '+str(replaced)+'times.')
			else:
				content.append(line)
		with open(file, 'w') as f:
			for line in content:
				f.write(line)
