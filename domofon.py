import time

mieszkania = ['124', '125', '126']
kody = ['5942', '4386', '5660']

while True:
    mieszkanie = input('wpisz numer mieszkania')
    if mieszkanie in mieszkania:
        miejsce = mieszkania.index(mieszkanie)
        kod = input('wpisz kod lub połącz wybierając 0')
        if kod in kody[miejsce] and int(len(kod)) == 4:
            print('Zampraszamy')
            break
        elif kod == '0':
            print('Zaraz rozpocznie łączenie...')
            time.sleep(2)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('Mieszkanie', mieszkanie, 'łączenie...')
            break
        else:
            print('Błędny kod')
            time.sleep(2)
            print('Zaraz rozpocznie łączenie...')
            time.sleep(2)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('Mieszkanie', mieszkanie, 'łączenie...')
        break
    else:
        print('Wprowadź numer jeszcze raz')
