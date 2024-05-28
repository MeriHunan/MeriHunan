"""
Name: Smith
Date: 4/2/24
File name: sample_image_creator.py
"""
from pathlib import Path
import math


def initialize_image(width:int,height:int,start_color: tuple)->list:
    return [[start_color for col in range(width)] for row in range(height)]

def create_image_string(image_array:list)->str:
    '''
    P3'
    2 2
    255
    0 0 0 0 0 0
    0 0 0 0 0 0
    '''
    height = len(image_array)
    width = len(image_array[0])
    image_string = f"P3\n{width} {height}\n255\n"
    for row in range(height):
        row_string = ""
        for column in range(width):
            row_string += str(image_array[row][column])+" "
        image_string += row_string.strip()+"\n"
    return image_string

def create_file(image_string:str, file_name:str)->bool:
    path = Path(rf"Period_8\U7_Project_Part1a\{file_name}.ppm")
    try:
        path.write_text(image_string)
        return True
    except FileNotFoundError:
        print("File cannot be created - Directory doesn't exist")
        return False

def draw_rectangle(image_array,rect_top, rect_left, rect_height, rect_width, grayLevel):
    # to be implemented later
    return None


def create_image_string(image_array:list)->str:
    '''
    Turns the image_array into a string that can be written to
    a pgm file

    Parameter
    --------
    image_array:list - a list of grey scale values

    Return
    ------
    A string containing of image data for the pgm file
    '''
    image_string = ""
    # get height of array
    height = len(image_array)
    # get width of array
    width = len(image_array[0])
    # put the header info in the string (P2\width height\255\)
    image_string += f"P3\n{width} {height}\n255\n"
    # use a nested for loop to go through array and append
    # info to a string (hint: can use another empty string for the row)
    for row in range(height):
        row_string = ""
        for column in range(width):
            row_string += f"{image_array[row][column]} "
        image_string += f"{row_string.strip()}\n"
    return image_string

def create_file(image_string:str, file_name:str)->bool:
    """
    Creates a .ppm file in the same directory as this file. If the file is not able to get created it will print an error message
      and return False. If it is able to create it, it will write the given string into it and return True.
    
    Parameters:
    -------------
        image_string(str) - The contents of the created file

        file_name(str) - The name of the created file

    Return:
    ----------
        bool - If the file was able to get created
    
    
    """
    path = Path(rf".\\MeriHunan\\Computer_Programming_2\\Unit_7\\Unit7_Project2\\{file_name}.ppm")
    print(path)
    try:
        path.write_text(image_string)
        return True
    except FileNotFoundError as e:
        print("File cannot be created", e)
        return False   

def draw_rect(image_array:list,x:int, y:int, rect_height: int, rect_width:int, lineColor:tuple, fullColor:tuple) -> list:
    """
    Draws and fills a rectangle in a given grey color. The x and y is in the middle of the drawn rectangle

    Parameter:
    ------------
        image_array(list) - The coordinate list of the image

        x(int) - The x of the center point of the drawn rectangle

        y(int) - The y of the center point of the drawn rectangle

        rect_height(int) - The height of the rectangle

        rect_width(int) - The width of the rectangle

        lineColor(int) - The line grey level of the rectangle

        fullColor(int) - The fill grey level of the rectangle
    
    Return:
    ----------
        image_array(list) - The coordinate list that is going to get turned into an image
    """
    half_width = (rect_width - 1) // 2
    half_height = (rect_height - 1) // 2
    x, y = x + half_width, y + half_height
    for row in range(rect_height):
        for pixel in range(rect_width):
            image_array[y-row][x-pixel] = fullColor

    for length in range(rect_height):        #going up
        image_array[y-length][x] = lineColor
        if length == rect_height - 1:
            y = y - length
    for length in range(rect_width):         #going left
        image_array[y][x-length] = lineColor
        if length == rect_width - 1:
            x = x - length
    for length in range(rect_height):
        image_array[y+length][x] = lineColor# going down
        if length == rect_height - 1:
            y= y + length
    for length in range(rect_width):         # going right
        image_array[y][x+length] = lineColor
        if length == rect_width - 1:
            x= x + length
    return image_array

