# import libraries
from turtle import Turtle
import math
from numpy import matmul

# read othographic points
file = open('othographics.txt', 'r')

# initialize point lists
top_points = []
front_points = []
side_points = []

# first line
line = file.readline()

# read file
if "Top" in line:
    # read in top points
    line = file.readline()
    while "Front" not in line:
        coords = [int(x.strip()) for x in line.split(',')]
        top_points.append(coords)
        line = file.readline()
    # read in front points
    line = file.readline()
    while "Side" not in line:
        coords = [int(x.strip()) for x in line.split(',')]
        front_points.append(coords)
        line = file.readline()
    # read in side points
    line = file.readline()
    while line != "":
        coords = [int(x.strip()) for x in line.split(',')]
        side_points.append(coords)
        line = file.readline()

# debug
print(top_points, front_points, side_points)

# initialize the screen
writer = Turtle()
writer.screen.screensize(500, 500)
writer.screen.title("Block Visualizer")

# this function will return a isomorphized 2d point from a 3d point   
def transform_dimentions(point_3d):
    # transformation matrix for 3d points into 2d isometric view
    transformation_matrix = [[math.sqrt(3), 0, math.sqrt(3)],
                         [1, 2, 1],
                         [math.sqrt(2), -math.sqrt(2), math.sqrt(2)]]
    
    point_2d = []

    x_cord = 0
    y_cord = 0

    # matrix multi
    for i in range(len(point_3d)):
        x_cord += transformation_matrix[0][i]*point_3d[i]
        y_cord += transformation_matrix[1][i]*point_3d[i]
    
    point_2d = [x_cord, y_cord]

    return point_2d



# this function draws all points in a list
def draw_points(points):
    for point in points:
        writer.goto(point)

writer.screen.mainloop()