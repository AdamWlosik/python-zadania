# FLASK

1. Tworzenie projektu
   - katalog główny projektu
        - ```mkdir flask_project```
   - katalog do HTML
        - ```mkdir flask_project\templates```
   - pliki statyczne (zdjęcia, kod CSS, pliki javascript)
        - ```mkdir flask_project\static```

2. Ręczne dodanie venv-a
      - ```cd flask_project```
   - dodanie środowiska wirtualnego
     - ```py -3 -m venv venv```
   - aktywacja środowiska wirtualnego
     - ```venv/Scripts/activate```
   - instalacja Flask
     - ```pip install Flask```

3. Kod py w katalogu głównym projektu flask_project\pliku.py

4. Uruchomienie aplikacji
   - ```python example.py```

5. Tworzenie obiektu reprezentującego aplikacje
   - ```APP = Flask(__name__)```

6. Określenie url aplikacji poprzez dekoratora
    ```
    @APP.route('/')
    def index():
    return 'Hello World!
   ```
   - ```@APP.route('/')```
     - wyświetli po wejściu do ścieżki głównej http://127.0.0.1:5000/
   - ```@APP.route('/home')```
     - wyświetli po wejściu do ścieżki home http://127.0.0.1:5000/home

7. Wywołanie aplikacji
    ```
    if __name__ == '__main__':
    APP.debug = True
    APP.run()
    ```
   - ```APP.debug = True```
     - automatyczne odświeżanie aplikacji po wprowadzeniu zmian
   - ```APP.run()```
     - uruchomienie aplikacji
-----------------------------------------------------------
Zaawansowana struktura projektu 

1. Tworzymy plik flask_project\__init__.py, który zawsze uruchamia się jako pierwszy
   ```
    from flask import Flask

    def create_app():
        app = Flask(__name__)
        app.debug = True

        from .main import index_blueprint
        app.register_blueprint(index_blueprint)

        return app
    ```
2. Tworzymy plik flask_project\main.py
    ```
   from flask import Blueprint

   index_blueprint = Blueprint('index', __name__)


   @index_blueprint.route('/')
   def index():
       return "Hello World!"
   ```
3. Uruchomienie aplikacji
   - Przechodzimy do katalogu nadrzędnego projektu flask_project
     - ```cd ..```
   - Komendy uruchamiające CMD
     - ```
       > set FLASK_DEBUG=1
       > set FLASK_APP=flask_project
       > flask run
       ```
   - Komendy uruchamiające PowerShell
     - ```
       > $env:FLASK_DEBUG=1
       > $env:FLASK_APP="flask_project"
       > flask run 
       ```
-----------------------------------------------------------------
Przekazanie parametru w adresie URL za pomocą <>
```
@user_blueprint.route('/<string:name>') 
def user_name(name):
    return f"Hello {name}!"
```
Url_for przyjmuje jako pierwszy argument nazwę funkcji, 
do której chcemy się odnieść oraz kolejne argumenty 
jako wartości parametrów funkcji. 
```
@admin_blueprint.route('/admin')
def admin():
    return redirect(url_for("user.user", name='Admin'))  
```
```
url_for("user.user", name='Admin') zwraca “/user/Admin”
url_for(“index.index”) zwraca “/”

```
meotda generująca kod html i przekazująca argumenty
```
@index_blueprint.route('/<string:name>')
def index(name):
    return render_template('index.html', welcome_text="Wassup", user_name=name)
```

------------------------------------------------------------------------------------
Nazwa metody:	Zastosowanie:
- GET	Pobieranie zasobu lub jego wyświetlanie, np. wyświetlenie szablonu strony. 
- POST	Przesyłanie danych zapisanych w postaci klucz-wartość do serwera. Kluczem jest nazwa danego pola, 
a wartością wpisana przez Nas wartość do danego pola. Metoda ta jest również wykorzystywana przy wysyłaniu plików na serwer. POST powoduje uruchomienie określonych operacji ustalonych przez serwer po przejściu na dany endpoint (URI).
- PUT	Służy do przesyłania paczki danych bez powiązania klucz-wartość. Wykorzystywana jest najczęściej przy RESTowych rozwiązaniach (tworzenie i update’owanie danych), gdzie ciałem danych jest formularz w postaci JSONa.
- DELETE	Usuwa zasoby na serwerze. Dlatego jest domyślnie wyłączona i uniemożliwia ingerencję w zasoby “z zewnątrz”.
- HEAD	 często jest wysyłany z tzw. “preflight requestami”. Służy on do sprawdzenia nagłówków zwracanego response z serwera, np. gdy potrzebujemy sprawdzić, jakiego rozmiaru będzie zwrócona odpowiedź bez pobierania jej ciała (przydatne, gdy nie chcemy danych o dużym rozmiarze).
