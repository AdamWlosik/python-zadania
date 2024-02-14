from python_zaawansowany.zadania.regex import Task1Regex, Task2Regex, Task3Regex, Task4Regex, Task5Regex


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
                task1.rozwiazanie()
            elif task == 2:
                task2 = Task2Regex(training, task)
                task2.rozwiazanie()
            elif task == 3:
                task3 = Task3Regex(training, task)
                task3.rozwiazanie()
            elif task == 4:
                task4 = Task4Regex(training, task)
                task4.rozwiazanie()
            elif task == 5:
                taks5 = Task5Regex(training, task)
                taks5.rozwiazanie()


if __name__ == "__main__":
    main()