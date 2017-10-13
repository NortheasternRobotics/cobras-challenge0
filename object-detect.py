import sys
from PIL import Image
from numpy import*

def brightness(color):
    b = color[0] * 0.3 + color[1] * 0.59 + color[2] * 0.11
    return int(b)

def toGreyscale(color):
    b = brightness(color);
    return repeat(b, 3)

file = input('File name (with ext): ')

im = Image.open('images/' + file)
WIDTH, HEIGHT = im.size

a = asarray(im)

flat_length = WIDTH * HEIGHT
flat_shape = (flat_length, 3)
twod_shape = (HEIGHT, WIDTH, 3)
a_flat = a.reshape(flat_shape);

r = zeros(flat_shape)
for i in range(flat_length):
    # do something on each pixel
    pix = a_flat[i]
    r[i] = toGreyscale(pix)

r = r.reshape(twod_shape)
print(r.shape)
im = Image.fromarray(r.astype('uint8'))
im.save("images/result001", "jpeg")