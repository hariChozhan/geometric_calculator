import math

class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            print("Invalid Input: x and y must be numbers.")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        if not isinstance(other, Point):
            print("Invalid Input: Input values must be Points")
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Line:
    def __init__(self, point1, point2):
        if not all(isinstance(p, Point) for p in [point1, point2]):
            print("Invalid Input: Line must be Point objects.")
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return f"Line({self.point1}, {self.point2})"

    def length(self):
        return self.point1.distance(self.point2)


class Circle:
    def __init__(self, center, radius):
        if not isinstance(center, Point):
            raise ValueError("Invalid Input: Center must be a Point.")
        if radius <= 0:
            raise ValueError("Invalid Input: Radius must be positive.")
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle(Center={self.center}, Radius={self.radius})"

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def union(self, other):
        if isinstance(other, Circle):
            return f"Union of Circle and Circle: Area = {self.area() + other.area()}"
        elif isinstance(other, Rectangle):
            return f"Union of Circle and Rectangle: Area = {self.area() + other.area()}"
        else:
            raise ValueError("Invalid Input: Union not supported for Circle and this shape.")


class Rectangle:
    def __init__(self, bottom_left, top_right):
        if not all(isinstance(p, Point) for p in [bottom_left, top_right]):
            raise ValueError("Invalid Input: Rectangle corners must be Point objects.")
        if bottom_left.x >= top_right.x or bottom_left.y >= top_right.y:
            raise ValueError("Invalid Input: Invalid rectangle coordinates.")
        self.bottom_left = bottom_left
        self.top_right = top_right

    def __repr__(self):
        return f"Rectangle({self.bottom_left}, {self.top_right})"

    def area(self):
        return (self.top_right.x - self.bottom_left.x) * (self.top_right.y - self.bottom_left.y)

    def perimeter(self):
        return 2 * ((self.top_right.x - self.bottom_left.x) + (self.top_right.y - self.bottom_left.y))

    def union(self, other):
        if isinstance(other, Rectangle):
            min_x = min(self.bottom_left.x, other.bottom_left.x)
            min_y = min(self.bottom_left.y, other.bottom_left.y)
            max_x = max(self.top_right.x, other.top_right.x)
            max_y = max(self.top_right.y, other.top_right.y)
            return Rectangle(Point(min_x, min_y), Point(max_x, max_y))
        elif isinstance(other, Circle):
            return f"Union of Rectangle and Circle: Area = {self.area() + other.area()}"
        else:
            raise ValueError("Invalid Input: Union not supported for Rectangle and this shape.")


class Polygon:
    def __init__(self, points):
        if not all(isinstance(p, Point) for p in points):
            raise ValueError("Invalid Input: Polygon must be a list of Point objects.")
        self.points = points

    def __repr__(self):
        return f"Polygon({self.points})"

    def area(self):
        n = len(self.points)
        area = 0
        for i in range(n):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i + 1) % n].x, self.points[(i + 1) % n].y
            area += x1 * y2 - x2 * y1
        return abs(area) / 2

    def perimeter(self):
        perimeter = 0
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            perimeter += p1.distance(p2)
        return perimeter

    def union(self, other):
        if isinstance(other, Polygon):
            return Polygon(self.points + other.points)
        elif isinstance(other, Circle):
            return f"Union of Polygon and Circle: Area = {self.area() + other.area()}"
        elif isinstance(other, Rectangle):
            return f"Union of Polygon and Rectangle: Area = {self.area() + other.area()}"
        else:
            raise ValueError("Invalid Input: Union not supported for Polygon and this shape.")


def union_of_shapes(shape1, shape2):
    if isinstance(shape1, Circle) and isinstance(shape2, Circle):
        return shape1.union(shape2)
    elif isinstance(shape1, Rectangle) and isinstance(shape2, Rectangle):
        return shape1.union(shape2)
    elif isinstance(shape1, Polygon) and isinstance(shape2, Polygon):
        return shape1.union(shape2)
    elif isinstance(shape1, Polygon) and isinstance(shape2, Circle):
        return shape1.union(shape2)
    elif isinstance(shape1, Polygon) and isinstance(shape2, Rectangle):
        return shape1.union(shape2)
    elif isinstance(shape1, Circle) and isinstance(shape2, Rectangle):
        return shape1.union(shape2)
    elif isinstance(shape1, Rectangle) and isinstance(shape2, Circle):
        return shape2.union(shape1)
    else:
        raise ValueError("Invalid Input: Union operation not defined for the given shapes.")


def main():
    print("*****Geometric Calculator*****")
    variables = {}

    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() == "exit":
                print("Exiting Geometry Calculator.")
                break

            if user_input.lower() == "help":
                print("Commands:")
                print("  Define a point: p1 = Point(x, y)")
                print("  Define a line: l1 = Line(p1, p2)")
                print("  Define a circle: c1 = Circle(p1, radius)")
                print("  Define a rectangle: r1 = Rectangle(p1, p2)")
                print("  Define a polygon: poly1 = Polygon([Point(x1, y1), Point(x2, y2), ...])")
                print("  Union: shape1.union(shape2) or union_of_shapes(shape1, shape2)")
                print("  Type 'exit' to quit.")
                continue

            if "=" in user_input:
                var_name, expression = user_input.split("=", 1)
                var_name = var_name.strip()
                expression = expression.strip()

                variables[var_name] = eval(expression, {"__builtins__": None}, {
                    "Point": Point,
                    "Line": Line,
                    "Circle": Circle,
                    "Rectangle": Rectangle,
                    "Polygon": Polygon,
                    "union_of_shapes": union_of_shapes, 
                    **variables, 
                })
                print(f"{var_name} = {variables[var_name]}")
            else:
                result = eval(user_input, {"__builtins__": None}, {
                    "Point": Point,
                    "Line": Line,
                    "Circle": Circle,
                    "Rectangle": Rectangle,
                    "Polygon": Polygon,
                    "union_of_shapes": union_of_shapes,
                    **variables,  
                })
                print(result)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
