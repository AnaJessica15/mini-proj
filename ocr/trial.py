# text recognition
import cv2
import pytesseract
# read image
im = cv2.imread('/home/ana/Pictures/img.jpeg')
# configurations
config = ('-l eng --oem 1 --psm 3')
# pytesseract
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('\n')
print(text)