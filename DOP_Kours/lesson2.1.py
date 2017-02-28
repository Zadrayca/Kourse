
class Base:

    def execute(self, a, b):
        raise Exception('Not implimented yet!')

class Plus(Base):

    def execute(self, a, b):
        return a + b

class Minus(Base):

    def execute(self, a, b):
        return a - b

class Multiply(Base):

    def execute(self, a, b):
        return a * b

class Divide(Base):

    def execute(self, a, b):
        return a / b

actions = {
    '+': Plus(),
    '-': Minus(),
    '*': Multiply(),
    '/': Divide(),

}

if __name__ == '__main__':
    print(actions['/'].execute(100, 5))

    print(actions['+'].execute(20, 30))

    print(actions['*'].execute(20, 30))

    from unittest import TestCase, main

    class SimpleTest(TestCase):

        def test_multiply(self):
            self.assertEqual(
                600, actions['*'].execute(20, 30)
            )

        def test_plus(self):
            self.assertEqual(
                50, actions['+'].execute(20, 30)
            )



    main()