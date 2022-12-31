def Area(shape):    
    if shape == "rectangle":
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))
        rect_area = l * b
        return "The area of rectangle is: " + str(rect_area)
    elif shape == "square":
        s = int(input("Enter square side: "))
        square_area = s * s
        return "The area of square is: " + str(square_area)
    elif shape == "circle":
        r = int(input("Enter radius of circle: "))
        pi=3.14
        circle_area = pi*r*r
        return "The area of circle is: " + str(circle_area)
    elif shape == "triangle":
        h = int(input("Enter triangle's height length: "))
        b = int(input("Enter triangle's breadth length: "))
        triangle_area=0.5*h*b
        return "The area of triangle is: "+ str(triangle_area)
    elif shape == "parallelogram":
        b = int(input("Enter parallelogram's base length: "))
        h = int(input("Enter parallelogram's height length: "))
        parallelogram_area=b*h
        return "The area of parallelogram is: "+ str(parallelogram_area)
    else:
        print("Sorry! This shape is not available")

