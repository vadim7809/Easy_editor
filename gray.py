from PIL import Image, ImageEnhance, ImageFilter

with Image.open("img.jpg")as pic_original:
    pic_gray = pic_original.convert("L")
    pic_gray = pic_original.transpose(Image.ROTATE_90)
    pic_gray = ImageEnhance.Contrast(pic_gray).enhance(2)
    pic_gray = ImageEnhance.Color(pic_gray).enhance(3)
    pic_gray = pic_gray.filter(ImageFilter.SHARPEN)
    pic_gray.save("gray.jpg")
    pic_gray.show()