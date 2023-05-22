# PythonIA

## Taller de inteligencia artificial en python

### Notas

- Pycharm es un editor de texto de Python

- Las líbrerias **TenserFlow** y **OpenCV** se utilizan para la inteligencia artificial.

- *OpenCV* se utiliza para detectar colores en un video o imagen, por ejemplo para detectar si una persona no cuenta con gafete de la empresa.

- No es recomendable trabajar con nuevas versiones de Python porque se pueden generar conflictos y hay poco soporte técnico

- __Django Celery__ permite ejecutar tareas asíncronas en segundo plano en una aplicación Django.

- Es recomendable trabajar en un entorno virtual para evitar conflictos de versiones

- El interprete hace que se pueda ejecutar el código de Python

---

## Práctica en Pycharm (Básico)

```python
Numero1 = 10
Numero2 = 15
Resultado = Numero1 + Numero2
print(Resultado)

Numero1 = 10
if Numero1==10:
    print('Si es igual a 10')
```

---

## Práctica en Pycharm (OpenCv)
Primero se debe instalar la líbreria Opencv

```bash
pip install opencv-python
```

Se crea una carpeta imagenes.

Una vez creada se realiza lo siguiente:

```python
import cv2
##Se busca la ruta de la imagen
imagen= cv2.imread('imagenes/Pikachu.jpg')

##Se aplican los cambios de color a la imagen
Imagen_Modificada = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
Imagen_Modificada2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

##Se muestran las imagenes
cv2.imshow('Imagen Mostrada', imagen)
cv2.imshow('Imagen Modificada', Imagen_Modificada)
cv2.imshow('Imagen Blanco y Negro', Imagen_Modificada2)

##Se guarda la imagen con los cambios
cv2.imwrite('imagenes/PikachuBlack.jpg',Imagen_Modificada2)

cv2.waitKey(0) ##Al pulsar la tecla 0 se cierra la ventana
cv2.destroyAllWindows()
```

---
## Recursos

- Roboflow es la plataforma para detectar objetos por medio de la visión 

- YoloV8 es un Dataset para localizar y detectar objetos

- Algunos requisitos para utilizar YoloV8 es *procesamiento de datos*, *Big Data* y *Data Analytics*.

- [Repositorio de Ultralytics](https://github.com/ultralytics)
