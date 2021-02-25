def dumpBytes(im):
    for r,g,b,a in im:
        print(bin(r), bin(g), bin(b), bin(a))