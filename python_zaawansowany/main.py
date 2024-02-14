from python_zaawansowany.zadania.regex import Task1Regex


def main():
    while True:
        try:
            traning = int(input("\nAby zakończyć wybierz 0 lub wprowadź numer szkolenia: "))
            if traning == 0:
                break
            task = int(input("Wprowadź numer zadania: "))
        except ValueError:
            print("Prosze nie psuć!")
            continue

        if traning == 1:
            if task == 1:
                task1 = Task1Regex(traning, task)
                task1.rozwiazanie()


if __name__ == "__main__":
    main()
