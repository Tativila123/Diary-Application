import diary


def show_menu():
    print("-------My Diary-------")
    print("1. Add entry")
    print("2. Search entries by date")
    print("3. Exit")



def dated_entry():
    while True:
        show_menu()
        option = input("choice an option: ")
        if option == "1":
            diary.add_entry()
        elif option == "2":
            diary.search_entries()
        elif option == "3":
            print("Good bye")
            break
        else:
            print("Invalid option")


dated_entry()
