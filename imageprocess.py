from PIL import Image, ImageFilter

img = Image.open("./images/test.jpg")
# print(img)
new_img = img.filter(ImageFilter.BLUR)
new_img.save("./images/blur.jpg")
