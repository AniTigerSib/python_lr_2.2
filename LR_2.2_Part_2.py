import base64
import hashlib

#help(base64)
hex_values = input().split()
byte_values = [int(value, 16) for value in hex_values]
b64string = base64.b64encode(bytearray(byte_values)).decode('ascii')
print(b64string)
encoded_string = input()
byte_values = base64.b64decode(encoded_string)
# byte_values = byte_values.decode('ascii')
print(byte_values)

#help(hashlib)
hashstr = hashlib.sha256()
string = input()
hashstr.update(string.encode('ascii'))
print(hashstr.hexdigest())