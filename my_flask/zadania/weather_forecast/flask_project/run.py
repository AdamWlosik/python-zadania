from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5012)

# TODO
# Traceback (most recent call last):
#   File "C:\Users\adamw\OneDrive\Pulpit\Mentoring\python-zadania\python_zaawansowany\main.py", line 1, in <module>
#     from python_zaawansowany.zadania.dekoratory import (
# ModuleNotFoundError: No module named 'python_zaawansowany'
