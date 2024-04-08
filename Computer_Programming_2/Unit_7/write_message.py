from pathlib import Path

# path = Path(r"Period_8\programming.txt")
# message = "I love Python!"
# message += "\nBut not Java :( " # update using +=
# path.write_text(message)

# prompt one user for their first name 
# then their last name.
# Add their full name to a file called
# guest.txt

# path2 = Path(r"Period_8\guest.txt")
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# full_name = f"{first_name.title()} {last_name.title()}"
# path2.write_text(full_name)

# Exception Handling - reading files
path3 = Path(r'Period_8\alice.txt')
try:
    path3.read_text()
except FileNotFoundError:
    print(f"The file {path3} does not exist.")

user_number = int(input("Enter a number: "))
try:
    user_quotient = 1000/user_number
except ZeroDivisionError:
    print("Don't enter zero")
else:
    print(user_quotient)

file_name = input("Give me a file name: ")
path4 = Path(f"{file_name}.txt")
path4.write_text("Success!")