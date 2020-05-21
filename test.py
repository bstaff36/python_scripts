import crypto

import sys
import zlib
import binascii

# Here is the first line of plaintext that we can use as a sort of "key" given that a ^ b = c
data = "The following encoded individuals are to be given a $27.3k bonus"
d = data.encode('utf-8')
# first I will use the encrypted text as the OTP and XOR against the plaintext. this will reveal the OTP used to encrypt the doc
otp = binascii.unhexlify("163dfc4585055aa4664477a9b2fbb3e8658a47fa53216019d0e5c5d77619b38e1baf31f7ba4fc0c842e819c856353aa1da4a06dd4bc2ad04addb52565d4dc38e")

# These are actual OTPs I worked out, for example
#otp = b'\\;\xdd\x01\x1c\xb2\xe37\xcd\xf02\xb9\xd9\xc1j\r\xfdO\xf3\xed:I\x10\xcb.3% l\x8a\xfb\xe4|\xe6\x10$\xe1\x07C&p\x026\xec\xa7]\xc8|\xf3\x08\xd6\xe3\xd7R\x9e\xe4\xc6p\x9d9\xa5\xbc\x17\xb8'
#otp = b'BU\x99e\xe3j6\xc8\t3\x1e\xc7\xd5\xdb\xd6\x86\x06\xe5#\x9f7\x01\tw\xb4\x8c\xb3\xbe\x12l\xd2\xe2h\x8fP\x85\xdfo\xb4\xa7b\x8a|\xe81\\L\xc4\xb4jg\xfdo\xf0\x9a*\x9e\xb0r42#\xb6\xfd'

# Now we can do the XOR at each index
out = []
for i in range(0, len(d)):
        out.append(d[i] ^ otp[i])

# Finally we print the BYTES of the OTP
final = b''
final += (bytes(out))
print(final)

'''
To reverse the encryption you will need to swap in your discovered OTP and use the desired ciphertext as your d. the ciphertext must be unhexlified first before the XOR operation.

After the XOR, you will have bytes that you have to convert with a decode('utf-8')
'''