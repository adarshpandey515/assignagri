# assignagri

this is my geometry calculator program i made for calculating distances and stuff

## what it does

basically it can calculate distances between different shapes like:
- points
- circles 
- rectangles
- lines

also it can calculate area and perimeter for some shapes

## how to run

just run the main.py file like this:

```
python3 main.py
```

then you can type commands and it will calculate stuff for you!!

## examples

### making a point

```python
p1 = Point(0, 0)
p2 = Point(3, 4)
```

this makes 2 points, one at origin and one at (3,4)

### calculating distance between points

```python
p1 = Point(0, 0)
p2 = Point(3, 4)
p1.calcdist(p2)
```

output: `5.0`

its using pythagorean theorm to calculate distance!!

### making a circle

```python
c = Circle(Point(0, 0), 5)
```

this makes a circle at origin with radius 5

you can also do:
```python
c = Circle()  # makes circle at (0,0) with radius 1
```

### circle stuff

```python
c = Circle(Point(0, 0), 10)
c.calcarea()  # gives you area
c.calccircumfrence()  # gives you circumfrence (i know i spelled it wrong lol)
```

### making rectangles

```python
r = Rectangle(Point(0, 0), Point(4, 3))
```

this makes a rectangle with top left at (0,0) and bottom left at (4,3)

the width and height are calculated automatically!!

```python
r.calcarea()  # area of rectangle
r.calcperimiter()  # perimeter (i spelled this wrong too)
```

### making lines

```python
l = Line(Point(0, 0), Point(5, 5))
```

makes a line from (0,0) to (5,5)

### distance calculations between different shapes

you can calculate distance between any shapes:

```python
# point to circle
p = Point(10, 0)
c = Circle(Point(0, 0), 5)
p.calcdist(c)  # output: 5.0
```

```python
# circle to circle
c1 = Circle(Point(0, 0), 5)
c2 = Circle(Point(10, 0), 3)
c1.calcdist(c2)  # output: 2.0
```

```python
# point to rectangle
p = Point(5, 5)
r = Rectangle(Point(0, 0), Point(3, 3))
p.calcdist(r)  # calculates distance
```

```python
# point to line
p = Point(1, 1)
l = Line(Point(0, 0), Point(2, 0))
p.calcdist(l)  # gives perpendicular distance
```

### interactive mode

when you run the program it starts in interactive mode. you can type commands:

```
Geometry Calc 
 Type 'quit' to exit
>p1=Point(0,0)
>p2=Point(3,4)
>p1.calcdist(p2)
5.0
>c=Circle(Point(0,0),10)
>c.calcarea()
314.1592653589793
>quit
Exiting Geometry Calc
```



## important notes!!

- all coordinates are in 2D (x and y only)
- distances are always positive numbers
- if shapes overlap the distance is 0
- you can chain calculations like `Circle(Point(1,2),5).calcdist(Point(0,0))`

## bugs i know about

- probably some edge cases dont work right
- error messages arent very helpful sometimes
- the rectangle width calculation might be confusing cause it uses bottomleft point

## thats it

thats pretty much all you need to know. just run it and try stuff out!!

sorry , if you find edge cases