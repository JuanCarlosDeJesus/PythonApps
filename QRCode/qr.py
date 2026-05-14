import qrcode   # you have to install pillow also
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World! This is Fenris!", image_factory=factory)
svg_img.save("myqrcodesvg.svg")

# Create a QR code with the specified data
# img = qrcode.make("Hello World! This is Fenris!")
# img.save("myqrcode.png")

# Create a QR code with custom settings
# qr = qrcode.QRCode(version=1,
#                    error_correction=qrcode.constants.ERROR_CORRECT_L,
#                    box_size=20,
#                    border=2)

# qr.add_data("https://www.neuralnine.com/books")
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save("advancedQR.png")