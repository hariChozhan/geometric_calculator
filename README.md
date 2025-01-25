# Geometric Calculator

A Python-based geometric calculator that allows users to define and manipulate geometric shapes such as points, lines, circles, rectangles, and polygons. It supports operations like calculating areas, perimeters, and unions of shapes.

## Features

- **Create geometric shapes**: Point, Line, Circle, Rectangle, Polygon.
- **Operations**: Calculate area, perimeter, length of lines, and union of shapes.
- **Interactive**: A command-line interface to define and operate on geometric shapes.

## Prerequisites

This project requires Python 3.6 or higher.

To install Python, visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hariChozhan/geometric_calculator
```
2. Navigate to the project directory:
```bash
cd geometric-calculator
```
3. Run the program:
```bash
python3 run.py
```

## Usage

Once you have the program running, you can interact with it via a simple command-line interface. Below are the instructions for using the various shapes and functions.
Available Shapes
1. Point Class

The Point class defines a 2D point with x and y coordinates.
```bash
p1 = Point(1, 2)
p2 = Point(4, 6)
```
2. Line Class

The Line class is defined by two Point objects. You can calculate the length of the line (distance between two points).
```bash
l1 = Line(p1, p2)
print(l1.length())  # Output: 5.0
```
3. Circle Class

The Circle class is defined by a center Point and a radius. It supports operations like calculating the area and circumference.
```bash
c1 = Circle(p1, 3)
print(c1.area())         # Output: 28.27 (approx.)
print(c1.circumference())  # Output: 18.85 (approx.)
```

4. Rectangle Class

The Rectangle class is defined by two Point objects (bottom-left and top-right corners). You can calculate the area and perimeter of the rectangle.

```bash
r1 = Rectangle(p1, p2)
print(r1.area())        # Output: 12
print(r1.perimeter())   # Output: 14
```

5. Polygon Class

The Polygon class is defined by a list of Point objects. You can calculate the area and perimeter of the polygon.

```bash
poly1 = Polygon([p1, p2, Point(5, 5)])
print(poly1.area())         # Output: 7.5
print(poly1.perimeter())    # Output: 10.0```
```
Union of Shapes

You can calculate the union of two shapes using the union method for each shape or the union_of_shapes function. It supports the following combinations:

    Circle + Circle
    Rectangle + Rectangle
    Polygon + Polygon
    Circle + Rectangle
    Polygon + Circle
    Polygon + Rectangle

# Example:

```bash
# Union of Circle and Rectangle
result = union_of_shapes(c1, r1)
print(result)  # Output: Union of Circle and Rectangle: Area = 45.54

# Union of two Rectangles
r2 = Rectangle(Point(2, 2), Point(6, 6))
result = r1.union(r2)
print(result)  # Output: Rectangle(Point(1, 1), Point(6, 6))
```

# Commands:

Help Command

To view the available commands, type help:

```bash
Commands:
  Define a point: p1 = Point(x, y)
  Define a line: l1 = Line(p1, p2)
  Define a circle: c1 = Circle(p1, radius)
  Define a rectangle: r1 = Rectangle(p1, p2)
  Define a polygon: poly1 = Polygon([Point(x1, y1), Point(x2, y2), ...])
  Union: shape1.union(shape2) or union_of_shapes(shape1, shape2)
  Type 'exit' to quit.
```