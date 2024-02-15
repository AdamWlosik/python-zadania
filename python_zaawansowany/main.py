from python_zaawansowany.zadania.regex import Task1Regex, Task2Regex, Task3Regex, Task4Regex, Task5Regex, Task6Regex, \
    Task7Regex, Task8Regex, Task9Regex, Task10Regex, Task11Regex


def main():
    while True:
        try:
            training = int(input("\nAby zakończyć wybierz 0 lub wprowadź numer szkolenia: "))
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


if __name__ == "__main__":
    main()
