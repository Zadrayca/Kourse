

class Sv():
    money_count = 100
    beds = 18
    count_vagons = 0



class Kupe():
    money_count = 40
    beds = 36
    count_vagons = 0


class Platskart():
    money_count = 20
    beds = 54
    count_vagons = 0


class Poezd(Sv, Kupe, Platskart):

    count_sv = 0
    count_kupe = 0
    count_platskart = 0
    count_road = 0
    value_road = 1000

    def __init__(self, name, count_sv, count_kupe, count_platskart, count_road):
        self.count_sv = count_sv
        self.count_kupe = count_kupe
        self.count_platskart = count_platskart
        self.count_road = count_road
        self.name = name
        Sv.count_vagons = count_sv
        Kupe.count_vagons = count_kupe
        Platskart.count_vagons = count_platskart

    def p_name(self):
        print(self.name)

    def value_sv(self):
        return Sv.money_count * Sv.beds * Sv.count_vagons - Sv.count_vagons * self.value_road

    def value_kupe(self):
        return Kupe.money_count * Kupe.beds * Kupe.count_vagons - Kupe.count_vagons * self.value_road

    def value_platskart(self):
        return Platskart.money_count * Platskart.beds * Platskart.count_vagons - Platskart.count_vagons * self.value_road

    def value_poezd(self):
        return (self.value_sv() + self.value_kupe() + self.value_platskart()) * self.count_road

road_list = []

def sozd():
    x = Poezd(input('Введите название поезда: '), int(input('Количество СВ вагонов: ')), int(input('Количество Купе вагонов: ')), int(input('Количество Плацкарт вагонов: ')), int(input('Длинна маршрута (в километрах): ')))
    print('\nИтак, прибыльность', x.name, 'поезда:', x.value_poezd())
    global road_list
    road_list.append(x)

def sps(road_list):
    for a in road_list:
        print('Прибыльность', a.name, 'поезда:', a.value_poezd(), 'рублей.')


def menu():
    """функция выводит меню, принимает выбор пользователя, и возвращает выбор"""
    choise = None
    while choise not in range(0, 3):
        try:
            choise = int(input('''\t\t\tЭто меню управления программой.
            Что-бы создать поезд, и посчитать прибыльность поездки, выберете "1"
            Что-бы что-бы просмотреть список поездов, выберете "2"
            Что-бы выйти из программы выберете "0"\n'''))
        except:
            continue
    return choise

def main():
    choise = None
    print('Здравствуйте, эта программа поможет вам просчитывать прибыльность железнодорожных поездок.')
    while choise != 0:
        choise = menu()
        if choise == 1:
            try:
                sozd()
            except:
                print('Ошибка!')
        elif choise == 2:
            try:
                sps(road_list)
            except:
                print('Ошибка!')
    input('Спасибо за использование нашего П.О. , нажмите Ентер чтобы выйти.')

main()

