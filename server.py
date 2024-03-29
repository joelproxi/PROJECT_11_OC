from datetime import datetime
import json
from pathlib import Path

from flask import Flask, render_template, request, redirect, flash, url_for

BASE_DIR = Path(__file__).resolve().parent


def load_lubs():
    with open(BASE_DIR / 'clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open(BASE_DIR / 'competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


def create_app(config=None):
    app = Flask(__name__)
    app.secret_key = "something_special"

    competitions = load_competitions()
    clubs = load_lubs()

    @app.route('/')
    def index():
        return render_template('index.html', clubs=clubs)

    @app.route('/showSummary', methods=['POST'])
    def show_summary():
        try:
            club = [club for club in clubs if club['email']
                    == request.form['email']][0]
            return render_template(
                'welcome.html',
                club=club,
                competitions=competitions)
        except IndexError:
            flash("Sorry, that email wasn't found.")
            return render_template('index.html'), 401

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        found_club = [c for c in clubs if c['name'] == club][0]
        found_competition = [
            c for c in competitions if c['name'] == competition][0]
        date = datetime.now()
        date_str = date.strftime("%Y-%m-%d %H:%M:%S")
        print(date_str)
        date_competition = found_competition['date']
        print(date_competition)
        print(competitions)
        if date_str < date_competition:
            if found_club and found_competition:
                return render_template('booking.html',
                                       club=found_club,
                                       competition=found_competition)
            else:
                print('else')
                flash("Something went wrong-please try again")
                return render_template('welcome.html',
                                       club=club,
                                       competitions=competitions)
        else:
            flash("Cette compétition n'est plus valide")
            return render_template('welcome.html',
                                   club=club,
                                   competitions=competitions)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchase_places():
        competition = [c for c in competitions if c['name']
                       == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        places_required = int(request.form['places'])
        places_available = int(competition['numberOfPlaces'])
        club_points = int(club['points'])
        while True:
            try:
                places_required = int(request.form['places'])
            except ValueError:
                flash("You can only enter number")
                break
            if places_required <= 0:
                raise ValueError(
                    "Then number of places must be greather than 0")
                flash("Then number of places must be greather than 0")
                break
            if places_required > club_points:
                flash("You can't have much places than ...")
                break
            if places_required > places_available:
                flash("You can't have much places than available")
                break
            if places_required > 12:
                flash("You can't have much than 12 places")
                break
            if places_required <= places_available:
                competition['numberOfPlaces'] = int(
                    competition['numberOfPlaces'])-places_required
                club_points = club_points - places_required
                club['points'] = str(club_points)
                flash('Great-booking complete!')
                return render_template('welcome.html',
                                       club=club,
                                       competitions=competitions)
        return render_template('welcome.html',
                               club=club,
                               competitions=competitions)

    # TODO: Add route for points display

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    if config is None:
        app.run(debug=True)
    if config is True:
        return app


if __name__ == "__main__":
    create_app()
