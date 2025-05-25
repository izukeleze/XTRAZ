def area_sum(rectangles):
    sum = 0 

    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        sum += area
    return sum