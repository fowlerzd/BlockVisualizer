import cv2
 
# import bmp image
img = cv2.imread('test1.bmp') 

# read in image dimesions
IMG_HEIGHT = img.shape[0]
IMG_WIDTH = img.shape[1]
COLOR_DEPTH = img.shape[2]

# print image info
print("Image Height: ", IMG_HEIGHT)
print("Image Width: ", IMG_WIDTH)
print("Color Depth: ", COLOR_DEPTH)

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
print("Widest White Row Located At: ", widest_white_count_row)

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
print("Tallest White Col Located At: ", tallest_white_count_col)

print()
print("(Row, Col)")

intersect = (widest_white_count_row, tallest_white_count_col)

# determine bounds of each view
top_view_bounds = ((0, 0), (intersect[0]-1, intersect[1]-1))
front_view_bounds = ((intersect[1]-1, 0), (IMG_HEIGHT-1, intersect[1]-1))
side_view_bounds = ((intersect[0]+1, intersect[1]+1), (IMG_HEIGHT-1, IMG_WIDTH-1))

# print bounds of each 
print(f"Top View Bounds: {top_view_bounds[0]} to {top_view_bounds[1]}")
print(f"Front View Bounds: {front_view_bounds[0]} to {front_view_bounds[1]}")
print(f"Side View Bounds: {side_view_bounds[0]} to {side_view_bounds[1]}")

# determine the width, depth, and height of the object
OBJ_WIDTH = top_view_bounds[1][1] - top_view_bounds[0][1] + 1
OBJ_DEPTH = top_view_bounds[1][0] - top_view_bounds[0][0] + 1
OBJ_HEIGHT = IMG_HEIGHT - 1 - OBJ_DEPTH

# print dimensions
print(f"Width: {OBJ_WIDTH}px, Depth: {OBJ_DEPTH}px, Height: {OBJ_HEIGHT}px")

# list of 2D points where black pixels are located
top_points = []
front_points = []
side_points = []

# bounds for pixel search
starting_row = top_view_bounds[0][0]
starting_col = top_view_bounds[0][1]
ending_row = top_view_bounds[1][0]
ending_col = top_view_bounds[1][1]

current_row = starting_row
current_col = starting_col

# print(starting_row, starting_col, ending_row, ending_col, current_row, current_col)

# determine where each black pixel is for the top viwe (row, col)
while(current_row <= ending_row):
    while(current_col <= ending_col):
        view = img.view()[current_row][current_col]
        if((img.view()[current_row][current_col] == [0, 0, 0]).all()):
            top_points.append((current_row, current_col))
        current_col += 1
    current_row += 1

print(top_points)
