import base64
 
s=''
with open('1.txt', 'r', encoding='UTF-8') as f:
    s=f.read()
src=s    
while True:
    try:
        s=base64.b16decode(s)
        continue
    except:
        pass
    try: 
        s=base64.b32decode(s)
        continue
    except:
        pass
    try:
        s=base64.b64decode(s)
        continue
    except:
        pass
    break
print(s)