
# действительная зашита атрибутов

class A:

    def _method(self):
        pass

    def __method2(self):
        pass

class B:

    def __getattr__(self, name):
        if name == 'car':
            return 'car-car'
        return None

# b = B()
# print(b.hfghfdgh)


from unittest import TestCase, main

if __name__ == '__main__':
    class SimpleTest(TestCase):

        def test_all(self):
            b = B()

            self.assertEqual(None, b.dfgdfg)

        def test_b(self):
            self.assertEqual('car-car', B().car)

    #main()

class Student:

    def __getattr__(self, name):
        if name == 'name':
            return 'Ivan'
        elif name == 'age':
            return 42
        elif name == 'sity':
            return 'SPb'

    def __setattr__(self, name, value):
        pass

from unittest import TestCase, main

if __name__ == '__main__':
    class SimpleTest(TestCase):

        def test_all(self):
            s = Student()

            self.assertEqual(None, s.dfgdfg)

        def test_b(self):
            self.assertEqual(42, Student().age)
            self.assertEqual('Ivan', Student().name)

        def test_4(self):
            stud = Student()
            stud.work = 'good'
            self.assertEqual(None, stud.work)

    main()