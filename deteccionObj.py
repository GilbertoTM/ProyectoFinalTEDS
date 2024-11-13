import cv2

class deteccionFondo():
    '''
    Se detecta el contorno de una imagen con un
    contorno homogeneo (o casi).
    '''
    def __init__(self):
        pass
    
    def deteccion(self, img):
        
        # Convertirmos la imagen a escala de grises
        imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Convertimos la imagen en gris en blaco y negro    
        # 255 -> negro
        
        '''
        Param de funcion adaptiveThreshold(fuente, valorMaximo, metodo adaptativo, metodo binario, tamDeanalisis, C) 
        
        Analiza cada pixel de la imagen y su contorno (19x19), saca la media del valor de intensidad de los pixeles y le resta 5 (en este caso)
        despues compara el valor final de la media con el valor de intensidad del pixel actual, si el valor actual es mayor que el de la media
        el pixel se convierte en color negro, en aso contrario se vuelve blanco.
        '''
        imgBlancoNegro = cv2.adaptiveThreshold(imgGris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)
        
        '''
        Buscamos los contornos de la imagen binaria, solo buscamos los contornos externos (retr_external), y comprimimos los contornos dejando slo los puntos
        escenaciales (chain_approx...)
        '''
        contornos, _ = cv2.findContours(image=imgBlancoNegro, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        
        contornosF = []
        
        for cont in contornos:
            area = cv2.contourArea(cont)
            if area > 2000:
                contornosF.append(cont)
        
        return contornosF