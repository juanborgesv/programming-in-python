from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Chef(Employee):
    def work(self):
        print('Doing some Chef related work...')

class Waiter(Employee):
    def work(self):
        print('Doing some Waiter related work...')

juan = Waiter()
juan.work()