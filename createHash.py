#run using "python3 createHash.py"
import crypt

def crackCrypt(passw):
	#accepts passw and generates crypt
	return crypt.crypt(passw)

with open('dict/test.txt') as file:
	for line in file:
		#creating hashes and storing
		newHash = crackCrypt(line)
		hashStore = open("hashDict.txt","a")
		hashStore.write(newHash + "\r")

		#creating comparison file
		comparison = open("hashCompare.txt","a")
		comparison.write(line + newHash + "\n")
		
		if 'abacus' in line:
			break

print ("Job's Done....")
