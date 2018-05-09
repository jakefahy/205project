import lsb_math
from PIL import Image
from stegano import lsb
from stegano import exifHeader

# im = Image.open('Pres_Obama.jpg')

# secret = exifHeader.hide("./tests/sample-files/Pres_Obama.jpg",
#                         "./Pres_Obama.jpg", secret_message="Hello world!")
# print(exifHeader.reveal("./Pres_Obama.jpg"))



secret = lsb.hide("./Pres_Obama.jpg", "Hello World")
secret.save("./Pres_Obama-secret.jpg")

# clear_message = lsb.reveal("./Pres_Obama-secret.jpg")
