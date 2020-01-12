from PIL import Image
import numpy as np

def random_img(output, width, height):

    array = np.random.randint(0,255 , (height,width,3))  

    array = np.array(array, dtype=np.uint8)
    img = Image.fromarray(array)
    #img = Image.fromarray(array).convert('LA') #convert to greyscale
    img.save(output)


random_img('random.png', 1366, 768)
