import datetime

def choose_diary():
    print("1. Personal Diary")
    print("2. School Diary")
    print("3. Travel Diary")

    

def add_entry():
    today = datetime.date.today()
    choose_diary()
    choice = input("Choose in what diary you would like to write: ")

    if choice == "1":
        diary = input("Write what you did today ")
        file = open("Personal_diary.txt", "a")
        file.write(str(today) + "-->" + diary + "\n")
        file.close()
        print(today, diary)
    if choice == "2":
        diary = input("Write what you did today ")
        file = open("school_diary.txt", "a")
        file.write(str(today) + "-->" + diary + "\n")
        file.close()
        print(today, diary)
    if choice == "3":
        diary = input("Write what you did today ")
        file = open("travel_diary.txt", "a")
        file.write(str(today) + "-->" + diary + "\n")
        file.close()
        print(today, diary)


def search_entries():
    choose_diary()
    choice = input("Choose a diary to search: ")

    if choice == "1":
        filename = "Personal_diary.txt"
    elif choice == "2":
        filename = "school_diary.txt"
    elif choice == "3":
        filename = "travel_diary.txt"
    else:
        print("Invalid option")
        return

    date = input("what date are you looking for (YYYY-MM-DD): ")
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("This diary does not exist yet")
        return
    count = 0

    for line in file:
        if date == line[:10]:
            print(line)
            count += 1
    if count == 0:
            print("There is no information on that date")
    file.close()

