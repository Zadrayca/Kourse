
class Bukva:

    all_bukvs = []

    def __init__(self, bukva):
        self.bukva = bukva
        self.all_bukvs.append(bukva)
    def rename_bukva(self, name, new_name):
        for i, a in enumerate(self.all_bukvs):
            if a == name:
                self.all_bukvs[i] = new_name


Bukva('a')
Bukva('b')
c = Bukva('c')

print(Bukva.all_bukvs)

c.rename_bukva('b', 'B')

print(Bukva.all_bukvs)