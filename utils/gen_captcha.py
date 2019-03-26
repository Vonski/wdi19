from captcha.image import ImageCaptcha
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random, string


def generate_random_labeled_sample():
    text = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))

    gen = ImageCaptcha()
    imageIO, spec, chars = gen.generate(text)

    imageIO.seek(0)
    image = Image.open(imageIO)

    return image, spec, chars


# gen = ImageCaptcha()
#
# imageIO, spec, chars = gen.generate("abcd")
#
# print(type(imageIO))
#
# imageIO.seek(0)
# image = Image.open(imageIO)
#
# draw = ImageDraw.Draw(image)
# for i in range(len(chars)):
#     if chars[i] is not " ":
#         draw.rectangle([spec[i][0],spec[i][1],spec[i][0]+spec[i][2],spec[i][1]+spec[i][3]],fill=None, outline="red")
#
# print(chars)
#
# image = image.resize((1280,480))
# image.show()
#
# image.save('lol.png', 'png')
#
# gen.write('1234','cap.png')