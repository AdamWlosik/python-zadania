from python_zaawansowany.zadania.dekoratory import Task1Dek


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


if __name__ == "__main__":
    main()
