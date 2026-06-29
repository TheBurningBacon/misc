# Encryption test 4
O(n) cypher shift multiplication
Converts characters into a x length number with the key being another x length number
Places all characters into a string and then shifts it over so that the first digit of the second number is the last of the first number
Multiplies each number by the key

## Example

    key,encmess=misc.encrypt(message,None,3)

    demessage.misc.decrypt(encmess,key)
