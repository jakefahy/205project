from stegano import lsb
from PIL import Image
#Blay Suttonwills worked on this file

#Encoding the message into the image
def encoding(fname, string):
    img = fname
    secret = lsb.hide(img, string)
    img = Image.open(img)
    img.show()
    secret.save("hidden.png")

#Decoding the image and getting the message back
def decoding():
    clear_message = lsb.reveal("./hidden.png")
    print(clear_message)
