import cv2
imagen= cv2.imread('imagenes/Pikachu.jpg')
Imagen_Modificada = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
Imagen_Modificada2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


cv2.imshow('Imagen Mostrada', imagen)
cv2.imshow('Imagen Modificada', Imagen_Modificada)
cv2.imshow('Imagen Blanco y Negro', Imagen_Modificada2)

cv2.imwrite('imagenes/PikachuBlack.jpg',Imagen_Modificada2)

cv2.waitKey(0) ##Al pulsar la tecla 0 se cierra la ventana
cv2.destroyAllWindows()