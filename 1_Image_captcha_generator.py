"""install captcha package"""
from captcha.image import ImageCaptcha
from PIL import Image


#specify the image size
image = ImageCaptcha(width = 300, height = 100)
#Specify the text for captcha
captcha_text = input("Enter captcha text: ")
#generate the image of text
data= image.generate(captcha_text)
#write the image and save it
image.write(captcha_text, 'CAPTCHA1.png')
from PIL import Image
image.open('CAPTCHA1.png')
