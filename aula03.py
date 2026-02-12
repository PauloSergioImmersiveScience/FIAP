
# importa a biblioteca principal do OpenCV
import cv2
# define o caminho e a imagem onde o OpenCv vai encontr´a-la
PATH = "lena.jpg"
# Lˆe a imagem
img = cv2.imread(PATH)
# define uma janela de visualiza¸c˜ao
cv2.namedWindow("Imagem", cv2.WINDOW_NORMAL)
# exibe a imagem na janela definida
cv2.imshow("Imagem", img)
# aguarda at´e uma tecla ser acionada
cv2.waitKey(0)
# encerra todas as janelas definidas at´e aqui
cv2.destroyAllWindows()

