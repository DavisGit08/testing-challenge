from src.exercise1_api.bookStore.api.bookstore_api import app
import json, pytest


# Client to be started.
@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

# Json to extract input data
data_file_path = 'tests\\api\\data\\booksData.json'
def new_book_json(book):
    with open(data_file_path, "r") as file:
        data = json.loads(file.read())
        new_book = data[book]
        file.close()
        return new_book

# Validate response headers
def resp_headers_validation(response):
    assert 'Content-Type' in response.headers
    assert response.headers['Content-Type'] == 'application/json'