
from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def unexecute(self) -> None:
        pass

class SimpleCommand(Command):

    def execute(self) -> None:
        print('execute')
        return print(123)

    def unexecute(self) -> None:
        print('unexecute')
        return print(123)

x = SimpleCommand()
print(x.execute(), x.unexecute())