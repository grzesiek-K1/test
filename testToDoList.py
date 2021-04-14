chosen_number = -1
index = "0"
list = []

def Menu():
    print("1: Wyświetl listę")
    print("2: Dodaj do listy")
    print("3: Zapisz listę")
    print("4: Usuń z listy")
    print("5: Wyjdź")

def Show_List():
    print(list)

def Add_List():
    Add_List_Problem = input("Dodane zadanie: ")
    list.append(Add_List_Problem)

def Saved_File():
    print("coming soon")


def Delete_Index():
    print("Co chcesz usunąć")
    for lists in list:
        print(lists)

    index_number = int(input("Podaj index zaczynając od zera "))
    list.pop(int(index_number))


while chosen_number != 5:

    if chosen_number == 1:
        Show_List()
    if chosen_number == 2:
        Add_List()
    if chosen_number == 3:
        Saved_File()
    if chosen_number == 4:
        Delete_Index()


    Menu()
    chosen_number = int(input("Wybrany numer: "))