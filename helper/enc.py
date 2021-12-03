def cmb(insert, target): #combine
    return (target & 0b11111100) + insert

def interpolate(im, stream):
    for i, bits in enumerate(stream):
        R1, G1, B1, A1 = bits
        R2, G2, B2, A2 = im[i]
        im[i] = tuple([cmb(R1, R2), cmb(G1, G2), cmb(B1, B2), cmb(A1, A2)])

def parseText(lines):
    stream = []
    for line in lines:
        for c in line:
            byte = ord(c)
            R = (byte & 0b11000000) >> 6
            G = (byte & 0b00110000) >> 4
            B = (byte & 0b00001100) >> 2
            A = (byte & 0b00000011) 
            #print(bin(byte), bin(R), bin(G), bin(B), bin(A))
            stream.append(tuple([R,G,B,A]))
    stream.append(tuple([0,0,0,0])) #NULL character
    return stream
