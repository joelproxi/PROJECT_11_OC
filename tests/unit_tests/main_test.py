import pytest

from server import create_app


@pytest.fixture()
def test_client():
    flask_app = create_app(config=True)
    yield flask_app.test_client()


@pytest.fixture()
def points_text():
    data = {
        "available_points": "Points available: 69",
        "number_of_places": "Number of Places: 34",
    }
    return data


@pytest.fixture()
def db_data():
    data = {
        "club": "Simply Lift",
        "competition": "Spring Festival",
        "email": "john@simplylift.co",
    }
    return data


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200


def test_showSummary_with_correct_email(test_client, db_data):
    competition_name = db_data["competition"]
    email = db_data["email"]
    response = test_client.post(
        "/showSummary", data={"email": email})

    assert response.status_code == 200
    assert f"Welcome, {email}" in response.data.decode()
    assert competition_name in response.data.decode()


def test_showSummary_with_unknow_email(test_client):
    email = "wrong@test.com"
    response = test_client.post("/showSummary", data={"email": email})

    assert response.status_code == 401


def test_purchasePlaces_happy_path(test_client, db_data):
    club_name = db_data["club"]
    competition_name = db_data["competition"]
    requiredPlaces = 5
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 200


def test_purchasePlaces_required_places_isnt_int(
    test_client, points_text, db_data
):
    club_name = db_data["club"]
    competition_name = db_data["competition"]
    requiredPlaces = ""
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 500
    with pytest.raises(ValueError):
        int(requiredPlaces)


def test_purchasePlaces_required_places_is_less_than_zero(
    test_client, points_text, db_data
):

    club_name = db_data["club"]
    competition_name = db_data["competition"]
    requiredPlaces = -1
    response = test_client.post(
        "/purchasePlaces",
        data={
            "club": club_name,
            "competition": competition_name,
            "places": requiredPlaces,
        },
    )
    assert response.status_code == 500
