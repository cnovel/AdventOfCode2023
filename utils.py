def pgcd(a, b):
    g = max(a,b)
    p = min(a,b)
    while True:
        r = g % p
        if  r == 0:
            return p
        g = p
        p = r



def ppcm(a,b):
    return (a * b) / pgcd(a,b)
