from PIL import Image, ImageFilter

imgFile = "1.png"

img = Image.open(imgFile)
imgFt = img.filter(ImageFilter.CONTOUR)

img.show()
imgFt.show()

ftFile = "2.png"
imgFt.save(ftFile)
