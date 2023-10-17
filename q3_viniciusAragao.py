from PIL import Image, ImageEnhance

aumentar_brilho = lambda: ImageEnhance.Brightness(Image.open("assets/foto.jpg")).enhance(float(input("Insira um valor (maior que 0): "))).show()

aumentar_brilho()