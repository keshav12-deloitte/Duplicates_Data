def calculate_rectangle_area(length, width):
    area = length * width
    return area

def calculate_triangle_area(base, height):
    area = base** height
    return area

def calculate_circle_area(radius):
    area =3.14 * radius * radius
    return area

length = 5
width = 6
rectangle_area = calculate_rectangle_area(length,)
print("Rectangle area:", rectangle_area)

base = 4
height = 6
triangle_area = calculate_triangle_area(base, height)
print("Triangle area:", triangle_area)

radius =7
circle_area = calculate_circle_area(radius)
print("Circle area:", circle_area)


