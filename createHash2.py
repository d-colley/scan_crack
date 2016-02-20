import crypt

from hmac import compare_digest as compare_hash

plaintext='gaza'
encrypted= crypt.crypt(plaintext)

if compare_hash(encrypted, crypt.crypt(plaintext, encrypted)):
   print (crypt.crypt(plaintext, encrypted))
   print (encrypted)

