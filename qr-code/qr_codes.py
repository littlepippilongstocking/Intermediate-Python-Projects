"""
Dilyana Koleva, July 2022
Intermediate Python Project - QR Code Encoder/Decoder
"""
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def encoder():
    path = ""  # add your own path
    data1 = "Albert Einstein"
    img1 = qrcode.make(data1)
    img1.save(path + "myqrcode.png")

    data2 = "Paul Anka"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data2)
    qr.make(fit=True)
    img2 = qr.make_image(fill_color='red', back_color='white')
    img2.save(path + "myqrcode1.png")


def decoder():
    path = ""  # add your own path
    img = Image.open(path + "myqrcode1.png")
    results = decode(img)
    print(results)


if __name__ == '__main__':
    resp = input("Do you want to decode or encode QR Codes? ").lower()
    if resp == "decode":
        decoder()
    elif resp == "encode":
        encoder()
