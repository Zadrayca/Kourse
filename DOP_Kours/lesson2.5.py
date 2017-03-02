from pickle import dump, load

CONFIG_FILENAME = 'conf.ini'

class Config:
    __instance = None

    def __init__(self, filename, **kwargs):
        if not 'fdsgdcvdc' in kwargs and kwargs['fdsgdcvdc'] == 5464684654:
            raise Exception('Do not create Config manuality. Use Config.getinstanse()')

        self.filename = filename
        self.params = {}


    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Config(CONFIG_FILENAME, fdsgdcvdc=5464684654)
        return cls.__instance

    def read(self):
        try:
            with open(self.filename, 'rb') as f:
                self.params = load(f)
        except FileNotFoundError:
            pass

    def write(self):
        with open(self.filename, 'wb') as f:
            dump(self.params, f)

    def __getattr__(self, name):
        return self.params.get(name, None)

    def __setattr__(self, name, value):
        if name in ('params', 'filename'):
            return super().__setattr__(name, value)
        self.params[name] = value

    def __delattr__(self, name):
        pass

if __name__ == '__main__':
    a = Config.get_instance()
    b = Config.get_instance()
    print(a, b, a == b)









    #
    # config = Config(filename='my_config.pickle')
    # config.read()
    # print('main_color:', config.main_color)
    #
    # config.main_color = '#ff0000'
    # config.write()
    #
    #
    #





# при добавлении аттрибута в сетаттр проверять на равенство
# в класс конфиг добавляем техническое свойство "changed"
# попробуйте конфиг сделать синглтоном
#