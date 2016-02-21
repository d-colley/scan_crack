import crypt
dictFile=[]
hshFile=[]

dictFile = [line.rstrip('\n') for line in open('dict/brit-a-z.txt')]
hshFile = [line.split( ) for line in open('hashDict.txt')]

i=0
count = len(dictFile)

while (i < count):
	plaintext = dictFile[i]
	encrypted = hshFile[0][i]


	test1 = (crypt.crypt(plaintext, 'xoxo'))
	test2 = encrypted

	print (plaintext + "'s test encryption: " + test1)
	print ('Dict hash for plaintext: ' + encrypted + "\n")

	if (test1 == test2):
		print (" MATCH ALERT!!!!!! " + test1 + ' = ' + plaintext + "\n")
	i=i+1
