from pathlib import Path
print("Meri Hunanyan")
"""
Name: Meri Hunanyan
Date: 4/4/2024
Assignment: Unit 7 HW 2
"""
#Problem 1
user_response = [""]
while user_response[-1] != "exit":
    user_response.append(input("What's your name?(exit when your done): "))

path = Path("Computer_Programming_2\\Unit_7\\guest_book.txt")
path.write_text("\n".join(user_response[1:-1]))

#Problem 2
def grade_book_creator(class_test_data: dict) -> None:
    """
    This function takes in the dictionary file and make a text file for each person with their grades in it
    
    Input:
    --------
    class_test_data(dict) - The dictionary
    
    Output: 
    ---------
    None
    """
    for student in class_test_data:
        path_to_student = Path(f"Computer_Programming_2\\Unit_7\\{student.replace(" ", "_")}.txt")    
        text = f"Name: {student}\n"
        for key, value in class_test_data[student].items():
            text += f"{key}: {value}\n"
        path_to_student.write_text(text)

def main() -> None:
    """
    The space to do all the tests in

    Intake:
    --------
    None

    Return:
    --------
    None
    
    """
    class_test_data={
        "Billy Bot":{"Test 1":95,"Test 2":90,"Test 3":87},
        "Samantha Smith":{"Test 1":85,"Test 2":88,"Test 3":91},
        "John Doe":{"Test 1":78,"Test 2":82,"Test 3":79},
        "Emily Jones":{"Test 1":92,"Test 2":95,"Test 3":96},
        "Michael Brown":{"Test 1":88,"Test 2":84,"Test 3":90}
    }
    grade_book_creator(class_test_data)

if __name__ == '__main__':
    main()