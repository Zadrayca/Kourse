from abc import ABCMeta, abstractmethod
from unittest import TestCase, main


class Animals(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass

class Duck(Animals):

    def execute(self):
        return 'KRYA'

    def unexecute(self):
        return 'NE KRYA'

class Dog(Animals):

    def execute(self):
        return 'GAW'

    def unexecute(self):
        return 'NE GAW'

class Python(Animals):

    def execute(self):
        return 'TSSSSSSS'

    def unexecute(self):
        return 'MUTE'

#
# x = [Duck(), Dog(), Python()]
# for i in x:
#     i.execute()

if __name__ == '__main__':
    class SimpleTest(TestCase):

        def test_all(self):

            animals = [Duck(), Dog(), Python()]

            out = [a.execute() for a in animals]
            out += [a.unexecute() for a in animals]

            self.assertEqual(['KRYA', 'GAW', 'TSSSSSSS', 'NE KRYA', 'NE GAW', 'MUTE'])

    main()