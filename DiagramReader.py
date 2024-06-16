import cv2
 
# save read image into different file formats
bmp = cv2.imread('test1.bmp') 
jpg = cv2.imread('test1.jpg') 
png = cv2.imread('test1.png') 
tga = cv2.imread('test1.tga') 
tiff = cv2.imread('test1.tiff')

# print what a pixel of each format looks like
print('bmp: ', bmp[0], '\n')
print('jpg: ', jpg[0], '\n')
print('png: ', png[0], '\n')
#print('tga: ', tga[0], '\n')
print('tiff: ', tiff[0], '\n')
