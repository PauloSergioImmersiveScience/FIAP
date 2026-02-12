# Código para Ler e exibir um  video simples no OpenCV 4.13
# Data: 12/02/26
# Autor: Prof. Dr. Paulo Sérgio Rodrigues (UFABC/FIAP)

import cv2

PATH = "paisagem01.mp4"

cap = cv2.VideoCapture(PATH)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



