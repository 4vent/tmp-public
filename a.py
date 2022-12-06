from glob import glob
import cv2

paths = glob('images\\*.jpg')
x, y = 790, 1584
for path in paths:
    img = cv2.imread(path)
    name = path.split('.')[0]
    ext = path.split('.')[-1]
    cv2.imwrite(f'{name}_qr.{ext}', img[y:y + 315, x:x + 315])