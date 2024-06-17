import cv2
 
# import bmp image
bmp = cv2.imread('test1.bmp') 


print("Height: ", bmp.shape[0])
print("Width: ", bmp.shape[1])
print("RGB Values: ", bmp.shape[2])

# print pixel 0, 0 (height, width)
print(bmp.view()[0][0]) # [0 0 0] is black
print(bmp.view()[0][6]) # [255 255 255] is white
