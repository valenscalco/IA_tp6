# Importar librería cv2
from PIL import Image
import copy


def leer_images(x):
    nom = ['1A58103.jpg', '1B58103.jpg', '2A58103.jpg', '2B58103.jpg', '3A58103.jpg', '3B58103.jpg', '4A58103.jpg', '4B58103.jpg', '5A58103.jpg', '5B58103.jpg']
    # Leer imagen
    img = Image.open(nom[x])
    width, height = img.size
    lista = []
    valores = []
    persona = True
    aux = []
    pixel_access_object = img.load()
    for i in range(width):
        for j in range(height):
            lista.append(pixel_access_object[i, j])
    # print(lista)
    aux.clear()
    aux.append(1) # Agrego Vias a la entrada
    for r in range(len(lista)):
        px = lista[r][0]
        exceso = 0
        for t in range(8):
            if t < 8-len(bin(px)[2:]):
                aux.append(0)
                exceso = exceso + 1
            else:
                aux.append(int(bin(px)[2+t-exceso]))
    if persona:
        aux.append(int(0))
        persona = False
    else:
        aux.append(1)
        persona = True
    # for i in range(len(lista)):
        # valores.append(lista[i][0]/255)
        # valores.append(lista[i][0])
        # temp = format(valores[i], "b")
    # print(valores)
    return aux


#if __name__ == "__main__":
#    leer_images()
