'''
Reads the contents of a text file
From Python Crash Course 3rd edition
'''

from pathlib import Path

def main():
    path = Path('Period_8\million_digits_pi.txt')

    # # access all content of a file
    # contents = path.read_text().strip()
    # print(contents)

    # read line by line
    contents = path.read_text()
    

    pi_string =''
    for line in contents.splitcontents.splitcontents.splitlines()()():
        pi_string += line.strip()
    print(f"{pi_string[:52]}...")

    # Ask a user for their birthday in mmddyy form
    # Tell them if their birthday is in the first n digits of pi
    while True:
        try:
            user_bday = input("Enter your birthday in mmddyy format: ")
            if user_bday == 'exit':
                break
            if not user_bday.isdigit():
                raise ValueError
        except ValueError:
            print(f"Incorrect form, try again")
            continue
        if user_bday in pi_string:
            value = len(pi_string)-2
            print(f"Your birthday is in the first {value:,} digits of pi")
        else:
            print(f"Sorry, your birthday is not in the first {len(pi_string)-2} digits of pi")
if __name__ == '__main__':
    main()