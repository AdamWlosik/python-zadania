from abc import ABC


class Training(ABC):
    """Klasa abstrakcyjna szkolenie"""
    def __init__(self, training, task):
        self.training = training
        self.task = task
        self.title()

    def title(self):
        print(f"Wybrałeś szkolenie: {self.training} i zadanie: {self.task}: ")

    # @abc.abstractmethod
    def solution(self):
        pass
