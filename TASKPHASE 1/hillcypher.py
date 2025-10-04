import sys
from math import gcd

def clean(s):
    s=''.join(ch for ch in s.upper() if 'A'<=ch<='Z')
    if len(s)%2: s+='X'
    return s

def egcd(a,b):
    x0,y0,x1,y1=1,0,0,1
    while b:
        q,a,b = a//b, b, a - (a//b)*b
        x0,x1 = x1, x0 - q*x1
        y0,y1 = y1, y0 - q*y1
    return a,x0,y0

def modinv(a,m):
    g,x,_=egcd(a%m,m)
    return x%m if g==1 else None

def det2(k):
    return (k[0]*k[3]-k[1]*k[2])%26

def inv2(k):
    d=det2(k)
    invd=modinv(d,26)
    if invd is None: return None
    a,b,c,d2 = k
    return [( d2*invd)%26, ((-b)*invd)%26, ((-c)*invd)%26, (a*invd)%26]

def pair_apply(p,k):
    x=ord(p[0])-65; y=ord(p[1])-65
    return chr((k[0]*x+k[1]*y)%26+65)+chr((k[2]*x+k[3]*y)%26+65)

def encrypt(plain,key):
    p=clean(plain); out=[]
    for i in range(0,len(p),2): out.append(pair_apply(p[i:i+2],key))
    return ''.join(out)

def decrypt(cipher,key):
    inv=inv2(key)
    if inv is None: return None
    c=clean(cipher); out=[]
    for i in range(0,len(c),2): out.append(pair_apply(c[i:i+2],inv))
    return ''.join(out)

def parse_key(s):
    parts=[int(x)%26 for x in s.split()]
    return parts if len(parts)==4 else None

def brute_force(cipher,crib):
    if not crib: return []
    c=clean(cipher); crib=crib.upper()
    res=[]
    for a in range(26):
        for b in range(26):
            for c2 in range(26):
                for d in range(26):
                    k=[a,b,c2,d]
                    if gcd(det2(k),26)!=1: continue
                    pt=decrypt(cipher,k)
                    if pt and crib in pt: res.append((pt,k))
    return res

def ask(prompt=''):
    sys.stdout.write(prompt); return input()

def menu():
    while True:
        print("1 encrypt  2 decrypt  3 brute  q quit")
        ch=ask("> ").strip()
        if ch=='1':
            pt=ask("plaintext: ")
            k=parse_key(ask("key (4 nums row-major): "))
            print("ciphertext:",encrypt(pt,k) if k else "bad key")
        elif ch=='2':
            ct=ask("ciphertext: ")
            k=parse_key(ask("key (4 nums row-major): "))
            p=decrypt(ct,k) if k else None
            print("plaintext:" , p if p else "bad/invertible key")
        elif ch=='3':
            ct=ask("ciphertext: "); crib=ask("crib (required): ").strip()
            found=brute_force(ct,crib)
            if not found: print("none")
            else:
                for pt,k in found: print(pt,"key=",k)
        elif ch.lower()=='q': break
        else: print("invalid")

if __name__=="__main__":
    try: menu()
    except KeyboardInterrupt: pass
