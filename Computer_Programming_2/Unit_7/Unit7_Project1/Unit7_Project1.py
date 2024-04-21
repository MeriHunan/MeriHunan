from pathlib import Path
import math
def initialize_image(width:int,height:int,grey_scale:int)->list:
    '''
    Initialize the canvas to be the color of grey_scale

    Parameters
    ----------
    width - int: width of the canvas
    height - int: height of the canvas
    grey_scale - int: greyness of the pixel from 0 - 255

    Return
    ------
    A list containing all of the pixels for the image

    '''
    
    '''image_array = []
    for row in range(height):
        row = []
        for column in range(width):
            row.append(grey_scale)
        image_array.append(row)

    return image_array'''
    return [[grey_scale for i in range(width)] for j in range(height)]

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
    image_string += f"P2\n{width} {height}\n255\n"
    # use a nested for loop to go through array and append
    # info to a string (hint: can use another empty string for the row)
    for row in range(height):
        row_string = ""
        for column in range(width):
            row_string += f"{image_array[row][column]} "
        image_string += f"{row_string.strip()}\n"
    return image_string

def create_file(image_string:str, file_name:str)->bool:
    # to get your relative path, right click this Python file
    # then click Copy Relative Path
    path = Path(rf".\\MeriHunan\\Computer_Programming_2\\Unit_7\\Unit7_Project1\\{file_name}.ppm")
    print(path)
    try:
        path.write_text(image_string)
        return True
    except FileNotFoundError as e:
        print("File cannot be created", e)
        return False
def draw_rect(image_array,x, y, rect_height, rect_width, grayLevel):
    half_width = (rect_width - 1) // 2
    half_height = (rect_height - 1) // 2
    x, y = x + half_width, y + half_height

    for length in range(rect_height):        #going up
        image_array[y-length][x] = grayLevel
        if length == rect_height - 1:
            y = y - length
    for length in range(rect_width):         #going left
        image_array[y][x-length] = grayLevel
        if length == rect_width - 1:
            x = x - length
    for length in range(rect_height):
        image_array[y+length][x] = grayLevel # going down
        if length == rect_height - 1:
            y= y + length
    for length in range(rect_width):         # going right
        image_array[y][x+length] = grayLevel
        if length == rect_width - 1:
            x= x + length
    return image_array

def draw_circle(image_array, ox, oy, radius, lineColor, follColor):
    top_play = 0
    right_play = 0
    x = ox - radius
    y = oy
    while x <= ox:
        hflipy = 2 * oy - y
        hflipx = x
        vflipy = y
        vflipx = 2 * ox - x
        oflipx = vflipx
        oflipy = hflipy
        for xf in range(x, vflipx):
            yf = y
            hflipyf = 2 * oy - yf
            hflipxf = xf
            image_array[yf][xf] = follColor
            image_array[hflipyf][hflipxf] = follColor

        image_array[y][x] = lineColor
        image_array[hflipy][hflipx] = lineColor
        image_array[vflipy][vflipx] = lineColor
        image_array[oflipy][oflipx] = lineColor
        upx = x
        upy = y + 1
        rightx = x + 1
        righty = y
        urx = x + 1
        ury = y + 1
        up_dist = math.sqrt((upx - ox)**2 + (upy - oy)**2) 
        right_dist = math.sqrt((rightx - ox)**2 + (righty - oy)**2)
        ur_dist = math.sqrt((urx - ox)**2 + (ury - oy)**2)
        up_diff = abs(up_dist - radius)
        right_diff = abs(right_dist - radius)
        ur_diff = abs(ur_dist - radius)
        if up_diff < right_diff:
            if up_diff < ur_diff:
                x = upx
                y = upy
            else:
                x = urx
                y = ury
        else: 
            if right_diff < ur_diff:
                x = rightx
                y = righty
            else:
                x = urx
                y = ury

    return image_array

def main():
 #   print("/*Somthing bad")
    #Test commit
    image_data = initialize_image(300,200,150)
#    print(image_data)
    image_data = draw_rect(image_data,150, 110, 70, 140, 0) # Body
    image_data = draw_circle(image_data, 55, 120, 25, 0, 100) # Head
    image_data = draw_rect(image_data, 254, 127, 35, 70, 0) # back legs
    image_data = draw_rect(image_data, 125, 150, 40, 60, 0) # side leg
    image_string = create_image_string(image_data)
    create_file(image_string,"Meri_Test")

if __name__ == '__main__':
    main()