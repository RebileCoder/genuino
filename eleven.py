#Welcome to the ELEVEN project! This is my new OS in the console. She has a text interface. Her functions is beatiful


print('Благодарим, что выбрали операционную систему ELEVEN\nУделите пять минут на настройку!')
os = input('Мы хотим узнать, что Вам подходит больше.\nВерсия ELEVEN: HOME[1] или PRO[2]: ')
print('Версия установлена')
if os == '1':
    os = 'HOME'
else:
    os = 'PRO'

print('Войдите, чтобы система узнала Вас!')
admin = input('Ваше имя: ')  # имя пользователя
if admin != '':
    d = input(str(admin) + ', хотите защитить систему паролем?[да/нет]: ')
    if d == 'да':
        sew = input('Хотите входить по секретному вопросу?[да/нет] ')
        if sew == 'да':
            task = input('Придумайте вопрос, ответ на который знаете только вы!\nВаш вопрос: ')
            answer = input('Ответ на секретный вопрос: ')
            print('Вопрос сохранён. Теперь при входе в систему будет задаваться предложенный вопрос, и вам нужно будет дать на него ответ.')
        else:
            passwor = input('Придумайте пароль: ')
            password = input('Подтвердите пароль: ')
            if passwor == password:
                print('Пароль успешно установлен')
            else:
                print('Пароли не совпадают, повторите попытку')
    f = open('eleven.txt', 'a')
    f.write('\n')
    f.write('OS: ELEVEN ' + str(os))
    f.write('\n')
    f.write('USER: ' + str(admin))
    if d == 'да':
        if sew == 'да':
            f.write('\n')
            f.write('SECRET TASK: ' + str(task))
            f.write('\n')
            f.write('ANSWER: ' + str(answer))
        else:
            f.write('\n')
            f.write('PASSWORD: ' + str(password))
    f.close()
else:
    print('')

# основная система

elev = True

while elev:
    def notebook():
        step = input('Создать новый файл: New\nОткрыть файл: Open\n')
        if step == 'New' or step == 'new':
            print('Создание нового файла')
            file_name = input('Название файла: ') #просим ввести название файла
            file_name += '.txt'  # добавляем расширение текстового документа txt
            f = open(file_name, 'a')  # создаём новый файл и открываем его на запись
            text = input('Введите сюда ваш текст:\n')  # поле для ввода текста
            f.write(text)  # записываем введённый пользователем текст в созданный файл
        if step == 'Open' or step == 'open':
            print('Открыть файл')
            f_name = input('Название файла(без расширения): ')
            f_name += '.txt'
            f = open(f_name, 'r')
            print(f.read())
            f.close()
    def console(admin):
        power = input('C:/users/' + str(admin) + '/')  # указываем путь
        if power == 'help':
            print('Введите sistem/all чтобы увидеть общую информацию о системе')
        elif power == 'sistem /all':
            print('Общие сведения о системе')
            f = open('eleven.txt', 'r')
            print(f.read())
            f.close()
        else:
            print('Команда ' + str(power) + 'не исполняется')

    apps = 3
    def my_computer(apps):
        print('Количество установленных приложений:' + str(apps))
        f = open('проводник.txt', 'w')
        f.write('\n')
        f.write('MY_COMPUTER')
        f.write('\n')
        f.write('CONSOLE')
        f.write('\n')
        f.write('NOTEBOOK')
        f.write('\n')
        f.close()
        f = open('проводник.txt', 'r')
        print('Приложения:')
        print(f.read())
        f.close()

    def power_app(app_name, user, a):
        print('===================')
        print('|' + str(app_name) + '.sim' + '|')
        print('===================')
        if app_name == 'notebook':
            notebook()
        if app_name == 'console':
            console(user)
        if app_name == 'my computer':
            my_computer(a)
        print('===================')

    # выводим список приложений
    menu = """
        NOTEBOOK[1]
        CONSOLE[2]
        MY COMPUTER[3]
        (q - выйти из системы)
        (block - заблокировать систему)
    """  # меню приложений
    print(menu)
    steppy = input('$ ')  # выбор приложения по его порядковому номеру
    if steppy == 'q':
        elev = False
    elif steppy == 'block':
        print('Система заблокирована')
        name = input('Имя: ')
        if name == admin:
            if d == 'да':
                if sew == 'да':
                    t_a = input('Вопрос: ' + str(task) + '\nОтвет: ')
                    if t_a == answer:
                        print('Система разблокирована')
                    else:
                        print('В доступе откразано')
                        break
                else:
                    rt = input('Введите пароль: ')
                    if rt == password:
                        print('Система разблокирована')
                    else:
                        print('В доступе отказано')
                        break

    elif steppy == '1':
        power_app('notebook', admin, 0)
    elif steppy == '2':
        power_app('console', admin, 0)
    elif steppy == '3':
        power_app('my computer', admin, apps)
    else:
        print('Приложение отсутствует')
