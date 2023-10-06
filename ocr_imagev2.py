import tesserocr


def main():
    from PIL import Image
    api = tesserocr.PyTessBaseAPI()
    pil_image = Image.open('ktp2.jpg')
    api.SetImage(pil_image)
    text = api.GetUTF8Text()
    print(text)
    
if __name__ == "__main__":
    main()
    
