from PIL import Image
from helper import enc
from helper import dec
from helper import out

def encode(source, target, text):
    src = Image.open(source)
    im = list(src.convert("RGBA").getdata())

    with open(text, encoding="utf-8") as f:
        lines = f.readlines()

    stream = enc.parseText(lines)
    enc.interpolate(im, stream)

    steganograph = Image.new("RGBA", (src.width, src.height))
    steganograph.putdata(im)
    steganograph.save(target+".png", format = "PNG")

    return

def decode(source, target):
    src = Image.open(source)
    im = list(src.convert("RGBA").getdata())

    text = ""
    byte = ''
    i = 0
    while byte != 0:
        byte = dec.parseGraf(im[i])
        text = text + chr(byte)
        i += 1

    print(f"Saving your message: \"{text[:100]}...\" to {target}")
    with open(target, "w+", encoding = "utf-8") as f:
        f.write(text)

    return

encode("dog.jpg", "dog2", "msg.txt")
decode("dog2.png", "out.txt")

    
