# Importar librería cv2
from PIL import Image


def leer_images(x):
    nom = ['1A58103.jpg', '1B58103.jpg', '2A58103.jpg', '2B58103.jpg', '3A58103.jpg', '3B58103.jpg', '4A58103.jpg', '4B58103.jpg', '5A58103.jpg', '5B58103.jpg']
    # Leer imagen
    img = Image.open(nom[x])
    width, height = img.size
    lista = []
    valores = []
    pixel_access_object = img.load()
    for i in range(width):
        for j in range(height):
            lista.append(pixel_access_object[i, j])
    for i in range(len(lista)):
        # valores.append(lista[i][0]/255)
        valores.append(lista[i][0])
        # temp = format(valores[i], "b")
    return valores
