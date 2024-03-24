# LISTY SKŁADANE
1. Zasada tworzenia list składanych
   - [wyrazenie for element in elements]
   - [wyrazenie for element in elements if warunek]
- Obliczanie n kolejnych kwadratów liczb
    ```
    N = 10
    lista_kwadratow_liczb = [i**2 for i in range(10)]
    print(lista_kwadratow_liczb) -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```
- Co drugi znak z dowolnego zdania 
   ```
   txt = "Przykladowy tekst"
   filtered_list = [txt[i] for i in range(0, len(txt), 2)]
   print(filtered_list) -> ['P', 'z', 'k', 'a', 'o', 'y', 't', 'k', 't']
   ```
- Kwadrat liczb parzystych
    ```
    squares_even2 = [i**2 for i in range(10) if i % 2 == 0]
    print(squares_even2) -> [0, 4, 16, 36, 64]
    ```
- Wyciąganie za zdania dozwolonych wyrazów
```
allowed_words = ["w", "pod", "i", "nad", "o"]
txt = "Ala i Staś trzymają koty w piwnicy pod kuchnią o świcie"
found_allowed_words = [word for word in txt.split() if word in allowed_words]
print(found_allowed_words) -> ['i', 'w', 'pod', 'o']
``` 
- Uproszczenie macierzy dwuelementowej do listy
```
multi_matrix = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
flatten = [x for sublist in multi_matrix
           for subsublist in sublist
           for x in subsublist]
print(flatten) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```