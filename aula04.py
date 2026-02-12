# Código para Ler, Alterar e exibir cada pixel de uma imagem simples no OpenCV 4.13
# Data: 12/02/26
# Autor: Prof. Dr. Paulo Sérgio Rodrigues (UFABC/FIAP)

# importa a biblioteca principal do OpenCV
import cv2

# importa a biblioteca principal do OpenCV
import numpy as np

# Caminho da imagem
PATH = "lena.jpg"

# Lê a imagem (RGB)
img = cv2.imread(PATH)

# Converte para GrayScale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define limiar
L = 128 # vocˆe pode alterar esse valor

# Obt´em dimens˜oes da imagem original
altura, largura = img_gray.shape

# Cria imagem bin´aria vazia
img_bin = np.zeros((altura, largura), dtype=np.uint8)

# Varre pixel a pixel e altera o valor para 0 (preto) ou 255 (branco)
for i in range(altura):
    for j in range(largura):
        if img_gray[i, j] >= L:
            img_bin[i, j] = 255
        else:
            img_bin[i, j] = 0

# Cria Janelas para exibir os resultados
cv2.namedWindow("Original Gray", cv2.WINDOW_NORMAL)
cv2.namedWindow("Binaria", cv2.WINDOW_NORMAL)

# Exibe os resultados nas janelas criadas
cv2.imshow("Original Gray", img_gray)
cv2.imshow("Binaria", img_bin)

# aguarda at´e uma tecla ser acionada
cv2.waitKey(0)

# apaga as janelas criadas e encerra o programa
cv2.destroyAllWindows()


