from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Movies

add_movie_blueprint = Blueprint("add_movie", __name__)
show_movies_blueprint = Blueprint("show_movies", __name__)
home_page_blueprint = Blueprint("home_page", __name__)
summary_blueprint = Blueprint("summary", __name__)


@home_page_blueprint.route("/")
def home_page():
    return render_template("home_page.html")


@add_movie_blueprint.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    """Metoda dodająca filmy i opinie o nich do bazy dancyh"""
    if request.method == "POST":
        title = request.form.get("title")
        opinion = request.form.get("opinion")
        if title:
            new_movie = Movies(title=title, opinion=opinion)
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for("show_movies.show_movies"))
        else:
            error_message = "Please provide a title for the movie."
            return render_template("add_movie.html", error_message=error_message)
    return render_template("add_movie.html")


@show_movies_blueprint.route("/show_movies", methods=["POST"])
def show_movies():
    """Metoda wyświetlająca filmy z bazy danych"""
    movies = Movies.query.all()
    return render_template("show_movies.html", movies=movies)


@summary_blueprint.route("/summary", methods=["POST"])
def summary():
    """Metoda wyświetlająca tytuły i opinie o filamch"""
    movies = Movies.query.all()
    return render_template("summary.html", movies=movies)
