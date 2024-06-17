import cv2
 
# import bmp image
img = cv2.imread('test1.bmp') 

# read in image dimesions
IMG_HEIGHT = img.shape[0]
IMG_WIDTH = img.shape[1]
IMG_DEPTH = img.shape[2]

print("Image Height: ", IMG_HEIGHT)
print("Image Width: ", IMG_WIDTH)
print("Image Depth: ", IMG_DEPTH)

# find horizontal seperation
white_count = 0
widest_white_count_row = 0
# loop through image
for row in range(IMG_HEIGHT):
    white_count = 0
    for col in range(IMG_WIDTH):
        if((img.view()[row][col] == [255, 255, 255]).all()): # check if pixel is white
            white_count += 1
            if(white_count == IMG_WIDTH): # row is found
                widest_white_count_row = row
                break
        else:
            white_count = 0
print("Widest White Row: ", widest_white_count_row)

# find vertical seperation
white_count = 0
tallest_white_count_col = 0
# loop through image
for col in range(IMG_WIDTH):
    white_count = 0
    for row in range(IMG_HEIGHT):
        if((img.view()[row][col] == [255, 255, 255]).all()): # check if pixel is white
            white_count += 1
            if(white_count == IMG_HEIGHT): # tallest collumn is found
                tallest_white_count_col = col
                break
        else:
            white_count = 0
print("Tallest White Col: ", tallest_white_count_col)

print()
print("(Col, Row)")

intersect = (tallest_white_count_col, widest_white_count_row)

# print bounds of each 
print(f"Top View Bounds: (0, 0) to (" + str(intersect[0]-1) + ", " + str(intersect[1]-1) + ")")
print(f"Front View Bounds: (0, " + str(intersect[1]+1) + ") to (" + str(intersect[0]-1) + ", " + str(IMG_HEIGHT-1) + ")")
print(f"Side View Bounds: (" + str(intersect[0]+1) + ", " + str(intersect[1]+1) + ") to (" + str(IMG_WIDTH-1) + ", " + str(IMG_HEIGHT-1) + ")")
