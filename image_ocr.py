# source from https://pypi.org/project/tesserocr/
import tesserocr

from PIL import Image
api = tesserocr.PyTessBaseAPI()
pil_image = Image.open('sample.jpg')
api.SetImage(pil_image)
text = api.GetUTF8Text()
print(text)