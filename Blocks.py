from turtle import Turtle
import math
from numpy import matmul

# initialize the screen
writer = Turtle()
writer.screen.screensize(500, 500)
writer.screen.title("Block Visualizer")

# 3d points on a cube
point1_3d = [0, 0, 0]
point2_3d = [0, 0, 50]
point3_3d = [0, 50, 0]
point4_3d = [0, 50, 50]
point5_3d = [50, 0, 0]
point6_3d = [50, 0, 50]
point7_3d = [50, 50, 0]
point8_3d = [50, 50, 50]

# list of points to be drawn
points_3d = [point1_3d, point3_3d, point4_3d, point2_3d, point1_3d]

# initilize the list of 2d points
points_2d = points_3d

# this function will return a isomorphized 2d point from a 3d point   
def transform_dimentions(point_3d):
    # transformation matrix for 3d points into 2d isometric view
    transformation_matrix = [[math.sqrt(3), 0, math.sqrt(3)],
                         [1, 2, 1],
                         [math.sqrt(2), -math.sqrt(2), math.sqrt(2)]]
    
    point_2d = []

    x_cord = 0
    y_cord = 0

    for i in range(len(point_3d)):
        x_cord += transformation_matrix[0][i]*point_3d[i]
        y_cord += transformation_matrix[1][i]*point_3d[i]
    
    point_2d = [x_cord, y_cord]

    return point_2d

# transform 3d points into 2d
for i in range(len(points_3d)):
    points_2d[i] = transform_dimentions(points_3d[i])

# draw each desired point (side of a cube)
for point in points_2d:
    writer.goto(point)

writer.screen.mainloop()