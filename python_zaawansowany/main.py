def main():
    while True:
        try:
            szkolenie = int(input("\nAby zakończyć wybierz 0 lub wprowadź numer szkolenia: "))
            if szkolenie == 0:
                break
            zadanie = int(input("Wprowadź numer zadania: "))
        except ValueError:
            print("Prosze nie psuć!")
            continue

        if szkolenie == 1:
            if zadanie == 1:
                pass


if __name__ == "__main__":
    main()
