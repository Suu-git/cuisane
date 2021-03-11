import cv2
import numpy as np
import urllib.request

from keras.models import load_model
model2=load_model('Alphabet/model_detecting_handwritten_alphabet.h5')

def return_word(position):
    a_z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
    return a_z[position].upper()

def index_of_max_element(arr):
    max=arr[0]
    index_return=0
    for i in range(0, len(arr)):
        if arr[i]>max:
            max=arr[1]
            index_return=i
    return (index_return) #position is equal to index plus 1

def detecting_image_alphabet(path_of_image):
    im=cv2.imread(path_of_image,cv2.IMREAD_GRAYSCALE)
    im=cv2.resize(im,(28,28))
    im=im.reshape(28,28,1)
    position = index_of_max_element(model2.predict(np.array([im])).flatten())
    return return_word(position)

def download_image_ipg(url, file_path, file_name):
    fullpath=file_path+file_name+".png"
    urllib.request.urlretrieve(url,fullpath)