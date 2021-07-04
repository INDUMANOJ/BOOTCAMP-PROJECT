import hashlib
def md5string(name):
    
    y=hashlib.md5(name.encode('UTF-8')).hexdigest()
    return y
x=input("entr name")
print(md5string(x),x)
