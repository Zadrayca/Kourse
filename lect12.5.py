


class Worker:

    @property
    def sum_prop(self):
        return 'Hello'

    @property
    def sum_prop2(self):
        if hasattr(self, '_sum_prop_2_value'):
            return self._sum_prop_2_value
        return '333333333'

    @sum_prop2.setter
    def sum_prop2(self, val):
        self._sum_prop_2_value = val


w = Worker()
print(w.sum_prop)

#w.sum_prop = 'fghfdhfh' - ОШИБКА

print(w.sum_prop2)
w.sum_prop2 = '1111111'
print(w.sum_prop2)