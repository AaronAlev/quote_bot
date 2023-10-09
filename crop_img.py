from PIL import Image

def crop():
    img = Image.open('quote.png')
    box = (100, 0, 700, 600)
    img2 = img.crop(box)
    img2.save('quote.png')