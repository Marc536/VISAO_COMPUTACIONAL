import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carregans imagem
img = cv2.imread('AVIAO_01.jpg')


# Convertendo espaço de cores
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

#plot imagens
imagens = [img_rgb,img_gray,img_hsv,img_hls]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()




plt.show()