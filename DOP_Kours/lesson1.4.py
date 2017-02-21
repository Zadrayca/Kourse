# сделать класс который умеет отображать тэг

# <tag>some text</tag>

class MyTag:

    def __init__(self, tag, text):
        self.tag = tag
        self.text = text

    def execute(self):
        return '<{tag}>{text}</{tag}>'.format(tag=self.tag, text=self.text)

class ClassH(MyTag):

    def __init__(self, text):
        super().__init__('h1', text)


class ClassB(MyTag):

    def __init__(self, text):
        super().__init__('b', text)

class ClassSpan(MyTag):

    def __init__(self, text):
        super().__init__('span', text)


if __name__ == '__main__':
    # tagg = MyTag('b', 'test text')
    # print(tagg.execute())
    # h = ClassH('sdfsdfsdg')
    # print(h.execute())

    #q = ClassH('Hello from')
    w = ClassB('some title')
    e = ClassSpan('text')
    q = ClassH('Hello from' + str(e.execute()))
    print(q.execute() + w.execute())