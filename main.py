todos = []
#białe znaki przy input usera (strip)
# txt = "zakupy"
# x=txt.strip()
# print("",x)
#obsługa błedów przy input usera ( rzutowanie na liczby)
#zapisywanie danych w pliku tesktowym
#obsługa błedu przy braku pliku tekstowego


while True:
    user_command = input("Co chcesz zrobić ?")
    if user_command == "add":
        task = input("Jakie zadania chcesz otrzymać ?")
        todos.append(task)
    elif user_command == "show":
        for idx,task in enumerate(todos):
            print(f"{idx +1}. {task}")
    elif user_command == "complete":
        task = input("Jakie zadanie chcesz zakończyc ?")
        todos[int(task)-1]
    elif user_command == "exit":
        break
    else:
        print("Zła komenda")



