from python_zaawansowany.zadania.dekoratory import Task1Dek, Task2Dek, Task3Dek, Task4Dek, Task5Dek, Task6Dek


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


if __name__ == "__main__":
    main()
