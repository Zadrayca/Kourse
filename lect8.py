# coding: utf-8
# поезд пошел по маршруту, функция сдел поворот на вход дается тру или фолс, поворот или тупик проверяем и выводим.

train_speed = 90

def train(x, train_speed):
    if x == True:
        try:
            train_speed / 0
        except:
            print('Произошла катастрофа!!!')
            train_speed -= 90
            return train_speed
    elif x == False:
        print('Поезд успешно повернул.')
        train_speed += 10
    return train_speed



train_speed = train(True, train_speed)
print('Скорость поезда -', train_speed)