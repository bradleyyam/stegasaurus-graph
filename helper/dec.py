def rcmb(source): #reverse combine
    return (source & 0b00000011)

def parseGraf(pixel):
    R, G, B, A = pixel
    byte = (rcmb(R) << 6) + (rcmb(G) << 4) + (rcmb(B) << 2) + rcmb(A)
    return byte