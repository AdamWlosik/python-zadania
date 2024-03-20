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

-----------------------------------------------------------------------
```
<form action="#" method="POST">
        <p>Your name: <input type="text" name="nickname" /></p>
        <p><input type="submit" value="submit" /></p>
    </form>
```
- action=”#” określa, dokąd ma zostać przeniesiony użytkownik, gdy zatwierdzi swój wybór klawiszem submit. # mówi, iż ma on zostać przekierowany na tę samą stronę, z którego dokonał wyboru (i właśnie z jej poziomu mają być podejmowane dalsze kroki, co ma się zadziać co do działania aplikacji)
- method=”POST” określa, jak mają zostać wysłane dane z formularza do serwera
- parametr name w znaczniku ```<input type=”text”>``` określa, z jakim kluczem ma być kojarzona wysyłana wartość z poziomu formularza; określenie takiego klucza jest niezbędne w celu obsługiwania odpowiednich danych z formularza z poziomu logiki programu (plik main.py).

- flashowanie wiadomości 
1. python:
   - ```flash("text")```
2. HTML
  - pobranie wszystkich sflashowanych wiadomości
    - ```{% with messages = get_flashed_messages() %}```
  - przechodzenie po każdej pojedyńczej wiadomości
    - ```{% for msg in messages %}```
  - wyświetlanie
    -  ```<p>{{ msg }}</p>```
-------------------------------------------------------------------
1. Połączenie z bazą danych (SQLAlchemy) (main.py)
```
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
    db = SQLAlchemy(app)
```

2. Utworzenie tabeli (main.py)
```
class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name, self.email = name, email
```
3. Relacje między tabelami (main.py)
```
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://nazwa_bazy.sqlite3'
db = SQLAlchemy(app)

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    children = relationship("Child")

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, ForeignKey('parent.id'))

```
4. Dodanie tabeli do bazy danych przy pomocy konsoli 
    - przechodzimy do katalogu nadrzędnego projektu
    - utuchamiamy interpreter poleceniem ```python```
    - wpisujemy w konsoli 
      - ```
        from project import db
        db.create_all() 
        ```
      # TODO nie działa 

5. Przykładowe operacje:
    - dodanie rekordów (insert into:
    ```
        from main import db
        for i in range(10):
            new_user = Users(f'Jan {i}', f'jan_{i}@devs-mentoring.pl')
            db.session.add(new_user) # dodanie rekordu

        db.session.commit() # zatwierdzenie zmian
    ```
    - wybór rekordów (select):
    ```
    from main import db
    found_user = Users.query.filter_by(name='Jan 1').first() 
    print(found_user.email) # prints jan_1@devs-mentoring.pl
    ```
   ```
   from main import db
   for user in Users.query.order_by(Users.name):
   print(user.name, user.email) # prints users in ascending order by their names
   ```
   ```
    from main import db
    found_user = Users.query.get(1) # gets user by primary_key (id)
    print(found_user.email) # prints jan_1@devs-mentoring.pl
    ```
   - usuwanie rekordów (delete from)
   ```
    from main import db
    Users.query.filter_by(name='Jan 2').delete()
    db.session.commit()
    ```
   - aktualizacja (update)
   ```
    from main import db
    found_user = Users.query.filter_by(name='Jan 2').first()
    found_user.email = 'new_email@gmail.com'
    db.session.commit()
    ```
----------------------------------------------------------------------
1. integorwanie bazy danych (__init__)
    - meotda integrująca ```init_app()```
-------------------------------------------------
STRUKTURA PROJEKTU
- folder_główny_projektu
  - flask_project
    - run.py
    - app
      - constans.py
      - mian.py
      - models.py
      - my_database.db
      - __init__py
      - static
        - base.css
      - templates
        - base.html
        - dashboard.html
        - index.html

run.py
```
def create_db(app):
    with app.app_context():
        if not os.path.exists(DB_PATH):
            db.create_all()
```