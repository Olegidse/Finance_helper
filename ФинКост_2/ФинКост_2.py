f = open(input("Please enter the path to your file: "))
expenses = []
names = {}
names_rev = {}
for line in f:
    if not line.isspace():
        expenses.append(line.rstrip()) #Копирование файла в список

words = []
for line in expenses:  #Нахождение всех имён
    word = line.split()
    for element in word:
        if not element.isdigit():
             words.append(element)
#print(words)
nameset = set(words) #Удаление дубликатов
#print(nameset)
i = 0

for name in nameset: #Создание словарей с именами
        names.update({name:i})
        names_rev.update({i:name})
        i+=1
#print(names)
a = i
table = [[0 for i in range(a)] for i in range(a)] #Создание таблицы для записи долгов 
#print(table)

for line in expenses: #Заполнение таблицы долгов 
    words = line.split()
    for word in words[2:len(words)]:
        table[names[words[0]]][names[word]] = table[names[words[0]]][names[word]] + (float(words[1])/(len(words)-2))

i = 0

plus = []
minus = []
while i < a:    #Создание списков с должниками и теми, кому должны
    sum = 0
    j = 0
    while j < a:
        sum += table[i][j]
        sum -= table[j][i]
        j+=1
    if sum < 0:
        minus.append([i,-sum])
    if sum > 0:
        plus.append([i,sum])

        
    i+=1
#print(table)
#print(plus)
#print(minus)

total = []
for i in range(a):
    total.append([0] * a)
current = 0

for person in minus:    #заполнение упрощённой таблицы долгов 
    flag =True
    money = person[1]
    while flag == True:
        if money > plus[current][1]:
            total[plus[current][0]][person[0]] = plus[current][1]
            money -= plus[current][1]
            current += 1
        elif money == plus[current][1]:
            total[plus[current][0]][person[0]] = money
            current += 1
            flag = False
        elif money < plus[current][1]:
            total[plus[current][0]][person[0]] = money
            plus[current][1] -= money
            flag = False


#print(total)

i = 0
while i < a:   #Вывод итоговых значений 
    j = 0
    print(names_rev[i],':')
    while j < a:
        if  not total[j][i] == 0:
            print(total[j][i],' --> ',names_rev[j])
        j+=1
    print('\n')
    i+=1
