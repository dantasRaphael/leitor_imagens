from PIL import Image
import pytesseract

caminho = 'C:/Users/NR Contabilidade/AppData/Local/Tesseract-OCR'

#img = Image.open("C:/Users/NR Contabilidade/Desktop/newPic.jpg")

img = Image.open("C:/Users/NR Contabilidade/Documents/imagens/a1.jpeg")
#

pytesseract.pytesseract.tesseract_cmd = caminho + "/tesseract.exe"

texto = pytesseract.image_to_string(img)
print('a mensagem é: ')
print(texto)