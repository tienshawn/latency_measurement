import zxing

reader = zxing.BarCodeReader()
print(reader.zxing_version, reader.zxing_version_info)

def barcode_reader(img):
    barcode = reader.decode(img)
    print(barcode.parsed)
    
img = "/home/tienshawn1/Downloads/barcode (1).png"
barcode_reader(img)

link = ''
for i in range (100):
    img = link+str(i)+".png"
    barcode_reader(img)
