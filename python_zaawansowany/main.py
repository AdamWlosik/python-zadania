from python_zaawansowany.zadania.programowanie_funkcyjne import Task1PF, Task2PF, Task3PF, Task4PF, Task5PF, Task6PF, \
    Task7PF, Task8PF


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
            pass
        elif training == 2:
            pass
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


if __name__ == "__main__":
    main()
