
# шаблон проэктирования команда

class Base:

    def execute(self):
        pass

class Worker(Base):

    def execute(self):
        print('work')

class Car(Base):

    def execute(self):
        print('drive')

executers = [Worker(), Car(), Car()]
for x in executers:
    x.execute()