def calculate_circle_upper_left_points(ox: int, oy: int, radius: int) -> list:
    """
    calculates the circles upper left points but from our perspective it will be the lower left point
    
    Parameter:
    -------------
        ox(int) - The circle's origin's x

        oy(int) - The circle's origin's y

        radius(int) - The radius of the circle
    
    Return:
    -----------
        list - All of the coordinates for the circle
    """
    res = []
    x = ox - radius
    y = oy
    while x <= ox:
        res.append((x, y))

        up_x = x
        up_y = y + 1
        right_x = x + 1
        right_y = y
        up_right_x = right_x
        up_right_y = up_y

        up_origin_dist = math.sqrt((up_x - ox)**2 + (up_y - oy)**2) 
        right_origin_dist = math.sqrt((right_x - ox)**2 + (right_y - oy)**2)
        up_right_origin_dist = math.sqrt((up_right_x - ox)**2 + (up_right_y - oy)**2)
        up_origin_diff = abs(up_origin_dist - radius)
        right_origin_diff = abs(right_origin_dist - radius)
        up_right_origin_diff = abs(up_right_origin_dist - radius)
        prevy = y     
        if up_origin_diff < right_origin_diff:
            if up_origin_diff < up_right_origin_diff:
                x = up_x
                y = up_y
            else:
                x = up_right_x
                y = up_right_y
        else: 
            if right_origin_diff < up_right_origin_diff:
                x = right_x
                y = right_y
            else:
                x = up_right_x
                y = up_right_y
    return res

def upper_left_to_lower_left(x:int, y:int, ox:int, oy:int) -> tuple:
    """
    Gets the x and y and flips them horizontally. In our perspective it would be the upper left point

    Parameter:
    -----------
        x(int) - The x of the point to be flipped

        y(int) - The y of the point to be flipped

        ox(int) - The origin x of the circle

        oy(int) - The origin y of the circle
    
    Return:
    --------
        tuple - The x and the y of the new point
    """
    return (x, 2 * oy - y)

def upper_left_to_upper_right(x:int, y:int, ox:int, oy:int) -> tuple:
    """
    Gets the x and y and flips them vertically. In our perspective it would be the upper right point

    Parameter:
    -----------
        x(int) - The x of the point to be flipped

        y(int) - The y of the point to be flipped

        ox(int) - The origin x of the circle

        oy(int) - The origin y of the circle
    
    Return:
    --------
        tuple - The x and the y of the new point
    """
    return (2 * ox - x, y)

def upper_left_to_lower_right(x: int, y:int, ox:int, oy:int) -> tuple:
    """
    Gets the x and y and flips them on the origin. In our perspective it would be the lower right point

    Parameter:
    -----------
        x(int) - The x of the point to be flipped

        y(int) - The y of the point to be flipped

        ox(int) - The origin x of the circle

        oy(int) - The origin y of the circle
    
    Return:
    --------
        tuple - The x and the y of the new point
    """
    return (2 * ox - x, 2 * oy - y)

def draw_4_points_and_fill_line(image_array: list, x: int, y: int, ox: int, oy: int, line_color: tuple, fill_color: tuple) -> None:
    """
    Draw 4 points and fills line in between two lower points points, right and left

    Parameter:
    ------------
        image_array(list) - The coordinate list of the image

        x(int) - In the computer's perspective the upper left x 

        y(int) - In the computer's perspective the upper left y 
        
        ox(int) - The origin of the circle

        oy(int) - The origin of the circle

        line_color(int) - The greylevel of the the line

        fill_color(int) - The greylevel of the fill

    Return:
    ----------
        None
    """
    upper_left_x = x
    upper_left_y = y
    lower_left_x, lower_left_y = upper_left_to_lower_left(x, y, ox, oy)
    upper_right_x, upper_right_y = upper_left_to_upper_right(x, y, ox, oy)
    lower_right_x, lower_right_y = upper_left_to_lower_right(x, y, ox, oy)
    image_array[upper_left_y][upper_left_x] = line_color
    image_array[lower_left_y][lower_left_x] = line_color
    image_array[upper_right_y][upper_right_x] = line_color
    image_array[lower_right_y][lower_right_x] = line_color
    if fill_color is not None:
        for lx in range(upper_left_x + 1, upper_right_x):
            image_array[upper_left_y][lx] = fill_color
            image_array[lower_left_y][lx] = fill_color

