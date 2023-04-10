
def read_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        return lst

def add_contact(surname,name,phone):
    file = open('phonebook.txt', 'a')
    file.write(surname + ' ' + name + ' ' + phone + '\n')
    return surname, name, phone

def find(search):
    line = read_phonebook()
    a = ''
    for l in line:
        if search in l:
            a += l
    return a

def fix_editing(editing, surname, name, phone):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
        fip = surname + ' ' + name + ' ' + phone  + '\n' 
        for i in range(len(line)):
            if editing in line[i]:
                line[i] = fip
    with open('phonebook.txt', 'w', encoding='utf-8') as line1:
        for i in line:
            line1.writelines(i)
        return 'готово'
    
    
def removal(rem):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
        for i in range(len(line)):
            if rem in line[i]:
                line[i] = ''
    with open('phonebook.txt', 'w', encoding='utf-8') as line1:
        for i in line:
            line1.writelines(i)
        return 'готово'