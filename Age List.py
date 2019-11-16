# List program

# defines ages
print("Please start by giving the ages to make the list")
Age1 = int(input("Please insert age: "))
Age2 = int(input("Please insert age: "))
Age3 = int(input("Please insert age: "))
Age4 = int(input("Please insert age: "))
Age5 = int(input("Please insert age: "))
Agelist = [Age1, Age2, Age3, Age4, Age5]
print("____________________")
print("")

while True:
    print("Menu:")
    print("1) Input a new list.")
    print("2) Show current list.")
    print("3) Find oldest in list.")
    print("4) Find Youngest in list.")
    print("5) Count an age.")
    print("6) Remove an age from the list given.")
    print("7) Reverse the list.")
    print("8) Sort the list")
    print("9) Quit")
    user_input = input(": ")

    if user_input == "9":
        print("Exiting...")
        break  # Exits program


    elif user_input == "1":
        Age1 = int(input("Please insert age: "))
        Age2 = int(input("Please insert age: "))
        Age3 = int(input("Please insert age: "))
        Age4 = int(input("Please insert age: "))
        Age5 = int(input("Please insert age: "))
        Agelist = [Age1,Age2,Age3,Age4,Age5]
        print("____________________")
        print("")

    elif user_input == "2":
        (Num) = len(Agelist)  # Shows list length
        print(Agelist)
        print("List length is " + str(Num) + " instances")
        print("____________________")
        print("")

    elif user_input == "3":
        print("The oldest is: " + str(max(Agelist)))  # Finds largest age
        print("____________________")
        print("")

    elif user_input == "4":
        print("The youngest is: " + str(min(Agelist)))  # Finds largest age
        print("____________________")
        print("")

    elif user_input == "5":
        term = int(input("Which age would you like to search for?: "))  # specifies count term
        print(str(term) + " occurs " + str(Agelist.count(term)) + " times.") # Show how many times 'term' occurs in list
        print("____________________")
        print("")

    elif user_input == "6":
        print(Agelist)
        remove = int(input("Which item on the list would you like to remove?: "))
        Agelist.remove(int(remove))
        print("New list is: " + str(Agelist))
        (Num) = len(Agelist)
        print("List length: " + str(Num))
        print("____________________")
        print("")

    elif user_input == "7":  # Reverses the list
        Agelist.reverse()
        print("New list is: ")
        print(str(Agelist))
        (Num) = len(Agelist)  # Finds list length and shows it
        print("List length: " + str(Num))
        print("____________________")
        print("")

    elif user_input == "8":
        while True:
            print("How would you like to sort?:")
            print("1) Ascending")
            print("2) Desending")
            print("3) Exit to menu")
            sort_choice = input(":")
            if sort_choice == "3":  # Exit to menu
                print("Exiting to menu...")
                break

            elif sort_choice == "1": # Ascending
                Agelist.sort(reverse=False)
                print(str(Agelist))
                print("____________________")
                print("")
            elif sort_choice == "2": # Descending
                Agelist.sort(reverse=True)
                print(str(Agelist))
                print("____________________")
                print("")
            else:
                print("Input not recognised. Try again.")
    else:
        print("Input not recognised. Try again")
