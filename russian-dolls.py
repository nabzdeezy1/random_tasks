print("There is a Russian doll on the table. You open it and find two more dolls, one blue one green.")
key = False
loop = True
while loop == True:
    print("There is a green Russian doll and a blue Russian doll on the table.")
    print("1. Open blue doll")
    print("2. Open green doll")
    choice = input("Enter your choice: ")
    if choice == "2":
        print("The doll contains a small key. You take the key.")
        key = True
    elif choice == "1":
        print("The doll contains a small locked box.")
        if key == True:
            loop = False
print("Congratulations, you have found the golden token!")