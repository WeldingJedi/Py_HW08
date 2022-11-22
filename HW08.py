import random
import numpy

def best_gpa_repeating_check(array):
    max_num = max(array)
    max1 = max_num
    array[array.index(max(array))] = 0
    for _ in range(len(array)):
        if max(array) == max1:
            print(f'group {array.index(max(array)) + 1}')
            array[array.index(max(array))] = 0
        else:
            break


def beauty_temperature_print(array):
    print(f'May temperature:\n{array[0]}')
    print(f'June temperature:\n{array[1]}')
    print(f'July temperature:\n{array[2]}')
    print(f'August temperature:\n{array[3]}')
    print(f'September temperature:\n{array[4]}')


def min_temperature_dates(array):
    flag = []
    buf = 100
    for i in range(5):
        min_temperature_in_month = 100
        for j in range(len(array[i]) - 6):
            flag_temperature_in_month = sum(array[i][j:j+7:1]) / 7
            if flag_temperature_in_month < min_temperature_in_month:
                min_temperature_in_month = flag_temperature_in_month
                date = j
                month = i
        if min_temperature_in_month < buf:
            buf = min_temperature_in_month
            flag.append(min_temperature_in_month)
            flag.append(date)
            flag.append(month)
    ind = flag.index(min(flag[::3]))
    print(f'The lowest temperature was in the period '
        f'{flag[ind+1]+1}.0{flag[ind+2]+5}.2021-{flag[ind+1]+7}.0{flag[ind+2]+5}.2021 '
        f'and was {min(flag[::3])}*C')


def max_temperature_dates(array):
    flag = []
    buf = 0
    for i in range(5):
        max_temperature_in_month = 0
        for j in range(len(array[i]) - 6):
            flag_temperature_in_month = sum(array[i][j:j+7:1]) / 7
            if flag_temperature_in_month > max_temperature_in_month:
                max_temperature_in_month = flag_temperature_in_month
                date = j
                month = i
        if max_temperature_in_month > buf:
            buf = max_temperature_in_month
            flag.append(max_temperature_in_month)
            flag.append(date)
            flag.append(month)
    ind = flag.index(max(flag[::3]))
    print(f'The highest temperature was in the period '
        f'{flag[ind+1]+1}.0{flag[ind+2]+5}.2021-{flag[ind+1]+7}.0{flag[ind+2]+5}.2021 '
        f'and was {max(flag[::3])}*C')


def question_random(start = 1, end = 20):
    return random.randrange(start // 2, end // 2) * 2 + 1


def read_question(position):
    with open('.\HW08\Arkadich.txt', 'r', encoding='utf-8') as file:
        question = file.read().split('\n')[position-1]
        return question


def decrypting_question(question):
    alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,-'
    step = 3
    res = ''
    for sym in question:
        res += alphabet[(alphabet.index(sym) - step) % len(alphabet)]
    print(res)


def read_answer(position):
    with open('.\HW08\Arkadich.txt', 'r', encoding='utf-8') as file:
        answer = file.read().split('\n')[position]
        # decrypting_answer(answer)
        return answer


def decrypting_answer(answer):
    alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,-'
    step = 3
    res = ''
    for sym in answer:
        res += alphabet[(alphabet.index(sym) - step) % len(alphabet)]
    # print('*' * len(res))
    return res


def game(answer):           # какая-то проблема с методом keyboard, приходится выкручиваться
    print('*' * len(answer))
    first_q = input('Слово целиком (1) или назовёте букву(2)?: ')
    if first_q == '1': word_enter(answer)
    elif first_q == '2': letter_enter(answer)
    else: 
        print('Попробуйте ещё разок')
        game(answer)
    

def word_enter(answer):
    word = input('Если слово угадаете не правильно, игра завершится\nВведите слово: ').upper()
    print(answer)
    print('Вы победитель!' if word == answer else 'Вы банкрот!')


def letter_enter(answer):
    letter = ['*'] * len(answer)
    print(''.join(letter))
    while True:
        symbol = input('Введите букву: ').upper()
        for i in range(len(answer)):
            if answer[i] == symbol:
                letter[i] = symbol
        word = ''.join(letter)
        print(word)
        if word == answer:
            print('Вы победитель!')
            break


def task01():
    # Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
    # Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

    rows = random.randint(3, 7)
    columns = random.randint(20, 30)
    group_performance = [0] * rows
    group_scores = []
    for i in range(len(group_performance)):
        group_performance[i] = list(None for _ in range(columns))
    for i in range(rows):
        gpa = 0                                 # great point average
        for j in range(columns):
            score = random.randint(2, 5)
            group_performance[i][j] = score
            gpa = gpa + score
        group_scores.append(gpa / columns)
    for group in group_performance:
        print(group)
    print(f'Groups GPA:\n{group_scores}')
    print(f'Best perfomance is in:\ngroup {group_scores.index(max(group_scores)) + 1}')
    best_gpa_repeating_check(group_scores)


def task02():
    # Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите,
    # сумма элементов каких строк превосходит сумму главной диагонали матрицы.

    size = random.randint(2, 6)
    # matrix = numpy.random.random_integers(0, 9, (size, size))
    matrix = numpy.random.randint(0, 9 + 1, (size, size))
    print(matrix)
    main_sum = numpy.sum(numpy.diagonal(matrix, 0))
    print(f'Main diagonal sum is: {main_sum}')
    for i in range(size):
        if numpy.sum(matrix[i]) > main_sum:
            print(f'Sum of row ({i + 1}) {matrix[i]} = {numpy.sum(matrix[i])} > main diagonal sum')


def task03():
    # Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
    # Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
    # Выведите его даты.

    temperature = [[random.randint(15, 30) for days in range(31)] for months in range(5)]
    temperature[1].pop(30)                      # June 30 days
    temperature[4].pop(30)                      # September 30 days
    beauty_temperature_print(temperature)     # OR:
    # for i in range(5):
    #     print(temperature[i])
    min_temperature_dates(temperature)
    max_temperature_dates(temperature)


def task04():
# Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». Вопрос и правильный ответ сохраните в файл.
# Реализуйте алгоритм шифрования правильного ответа.

    print('Добро пожаловать в игру "Усы Аркадьича"!\nИтаааааааааак, вопрос:')
    number = question_random()
    decrypting_question(read_question(number))
    answer = decrypting_answer(read_answer(number))
    game(answer)
    print('До встречи!')
 


# task01()
# task02()
# task03()
# task04()
