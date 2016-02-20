import crypt
from hmac import compare_digest as compare_hash
dictFile=[]
hshFile=[]
# with open('dict/brit-a-z.txt', encoding = "ISO-8859-1") as f:
# 	dictFile = [line.rstrip('\n') for line in open('dict/brit-a-z.txt', encoding = "ISO-8859-1")]

dictFile = [line.rstrip('\n') for line in open('dict/test.txt')]
hshFile = [line.rstrip('\n') for line in open('hashDict.txt')]

i=0
count = len(dictFile)

while (i < count):
	plaintext= dictFile[i]
	encrypted= hshFile[i]

	print (crypt.crypt(plaintext, encrypted))
	print (':')
	print (encrypted)
	if compare_hash(encrypted, crypt.crypt(plaintext, encrypted)):
		
		print('works')
	else:
		print('does not work')

	i=i+1
