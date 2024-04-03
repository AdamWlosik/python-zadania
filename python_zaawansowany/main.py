from python_zaawansowany.zadania.dekoratory import (
    Task1Dek,
    Task2Dek,
    Task3Dek,
    Task4Dek,
    Task5Dek,
    Task6Dek,
)
from python_zaawansowany.zadania.exceptions import FileHandlerEX, Task2EX
from python_zaawansowany.zadania.generatory_listy_skladane import (
    Task1GLS,
    Task2GLS,
    Task3GLS,
    Task4GLS,
    Task5GLS,
    Task6GLS,
    Task7GLS,
)
from python_zaawansowany.zadania.programowanie_funkcyjne import (
    Task1PF,
    Task2PF,
    Task3PF,
    Task4PF,
    Task5PF,
    Task6PF,
    Task7PF,
    Task8PF,
)
from python_zaawansowany.zadania.regex import (
    Task1Regex,
    Task2Regex,
    Task3Regex,
    Task4Regex,
    Task5Regex,
    Task6Regex,
    Task7Regex,
    Task8Regex,
    Task9Regex,
    Task10Regex,
    Task11Regex,
)
from python_zaawansowany.zadania.wielowatkowosc import Task1W


def main():
    while True:
        try:
            training = int(
                input("\nAby zakończyć wybierz 0 lub wprowadź numer szkolenia: ")
            )
            if training == 0:
                break
            task = int(input("Wprowadź numer zadania: "))
        except ValueError:
            print("Prosze nie psuć!")
            continue

        if training == 1:
            if task == 1:
                task1 = Task1Regex(training, task)
                task1.solution()
            elif task == 2:
                task2 = Task2Regex(training, task)
                task2.solution()
            elif task == 3:
                task3 = Task3Regex(training, task)
                task3.solution()
            elif task == 4:
                task4 = Task4Regex(training, task)
                task4.solution()
            elif task == 5:
                task5 = Task5Regex(training, task)
                task5.solution()
            elif task == 6:
                task6 = Task6Regex(training, task)
                task6.solution()
            elif task == 7:
                task7 = Task7Regex(training, task)
                task7.solution()
            elif task == 8:
                task8 = Task8Regex(training, task)
                task8.solution()
            elif task == 9:
                task9 = Task9Regex(training, task)
                task9.solution()
            elif task == 10:
                task10 = Task10Regex(training, task)
                task10.solution()
            elif task == 11:
                task11 = Task11Regex(training, task)
                task11.solution()
        elif training == 2:
            if task == 1:
                task1 = Task1Dek(training, task)
                task1.solution()
            elif task == 2:
                task2 = Task2Dek(training, task)
                task2.solution()
            elif task == 3:
                task3 = Task3Dek(training, task)
                task3.solution()
            elif task == 4:
                task4 = Task4Dek(training, task)
                task4.solution()
            elif task == 5:
                task5 = Task5Dek(training, task)
                task5.solution()
            elif task == 6:
                task6 = Task6Dek(training, task)
                task6.solution()
        elif training == 3:
            if task == 1:
                task1 = Task1PF(training, task)
                task1.solution()
            elif task == 2:
                task2 = Task2PF(training, task)
                task2.solution()
            elif task == 3:
                task3 = Task3PF(training, task)
                task3.solution()
            elif task == 4:
                task4 = Task4PF(training, task)
                task4.solution()
            elif task == 5:
                task5 = Task5PF(training, task)
                task5.solution()
            elif task == 6:
                task6 = Task6PF(training, task)
                task6.solution()
            elif task == 7:
                task7 = Task7PF(training, task)
                task7.solution()
            elif task == 8:
                task8 = Task8PF(training, task)
                task8.solution()
        elif training == 4:
            if task == 1:
                task1 = Task1GLS(training, task)
                task1.solution()
            elif task == 2:
                task2 = Task2GLS(training, task)
                task2.solution()
            elif task == 3:
                task3 = Task3GLS(training, task)
                task3.solution()
            elif task == 4:
                task4 = Task4GLS(training, task)
                task4.solution()
            elif task == 5:
                task5 = Task5GLS(training, task)
                task5.solution()
            elif task == 6:
                task6 = Task6GLS(training, task)
                task6.solution()
            elif task == 7:
                task7 = Task7GLS(training, task)
                task7.solution()
        elif training == 5:
            if task == 1:
                task1 = FileHandlerEX(training, task, "a", 12, 2000)
            elif task == 2:
                task2 = Task2EX(training, task)
                task2.solution()
        elif training == 6:
            if task == 1:
                task1 = Task1W(training, task)
                task1.solution()
        elif training == 5:
            if task == 1:
                task1 = FileHandlerEX(training, task, "a", 12, 2000)
            elif task == 2:
                task2 = Task2EX(training, task)
                task2.solution()


if __name__ == "__main__":
    main()
