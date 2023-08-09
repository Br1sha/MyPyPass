import random


#-------------------------------------------------------------------------------
def Level_1_password():
    # Generate a low strength password composed of digits.
    wordlist = [1,2,3,4,5,6,7,8,9,0,4,5,6]
    random.shuffle(wordlist)

    return ''.join(map(str , wordlist))
# --------------------------------------------------------------------------------
def Level_2_password():
    #  Generate a medium strength password composed of digits and lowercase letters.
    wordlist = [1,2,3,4,5,6,7,8,9,0,4,5,6,7,8,9,0,'p','a','p','a','y']
    random.shuffle(wordlist)

    return ''.join(map(str , wordlist))

# ---------------------------------------------------------------------------------
def Level_3_password():
    #  Generate a high strength password composed of digits, letters (upper and lower), and symbols.
    wordlist = [1,2,3,4,5,6,7,8,9,0,4,5,6,7,8,9,0,'q','w','e','Q','W','E','t','T','y','Y','i','I','a','A','s','S','d','m','M','x','x','!','@','#','$','%','^','&','*','(',')','-','=','[',']','{}']
    random.shuffle(wordlist)

    return ''.join(map(str , wordlist))

# If You See my Code Thank You
while True:
    User_input = input("Select the desired password strength level:\nType 1 for Low strength\nType 2 for Medium strength\nType 3 for High strength\nType Your Input : ")

    if User_input != "":
        if User_input == "1":
            print(Level_1_password())

        elif User_input == "2":
            print(Level_2_password())
        elif User_input == "3":
            print(Level_3_password())
        break
