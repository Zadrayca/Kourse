
# МЕТАКЛАССЫ

type # метакласс, базовый

class SomeNewClass:
    pass


# создан метакласссом type

class SomeOtherMeclass(type):

    def __new__(cls, name, bases, namespase, **kwds):
        name += ' by AnimalMetaclass'
        #return super().__new__(name, bases, namespase, kwds)

        print('create class: {} bases: {} namespase: {}'.format(name, namespase, kwds))

        ret = type(name, bases, kwds)

        #print(namespase)

        for nm_name in namespase:
            if nm_name.startswith('__'):
                continue
            if nm_name.upper() != nm_name:
                raise Exception('Need upper names in class {}'.format(name))

        return ret


class SomOtherClass(metaclass=SomeOtherMeclass):

    # def some_other_method(self):
    #     pass

    def SOME_OTHER_METHOD(self):
        pass

# этот класс создан SomOtherMeclass

# перед __init__ запускается __new__
# При создании класса запускается __init__
#

print(globals())