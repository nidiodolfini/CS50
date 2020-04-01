import sys

arg = sys.argv
try:
    key = int(arg[1])
except:
    key = 1

plaintext = input('plaintext: ')
ciphertext = ''
for i in plaintext:
    if i.isalpha():
        if i.isupper():
            c = (ord('A') + (ord(i) - ord('A') + int(key)) % 26)
            ciphertext += ''.join(chr(c))
        elif i.islower():
            c = (ord('a') + (ord(i) - ord('a') + int(key)) % 26)
            ciphertext += ''.join(chr(c))
    else:
        ciphertext += ''.join(i)
print(f'ciphertext: {ciphertext}')