def draw_circle(image_array: list, **kwargs) -> list:
    """
    Draws the circle.
    
    Parameter:
    ------------
        image_array(list) - The coordinate list of the image

        ox(int) - The origin x of the circle
    
        oy(int) - The origin y of the circle

        radius(int) - The radius of the circle

        line_color(tuple) - The color level of the line

        fill_color(tuple) - The color of the fill

    Return:
    --------
        list - Returns the updated image_array list
    """
    ox = kwargs["originx"]
    oy = kwargs["originy"]
    radius = kwargs["radius"]
    line_color = kwargs["line_color"]
    fill_color = kwargs.get("fill_color", None)
    prev_y = oy - 1
    for x, y in calculate_circle_upper_left_points(ox, oy, radius):
        fill = None
        if prev_y != y:
            fill = fill_color
        draw_4_points_and_fill_line(image_array, x, y, ox, oy, line_color, fill)
        prev_y = y
    return image_array

def draw_4_points_and_fill_line_partial(image_array:list, x:int, y:int, ox:int, oy:int, line_color: tuple, fill_color: tuple, ul:bool, ur:bool, ll:bool, lr:bool) -> None:
    """
    Draws points and draws a half line from the point to the origin. The number of points drawn is based on the bool value of ul, ur, ll, lr.

    Parameters:
    ---------------
        image_array(list) - The coordinate list of the image

        x(int) - The upper left corner coordinate x of the circle

        y(int) - The upper left corner coordinate y of the circle

        ox(int) - The origin x of the circle

        oy(int) - The origin y of the circle

        line_color(tuple) - The color of the line

        fill_color(tuple) - The color level of the fill

        ul(bool) - If the upper left side is going to be filled or not

        ur(bool) - If the upper right side is going to be filled or not

        ll(bool) - If the lower left side is going to be filled or not

        lr(bool) - If the lower right side is going to be filled or not
    
    Return:
    ----------
        None
    
    """
    upper_left_x = x
    upper_left_y = y
    lower_left_x, lower_left_y = upper_left_to_lower_left(x, y, ox, oy)
    upper_right_x, upper_right_y = upper_left_to_upper_right(x, y, ox, oy)
    lower_right_x, lower_right_y = upper_left_to_lower_right(x, y, ox, oy)
    if ul:
        image_array[upper_left_y][upper_left_x] = line_color
    if ll:
        image_array[lower_left_y][lower_left_x] = line_color
    if ur:
        image_array[upper_right_y][upper_right_x] = line_color
    if lr:
        image_array[lower_right_y][lower_right_x] = line_color
    if fill_color is not None:
        if ul or ur:
            if ul:
                start = upper_left_x + 1
            else:
                start = ox + 1
            if ur:
                stop = upper_right_x
            else:
                stop = ox + 1
            for lx in range(start, stop):
                image_array[upper_left_y][lx] = fill_color
        if ll or lr:
            if ll:
                start = lower_left_x + 1
            else:
                start = ox + 1
            if lr:
                stop = lower_right_x
            else:
                stop = ox + 1
            for lx in range(start, stop):
                image_array[lower_left_y][lx] = fill_color

