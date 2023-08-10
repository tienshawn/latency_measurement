from dbr import BarcodeReader, EnumErrorCode
reader = BarcodeReader()

def Bar_decode(filename):
    results = reader.decode_file(filename)
    if results is None:
        print("No codes found")
    else:
        for r in results:
            print(r.barcode_text)

for i in range (100):
    name = "/home/tienshawn1/Desktop/embed_barcode/Barcode/Code/new_code"+str(i)+".png"
    Bar_decode(name)

#bug: cannot read number ending with 7
