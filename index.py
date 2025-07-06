import pyqrcode
from PIL import Image

link = input("Type a link to generate QR: ")
qrCode = pyqrcode.create(link)
qrCode.png("MyQRCode.png", scale=5)

img = Image.open("MyQRCode.png")
img.show()