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
            pass
        elif training == 4:
            if task == 1:
                pass


if __name__ == "__main__":
    main()
