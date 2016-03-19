import crypt

def crackCrypt(passw):
	#accepts passw and generates crypt
	#salt is 'xoxo'
	return crypt.crypt(passw,'xoxo')

with open('dict/brit-a-z.txt') as file:
	for line in file:
		#creating hashes and storing
		newHash = crackCrypt(line)
		hashStore = open("hashDict.txt","a")
		hashStore.write(newHash + '\n')

		#creating comparison file
		comparison = open("hashCompare.txt","a")
		comparison.write(line + newHash + "\r")
		
		if 'zymurgy' in line:
			break

print "Job's Done...."
