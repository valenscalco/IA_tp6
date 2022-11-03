import matplotlib.pyplot as plt
import random
import leerimage_bin
import tiempo_progreso
import numpy as np


class Perceptron:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.valor_w0 = 1

    def compuerta_XOR(self):
        self.salida_d = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

    def grafico_error(self, error0, error1, error2, error3, error4, error5, error6, error7, error8, error9, count):
        plt.figure(figsize=(10, 7))
        count += 1
        plt.plot(range(count), error0, label="error 0")
        plt.plot(range(count), error1, label="error 1")
        plt.plot(range(count), error2, label="error 2")
        plt.plot(range(count), error3, label="error 3")
        plt.plot(range(count), error4, label="error 4")
        plt.plot(range(count), error5, label="error 5")
        plt.plot(range(count), error6, label="error 6")
        plt.plot(range(count), error7, label="error 7")
        plt.plot(range(count), error8, label="error 8")
        plt.plot(range(count), error9, label="error 9")
        plt.title("Errores")
        plt.legend()
        plt.savefig("Errores.png")
        plt.show()
        plt.close()

    def suma_oculta(self, z):
        y = []
        x = 0
        pesos_oculto = len(self.w) - (self.resp + 1)
        for g in range(0, pesos_oculto, 61443):
            x += (self.w[g] * 1)
            for i in range(61442):
                x += (self.w[g+1] * self.valores_e[i])
            valor_y = (np.float64(np.divide(1, (1 + np.exp(-x)))))
            y.append(round(valor_y, 10))
        y = self.suma_salida(y, pesos_oculto)
        return (y)

    def suma_salida(self, y_oculta, pesos_oculto):
        valor_suma = (self.w[pesos_oculto] * 1)
        for p in range(self.resp):
            pesos_oculto += 1
            valor_suma = valor_suma + (self.w[pesos_oculto] * y_oculta[p])
        valor_ys = np.float64(np.divide(1, (1 + np.exp(-valor_suma))))
        y_oculta.append(valor_ys)
        return (y_oculta)

    def resolucion(self):
        # delta_w = woc
        woc = []
        soc = []
        error0 = []
        error1 = []
        error2 = []
        error3 = []
        error4 = []
        error5 = []
        error6 = []
        error7 = []
        error8 = []
        error9 = []
        lr = 0.5
        t = 0
        self.w = []
        # Creo los pesos
        for i in range(self.resp+1):
            if i == self.resp:
                for j in range((self.resp + 1)):
                    self.w.append(random.uniform(-1, 1))
            else:
                for j in range(61443):
                    self.w.append(random.uniform(-1, 1))
        i = 0
        r = 0
        for t in range(0, self.it):
            for i in range(0, 10):
                self.valores_e = leerimage_bin.leer_images(i)
                valores_y = self.suma_oculta(i)
                error = self.salida_d[i] - valores_y[self.resp]
                sf = valores_y[self.resp] * (1 - valores_y[self.resp]) * error
                # Neuronas
                woc = []
                for k in range(0, self.resp):
                    soc = (valores_y[k] * (1 - valores_y[k]) * sf)
                    woc.append(lr * 1 * soc)
                    for r in range(0, 61442):
                        woc.append(lr * self.valores_e[r] * soc)
                # Ultima neurona
                woc.append(lr * 1 * sf)
                for y in range(0, self.resp):
                    woc.append(lr * valores_y[y] * sf)
                # Cambiar pesos
                for pesos in range(0, len(self.w)):
                    self.w[pesos] = self.w[pesos] + woc[pesos]
                if i == 0:
                    error0.append(error)
                if i == 1:
                    error1.append(error)
                if i == 2:
                    error2.append(error)
                if i == 3:
                    error3.append(error)
                if i == 4:
                    error4.append(error)
                if i == 5:
                    error5.append(error)
                if i == 6:
                    error6.append(error)
                if i == 7:
                    error7.append(error)
                if i == 8:
                    error8.append(error)
                if i == 9:
                    error9.append(error)
                if t == self.it - 1:
                    print('Salida real para salida deseada', self.salida_d[i], ':', valores_y[self.resp])
            self.valores_e = tiempo_progreso.tiempo_barra(t, self.it)
        print('Entrenamiento realizado:', t+1, 'veces')
        self.grafico_error(error0, error1, error2, error3, error4, error5, error6, error7, error8, error9, t)
        pesosexport = open('pesosfinales.txt', 'w')
        pesosexport.write(str(self.w))
        pesosexport.close()

    def numero_neuronas(self):
        self.resp = 0
        self.it = 0
        self.resp = int(input('Ingrese numero de perceptrones en capa oculta: \n'))
        self.it = int(input('Ingrese numero de iteraciones a realizar: \n'))
        self.compuerta_XOR()
        self.resolucion()


def main():
    g = Perceptron()
    g.numero_neuronas()


if __name__ == "__main__":
    main()