def draw_circle_partial(image_array, **kwargs):
    """
    Draws the circle partially. The bool value of ul, ur, ll, lr decide which circle side is going to be drawn and filled
    
    Parameter:
    ------------
        image_array(list) - The coordinate list of the image

        ox(int) - The origin x of the circle
    
        oy(int) - The origin y of the circle

        radius(int) - The radius of the circle

        line_color(tuple) - The color of the line

        fill_color(tuple) - The color of the fill

        ul(bool) - If the upper left side is going to be filled or not

        ur(bool) - If the upper right side is going to be filled or not

        ll(bool) - If the lower left side is going to be filled or not

        lr(bool) - If the lower right side is going to be filled or not

    Return:
    --------
        list - Returns the updated image_array list
    """
    ox = kwargs["originx"]
    oy = kwargs["originy"]
    radius = kwargs["radius"]
    line_color = kwargs["line_color"]
    fill_color = kwargs.get("fill_color", None)
    ul = kwargs.get("ul", False)
    ur = kwargs.get("ur", False)
    ll = kwargs.get("ll", False)
    lr = kwargs.get("lr", False)
    prev_y = oy - 1
    for x, y in calculate_circle_upper_left_points(ox, oy, radius):
        fill = None
        if prev_y != y:
            fill = fill_color
        draw_4_points_and_fill_line_partial(image_array, x, y, ox, oy, line_color, fill, ul, ur, ll, lr)
        prev_y = y
    return image_array

def main():
    """
    The space to do all the tests in

    Intake:
    --------
    None

    Return:
    --------
    None
    """
    image_data = initialize_image(900,600,(0, 0, 0))
    image_data = draw_rect(image_data, 448, 332, 210, 416, (255, 255, 255), (255, 255, 255)) # Body
    image_data = draw_circle(image_data, originx = 165, originy = 360, radius = 75, line_color = (255, 255, 255), fill_color = (255, 255, 255)) # Head
    image_data = draw_rect(image_data, 761, 383, 107, 212, (255, 255, 255), (255, 255, 255)) # back legs
    image_data = draw_rect(image_data, 375, 420, 105, 165, (255, 255, 255), (255, 255, 255)) # side leg
    image_data = draw_circle(image_data, originx = 135, originy = 345, radius = 15, line_color = (255, 255, 255), fill_color = (255, 255, 255)) # Eyes
    image_data = draw_circle(image_data, originx = 129, originy = 348, radius = 6, line_color = (255, 255, 255), fill_color = (255, 255, 255)) # Eyes
    image_data = draw_circle_partial(image_data, originx = 123, originy = 363, radius = 60, line_color = (255, 255, 255), ur = True) # smile
    image_data = draw_circle(image_data, originx = 345, originy = 294, radius = 51, line_color = (255, 255, 255), fill_color = (255, 255, 255)) # shell / body detail 4
    image_data = draw_circle(image_data, originx = 549, originy = 294, radius = 51, line_color = (255, 255, 255), fill_color = (255, 255, 255)) # smile / body detail 5
    image_data = draw_circle_partial(image_data, originx = 240, originy = 228, radius = 105, line_color = (255, 255, 255), fill_color = (255, 255, 255), ur = True)# shell / body detail 1
    image_data = draw_circle_partial(image_data, originx = 447, originy = 228, radius = 102, line_color = (255, 255, 255), fill_color = (255, 255, 255), ul = True, ur = True)# shell / body detail 2
    image_data = draw_circle_partial(image_data, originx = 654, originy = 228, radius = 105, line_color = (255, 255, 255), fill_color = (255, 255, 255), ul = True)# shell /  body detail 3
    image_data = draw_rect(image_data, 375, 450, 54, 165, (255, 255, 255), (255, 255, 255)) # side leg detail
    image_data = draw_rect(image_data, 761, 410, 54, 212, (255, 255, 255), (255, 255, 255)) # back leg detail
    image_data = draw_rect(image_data, 556, 410, 54, 199, (255, 255, 255), (255, 255, 255)) # body detail 1
    image_data = draw_rect(image_data, 267, 410, 54, 54, (255, 255, 255), (255, 255, 255)) # body detail 2
    image_string = create_image_string(image_data)
    create_file(image_string,"Meri_Test")

if __name__ == '__main__':
    main()
