
def bread(funk):
    def new_funk():
        print('=========')
        funk()
        print('=========')
    return new_funk

def tomats(funk):
    def new_funk():
        print('000000000')
        funk()
    return new_funk

def plate(funk):
    def new_funk():
        funk()
        print('\________/')
    return new_funk

@plate
@bread
@tomats
def butterbread():
    print('~~~~~~~~~')


butterbread()
