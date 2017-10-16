from PIL import Image
from PIL import ImageFilter
import numpy as np
import cv2

def brightness(color):
    b = color[0] * 0.3 + color[1] * 0.59 + color[2] * 0.11
    return int(b)
def toGreyscale(color):
    b = brightness(color);
    return np.repeat(b, 3)
def averageColor(colors):
    total = np.zeros(3)
    for c in colors:
        total = np.add(total, c)
    return np.divide(total, len(colors))
def colorDistance(c1, c2):
    return pow(c1[0] - c2[0], 2) + pow(c1[1] - c2[1], 2) + pow(c1[2] - c2[2], 2)
def saveImageWithName(v2d, name):
    im = Image.fromarray(v2d.astype('uint8'))
    im.save("images/" + name)

def findFaces():
    num = input('Image num: ')
    img = cv2.imread('images/sample' + num + '.jpg')
    body_cascade = cv2.CascadeClassifier('cascades/frontalface.xml')
    bodies = body_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in bodies:
        print(x)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imwrite('images/result' + num + '.jpg', img)

def manualConvert():
    D = 5 # averaging radius
    T = 1000 # color threshold (0 to 195075)

    # file = input('File name (with ext): ')
    num = input('File num (xxx): ')
    file = 'sample' + num + '.jpg'
    im = Image.open('images/' + file)
    WIDTH, HEIGHT = im.size

    a = np.asarray(im)

    im = im.filter(ImageFilter.FIND_EDGES)
    im.save("images/test.jpg")

    twod_shape = (HEIGHT, WIDTH, 3)

    # soon to be modified image
    m = np.zeros(twod_shape)
    for r in range(HEIGHT):
        for c in range(WIDTH):
            # do something on each pixel
            vals = a[max(r - D, 0):r + D + 1, max(c - D, 0):c + D + 1]
            avg = np.average(np.average(vals, axis=0), axis=0)

            # shape = (int(vals.size/3), 3)
            # neighbors = np.reshape(vals, shape)

            if (colorDistance(avg, a[r, c]) > T):
                m[r, c] = np.ones(3) * 255
            else:
                m[r, c] = np.zeros(3)

    saveImageWithName(m, 'result' + num + '.jpg')


findFaces()