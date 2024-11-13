import cv2
import cv2.aruco
import deteccionObj
import numpy as np

# Cargamos imagen
imagen = cv2.imread('img\\ejemplo.jpg') 


# Deteccion de objeto 
detector = deteccionObj.deteccionFondo()
contornos = detector.deteccion(imagen)


# Aruco
parametrosAruco = cv2.aruco.DetectorParameters()
arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
esquinas, ids, rejected = cv2.aruco.detectMarkers(imagen, arucoDict, parameters=parametrosAruco)
print(esquinas)

# Prueba
esquinasInt = np.int32(esquinas)
cv2.polylines(imagen, esquinasInt, True, (0,0,255), 2)
# Perimetro
erimetroAruco = cv2.arcLength(esquinas[0], True)
print(erimetroAruco)


# Pixeles -> CM
pixel_cm = erimetroAruco/20 # Obtenemos el valor de un cm en pixeles

for cont in contornos:
    # Dibujamos el contorno
    cv2.polylines(imagen, [cont], True, (255,0,0), 2)

    # Obtenemos valores del contorno
    rectangulo = cv2.minAreaRect(cont)
    (x,y), (altura, ancho), angl = rectangulo

    altura_cm = altura/pixel_cm
    ancho_cm = ancho/pixel_cm

    # Circulo en el centro del objeto detectado
    cv2.circle(imagen, (int(x), int(y)), 5, (255,0,0), -1)

    # Dibujamos la caja del contorno del objeto para una mayor precision
    caja = cv2.boxPoints(rectangulo)
    caja = np.int32(caja)
    cv2.polylines(imagen, [caja], True, (255, 0, 0), 2)

    # Informacion de las medidas
    cv2.putText(imagen, 'Ancho: {}'.format(round(ancho_cm, 1)), (int(x + int(ancho/2)), int(y - 30)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    cv2.putText(imagen, 'Altura: {}'.format(round(altura_cm, 1)), (int(x - int(ancho/2)), int(y + 30)), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    print(caja)

    # Las coordenadas x y y son el centro del rectangulo
    '''
    print(x,y)
    print(altura, ancho)
    print(angl)
    '''

cv2.namedWindow('Imagen', cv2.WINDOW_NORMAL)
cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
