import hashlib
dk=hashlib.pbkdf2_hmac('sha256',b'indu',b'salt',100000)
print(dk.hex())
