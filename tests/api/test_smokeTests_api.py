from src.exercise1_API.bookStore.api.bookstore_api import app
import pytest

# Client to be started.
@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·# SMOKE TESTS #·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#

# WorkFlow: Test POST endpoint.
def test_smoke_tests_post(client): 

    # Create a new book
    new_book = {"title": "book 1","author": "David the writter","published_date": "25/05/2024","isbn": "4-12-105554-0","price": "6 €"}
    response = client.post('/books', json=new_book)
    assert response.status_code == 201

# WorkFlow: Test PUT endpoint.
def test_smoke_tests_put(client): 

    # Udate a book.
    new_book = {"title": "book 1 modified","author": "David the writter","published_date": "25/05/2024","isbn": "4-12-105554-0","price": "6 €"}
    response = client.put('/books/1', json=new_book)
    assert response.status_code == 200


# WorkFlow: Test GET endpoint.
def test_smoke_tests_get(client): 

    # Get books list empty
    response = client.get('/books')
    assert response.status_code == 200


# WorkFlow: Test REMOVE endpoint.
def test_smoke_tests_remove(client): 

    # Remove book
    response = client.delete('/books/1')
    assert response.status_code == 204