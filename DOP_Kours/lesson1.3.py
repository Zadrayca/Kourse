
# делегирование

class SomeAllWorker():

    def __init__(self):
        self.someSimpleWorker = SomeSimpleWorker()
        self.someHardWorker = SomeHardWorker()

    def do_some_hard_work(self):
        self.someHardWorker.execute()

    def do_some_simple_work(self):
        self.someSimpleWorker.execute()


worker = SomeAllWorker()
worker.do_some_hard_work()
worker.do_some_simple_work()

worker.someSimpleWorker = SomeMiddleWorker()
worker.do_some_simple_work()

# иметь возможность менять воркеров = настраивать систему!!!


