from pathlib import Path
print("Meri Hunanyan")
"""
Name: Meri Hunanyan
Assignment: Unit 7 Homework 1
Date: 4/5/2024
"""



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
    # Problem 1
    path = Path("Computer_Programming_2\\Unit_7\\my_learning.txt")
    learned = ["write loops", "use data types and their methods", "write list comprehentions", "write functions", "read from file and write to file", "draw with turtle"] 
    path.write_text("\n".join(f"In Python you can {topic}" for topic in learned))
    contents = path.read_text()
    lines = contents.splitlines()
    print(contents)
    print()
    print(("\n").join([line for line in lines]))
    #Problem 2
    print()
    prog_language = "C++"
    for line in lines:
        print(line.replace("In Python", f"\nIn {prog_language}"), end = "")
    #Problem 3
    path2 = Path("Computer_Programming_2\\Unit_7\\file_reader.py")
    contents_fileread = path2.read_text()
    contents_fileread = contents_fileread.replace("lines = contents.splitlines()", "")
    path2.write_text(contents_fileread.replace("lines","contents.splitlines()"))
if __name__ == '__main__':
    main()