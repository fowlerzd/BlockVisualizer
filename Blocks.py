# import libraries
from turtle import Turtle
import math

'''
# read othographic points
file = open('othographics.txt', 'r')

# initialize point lists
top_points = []
front_points = []
side_points = []

all_points = [top_points, front_points, side_points]

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
'''

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

# 3d points on a cube
point1_3d = [0, 0, 0]
point2_3d = [0, 0, 100]
point3_3d = [0, 100, 0]
point4_3d = [0, 100, 100]
point5_3d = [100, 0, 0]
point6_3d = [100, 0, 100]
point7_3d = [100, 100, 0]
point8_3d = [100, 100, 100]

# list of points to be drawn
points_3d = [point1_3d, point2_3d, point4_3d, point8_3d, point7_3d, point5_3d, point1_3d, point3_3d, point7_3d, point3_3d, point4_3d]

# initilize the list of 2d points
points_2d = points_3d

# initialize the screen
writer = Turtle()
writer.screen.screensize(500, 500)
writer.screen.title("Block Visualizer")

# this function will return a isomorphized 2d point from a 3d point   
def transform_dimentions(point_3d):
    # transformation matrix for 3d points into 2d isometric view
    transformation_matrix = [[math.sqrt(3), 0, -math.sqrt(3)],
                         [1, 2, 1],
                         [math.sqrt(2), -math.sqrt(2), math.sqrt(2)]]
    
    point_2d = []

    x_cord = 0
    y_cord = 0

    # matrix multi
    for i in range(len(point_3d)):
        x_cord += transformation_matrix[0][i] * point_3d[i]
        y_cord += transformation_matrix[1][i] * point_3d[i]
    
    x_cord = x_cord / math.sqrt(6)
    y_cord = y_cord / math.sqrt(6)

    point_2d = [x_cord, y_cord]

    return point_2d

# this function draws all points in a list
def draw_points(points):
    for i in range(len(points)):
        #writer.color(colors[i])
        writer.goto(points[i])

# transform 3d points into 2d
for i in range(len(points_3d)):
    points_2d[i] = transform_dimentions(points_3d[i])

writer.speed(1)

# draw each desired point (side of a cube)
draw_points(points_2d)

writer.screen.mainloop()
