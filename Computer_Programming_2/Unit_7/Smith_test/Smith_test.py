from pathlib import Path

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
print("hello")
def create_file(image_string:str, file_name:str)->bool:
    # to get your relative path, right click this Python file
    # then click Copy Relative Path
    path = Path(rf"Computer_Programming_2\\Unit_7\\Smith_test\\{file_name}.ppm")
    try:
        path.write_text(image_string)
        return True
    except FileNotFoundError:
        print("File cannot be created")
        return False

def draw_rect(image_array,x, y, rect_height, rect_width, grayLevel):
    distance_midpoint = rect_width // 2
    image_array[x][y+distance_midpoint] = "0"
    return image_array
def main():
    image_data = initialize_image(300,200,150)
    print(image_data)
    image_data = draw_rect(image_data,50, 50, 100, 100, 150)
    image_string = create_image_string(image_data)
    create_file(image_string,"Meri_Test")

if __name__ == '__main__':
    main()