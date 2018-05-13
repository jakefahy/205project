from stegano import lsb
from keyword_search import keyword
from PIL import Image

img = keyword("cat")
secret = lsb.hide(img, "cat")
secret.save("hidden.png")

clear_message = lsb.reveal("./hidden.png")
print(clear_message)
