cats={
    'Дракариан': 'черный',
    'Рагнорек': 'белый',
    'Рыжик':'рыжий',
    'Стив':'коричневый',
    'Джон':'серый'
}
cat = ' '.join(cats.values()).split()
cat1 = ' '.join(cats.keys()).split()
for i in range(len(cats.keys())):
    catall = cat1[i]+' - '+cat[i]
    print(catall)
stop = 0
while stop !=1:
    print('Хотите добавить кота?')
    ask = input()
    if ask=='Да' or ask=='да':
        cat2 = input()
        color = input()
        cats[cat2]=color
        cat = ' '.join(cats.values()).split()
        cat1 = ' '.join(cats.keys()).split()
        for i in range(len(cats.keys())):
            catall = cat1[i] + ' - ' + cat[i]
            print(catall)
    print('Хотите удалить кота из списка?')
    ask1 = input()
    if ask1 == 'Да' or ask1 =='да':
        cat =' '.join(cats.keys()).split()
        print('Напишыте имя')
        ans = input()
        del cats[ans]
        cat = ' '.join(cats.values()).split()
        cat1 = ' '.join(cats.keys()).split()
        for i in range(len(cats.keys())):
            catall = cat1[i] + ' - ' + cat[i]
            print(catall)
    print('Хватит?')
    ans1=input()
    if ans1=='Да' or ask1== 'да':
        break