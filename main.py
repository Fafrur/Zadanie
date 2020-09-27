""" 
Ку, прога регистрирует пользователей, записывает данные в файл, так-же можно произвести авторизацию, посмотреть всех пользователей, поменять пароль, поменять имя

"""





import os
import pickle




class Account: #Класс куда записываются объект - аккаунт
    def __init__(self, login, password, name): 
        self.login = login
        self.password = password
        self.name = name
    
    def change_pass(self, old, new, id):  # Функция смены пароля
        if self.password == old:
            self.password = new
            i = ddd(id)
            file = "people" + i
            if os.path.exists(file):      # Записываю изменения в файл
                f = open (file, 'wb')
                person = {"login": self.login, "password": self.password, "name": self.name}
                pickle.dump(person, f)
            return 1
            print("Смена пароля прошла успешно")
        else:
            return 2
    
    def change_name(self, name, id):      # Функция смены имени
        self.name = name
        i = ddd(id)
        file = "people" + i
        if os.path.exists(file):          # Записываю изменения в файл
                f = open (file, 'wb')
                person = {"login": self.login, "password": self.password, "name": self.name}
                pickle.dump(person, f)
        return 1

    def out(self):                        # Функция вывода имен всех пользователей
        print(self.name, "\n")






def ddd(id):                              # Функция поиска нужного файла по id
    i = '1'
    while id != 0:
        i += '1'
        id -= 1
    return i




def w():                                  # Функция поиска последнего файла
    i = '1'
    while True:
        file = "people" + i
        if os.path.exists(file):
            i += '1'
        else:
            return file




def cl(person):                           # Функция записи данных из всех в файлов в класс при запуске программы + считает кол-во пользователей(id)
    list = []
    i = '1'
    j = 0
    while True:
        file = "people" + i
        if os.path.exists(file):
            p = {}
            f = open(file, 'rb')
            try:                          # Тут она иногда ломалась и не создавала новый объект из данных последнего файла, я бомбанул и въебал исключение :)
                p = pickle.load(f)
            except:                       # Беру последний объект не из файла а напрямую из программы(вводил его при регистрации)
                p = person
            list.append(Account(p['login'], p['password'], p['name']))
            i += '1'
            j += 1
            f.close
        else:
            break
    return(j, list) 





def check():                              # Функция проверки логина при регистрации(логины не должны повторяться)
    
    flag = 0
    i = '1'
    print("Введите логин - ")
    login = input ()
    while flag == 0:
        file = "people" + i
        if os.path.exists(file):          
            f = open(file, 'rb')                        
            person = pickle.load(f)       
            if login == person['login']:
                print("Этот логин уже занят, попробуйте еще раз\n")
                print("Введите логин - ")
                login = input ()
                i = '0'
                flag = 0
            i += '1'
            f.close
        else:
            flag = 1
    return (login)





def reg():                                # Функция регистрации
    
    login = check()
    print("Введите пароль - ")
    password = input()
    print("Введите ваше Имя - ")
    name = input()

    person = {"login": login, "password": password, "name": name}

    file = w()
    f = open (file, 'wb')
    pickle.dump(person, f)
    f.close
    id, list = cl(person)
    return id, list





def auth(login, password):                # Функция авторизации(проверка всех файлов на нужный логин и пароль)

    flag = 0
    i = '1'
    j = 0
    list = []
    while flag == 0:
        file = "people" + i
        if os.path.exists(file):
            j += 1
            f = open(file, 'rb')
            person = pickle.load(f)
            if login == person['login']:
                flag = 1
                if (password != person['password']):
                    f.close
                    id, list = cl(person)
                    return -1, list
                    flag = 1
                if (password == person['password']):
                    f.close
                    id, list = cl(person)
                    return j, list
                    flag = 1
            f.close
        else:
            return -1

    f.close
    return 0





def avto():                               # Функция вызова функции авторизации или регистрации
    while True:
        print ("Введите логин - ")
        login = input()
        print ("Введите пароль - ")
        password = input()
        id, list = auth(login, password)
        if id == -1:
            print ("Вы ввели неверный логин или пароль попробуйте еще раз или зарегистрируйтесь\n 1 - Еще раз\n 2 - Зарегистрироваться")
            ch = int(input())
            if (ch == 2):
                id, list = reg()
                return id, list
        else:
            print ("Авторизация прошла успешно")
            return id, list





print ("Авторизуйтесь или зарегистрируйтесь\n 1 - Авторизоваться \n 2 - Зарегистрироваться")
choice = int(input ())                    # Меню регистрации/авторизации
if choice == 1:
    id, list = avto()
if choice == 2:
    id, list = reg()
id = id - 1



flag = 0
while flag == 0:                          # Основное меню
    print ("Меню\n 1 - изменить пароль\n 2 - изменить имя\n 3 - посмотреть имена всех зарегистрированных пользователей\n 4 - сменить пользователя \n 5 - выйти\n")
    choice = int(input())


    
    if choice == 1:
        c = 1
        while c == 1:
            print ("Введите старый пароль - ")
            old = input()
            print ("Введите новый пароль - ")
            new = input()
            c = list[id].change_pass(old, new, id)
            if c == 1:
                print("Смена пароля прошла успешно")
                c = 0
            else:
                print("Был введен неверный пароль\n")
                print("Еще раз? 1 - да 2 - нет")
                c = int(input ())



    if choice == 2:
        print ("Введите новое имя - ")
        name = input()
        c = list[id].change_name(name, id)
        if c == 1:
            print ("Смена имени прошла успешно")
        else:
            print ("Упс, что-то пошло не так")



    if choice == 3:
        d = 0
        while d != id + 1:
            list[d].out()
            d += 1



    if choice == 4:
        id, list = avto()
        id = id - 1



    if choice == 5:
        flag = 1
    