"""
Задаем количество бутылок от 0 до 200.
Нужно вернуть количество и слово бутыл<?> с правильным окончанием.
Пример :
In: 5
Out: 5 бутылок
    
In: 1
Out: 1 бутылка
    
In: 22
Out: 22 бутылки
"""
'''
1 бутылка
2 бутылки
3 бутылки
4 бутылки
5 бутылок
6 бутылок
7 8 9 10 11 12 13 14 15 16 17 18 19 20
21 бутылка

'''
num = int(input('Enter num: '))
if num % 100 // 10 == 1:
    print(num,'бутылок')
elif num % 10 == 1:
    print(num,'бутылка')
elif 2<= num % 10 < 5:
    print(num,'бутылки')
else:
    print(num,'бутылок')


 