import view
import model


def run():
    view.greetings()  
    while True:
        view.menu()
        answer = input('Выбор: ')
        
        if answer == '1':
            data = model.read_phonebook()
            view.show_phonebook(data)    
        
        elif answer == '2':
            surname = input('Введите Фамилию контакта: ')
            name = input('Введите имя контакта: ')
            phone = input('Введите телефон контакта: ')
            
            data2 = model.add_contact(surname,name,phone)
            view.show_add_contact(data2)
            
        elif answer == '3':
            search = input('Введите данные: ')
            
            data3 = model.find(search)
            view.print_find(data3)
        
        elif answer == '4':
            editing = input('Введите параметр для изменения записи: ')
            
            surname = input('Введите Фамилию контакта: ')
            name = input('Введите имя контакта: ')
            phone = input('Введите телефон контакта: ')
            
            data4 = model.fix_editing(editing, surname,name,phone)
            view.print_editing(data4)
            
        elif answer == '5':
            rem = input('Введите данные для удаления: ')
            
            data5 = model.removal(rem)
            view.string_delete(data5)
        
        
        elif answer == '6':
            view.show_break()
            break
        else:
            view.incorrect_answer()