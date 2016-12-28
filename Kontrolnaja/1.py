from save_read import save, read, show

class Galaxy:
    total = 0
    planet_count = 0
    speed_all = 0
    planet_speed = []
    g_list = []
    g_dict = {}
    def __init__(self, name, planet_count, planet_speed):
        Galaxy.total += 1
        Galaxy.planet_count += planet_count
        Galaxy.g_list.append(name)
        Galaxy.g_dict[name] = planet_count
        Galaxy.planet_speed.append(planet_speed)
        print('Появилась новая галактика.')
        self.name = name
        self.planet_count = planet_count
        self.planet_speed = planet_speed

    def change():
        to_dell = input('Введите название галактики, для ее удаления!')
        if to_dell in Galaxy.g_list:
            Galaxy.g_list.remove(to_dell)
        else:
            print('Такой галактики нет в списке')
        to_add = input('Введите название галактики, для ее добавления!')
        if to_add in Galaxy.g_list:
            Galaxy.g_list.append(to_add)
    def save_galaxy(self):
        save(self.planet_count)
    def read_galaxy(self):
        print(read())


class Spaseshep(Galaxy):
    def __init__(self, name, shep_count):
        self.name = name
        self.shep_count = shep_count
    def save_shep(self):
        super().save_galaxy()
    def read_shep(self):
        super().read_galaxy()






x = Galaxy('asda', 5, 15)
e = Galaxy('sdfsdf', 4, 25)
w = Spaseshep('qwe', 15)
# print(Galaxy.g_dict)
# x.planet_count += 1
# print(Galaxy.g_dict)
# Galaxy.change()
# print(Galaxy.g_list)
# save(Galaxy.g_list)
# # show(read())
# x.save_galaxy()
# x.read_galaxy()
w.save_shep()
w.read_shep()