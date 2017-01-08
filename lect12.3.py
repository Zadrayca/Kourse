
class Vagon:
    def get_money_count(self):
        return self.money_count * self.money_coef()

class KupeVagon(Vagon):
    money_count = 3000
    personal = 2
    beds = 10
    tables = 9

    def money_coef(self):
        return self.beds


class RestoranVagon(Vagon):
    money_count = 1500
    personal = 3
    beds = 0
    tables = 15

    def money_coef(self):
        return self.tables

kupe = KupeVagon()
print('money count', kupe.get_money_count())

rest = RestoranVagon()
print('money count', rest.get_money_count())