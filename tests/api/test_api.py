from src.exercise1_API.bookStore.api.bookstore_api import app
from tests.api.utils.utils import new_book_json, resp_headers_validation
import pytest


# Client to be started.
@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·# RAINY PATHS #·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#

# WorkFlow: Remove non existing book by ID.
def test_rainy_remove_no_id(client): 

    # Remove all books with TestSupport endpoint
    client.delete('/books')

    # Remove non existing book
    response = client.delete('/books/999')
    assert response.status_code == 404
    resp_headers_validation(response)


# WorkFlow: Remove a book that previously existed
def test_rainy_remove_no_book_existed_before(client):

    # Data
    new_book = new_book_json('book1')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Remove book
    response = client.delete('/books/'+bookId)
    assert response.status_code == 204
    resp_headers_validation(response)

    # Get books list empty
    response = client.get('/books')
    assert response.status_code == 200
    assert response.get_json() == []
    resp_headers_validation(response)

    # Remove book
    response = client.delete('/books/'+bookId)
    assert response.status_code == 404
    assert 'Book not found' in str(response.get_json())
    resp_headers_validation(response)


# WorkFlow: Get non existing book by ID.
def test_rainy_get_no_id(client): 

    # Remove all books with TestSupport endpoint
    client.delete('/books')

    # Get book by ID
    response = client.get('/books/1')
    assert response.status_code == 404
    resp_headers_validation(response)


# WorkFlow: Get non existing book by ID that previously existed.
def test_rainy_get_no_book_existed_before(client): 

    # Data
    new_book = new_book_json('book1')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Remove book
    response = client.delete('/books/'+bookId)
    assert response.status_code == 204
    resp_headers_validation(response)

    # Get book by ID
    response = client.get('/books/'+bookId)
    assert response.status_code == 404
    resp_headers_validation(response)


# WorkFlow: Create a new book missing title.
def test_rainy_create_missing_title(client): 
    
    # Data
    new_book = new_book_json('missingTitle')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 400
    assert response.get_json().get('error') == 'Missing required fields'
    resp_headers_validation(response)


# WorkFlow: Create a new book missing author.
def test_rainy_create_missing_author(client): 

    # Data
    new_book = new_book_json('missingAuthor')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 400
    assert response.get_json().get('error') == 'Missing required fields'
    resp_headers_validation(response)


# WorkFlow: Create a new book missing publish date.
def test_rainy_create_missing_publish_date(client): 

    # Data
    new_book = new_book_json('missingPublishDate')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 400
    assert response.get_json().get('error') == 'Missing required fields'
    resp_headers_validation(response)


# WorkFlow: Create a new book missing isbn.
def test_rainy_create_missing_isbn(client): 

    # Data
    new_book = new_book_json('missingIsbn')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 400
    assert response.get_json().get('error') == 'Missing required fields'
    resp_headers_validation(response)


# WorkFlow: Create a new book missing price.
def test_rainy_create_missing_price(client): 

    # Data
    new_book = new_book_json('missingPrice')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 400
    assert response.get_json().get('error') == 'Missing required fields'
    resp_headers_validation(response)


# WorkFlow: Update a non existing book.
def test_rainy_update_non_existing_book(client): 

    # Data
    modif_book = new_book_json('bookModif')

    # Update a new book
    response = client.put('/books/999', json=modif_book)
    assert response.status_code == 404
    resp_headers_validation(response)


# WorkFlow: Update a non existing book.
def test_rainy_update_no_book_existed_before(client): 

    # Data
    new_book = new_book_json('book1')
    modif_book = new_book_json('bookModif')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Remove book
    response = client.delete('/books/'+bookId)
    assert response.status_code == 204
    resp_headers_validation(response)

    # Update a new book
    response = client.put('/books/'+bookId, json=modif_book)
    assert response.status_code == 404
    resp_headers_validation(response)


#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·# HAPPY PATHS #·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#

# WorkFlow: Retrieve empty books list.
def test_happy_empty_books(client):

    # Remove all books with TestSupport endpoint
    response = client.delete('/books')

    # Get books list empty
    response = client.get('/books')
    assert response.status_code == 200
    assert response.get_json() == []
    resp_headers_validation(response)


# WorkFlow: Retrieve list with several books.
def test_happy_get_several_books(client):

    # Remove all books with TestSupport endpoint
    response = client.delete('/books')

    # Data
    new_book = new_book_json('book1')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    resp_headers_validation(response)

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    resp_headers_validation(response)

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    resp_headers_validation(response)

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    resp_headers_validation(response)

    # Get books list empty
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.get_json()) == 4
    resp_headers_validation(response)


# WorkFlow: Create a new book.
def test_happy_create_book(client):

    # Remove all books with TestSupport endpoint
    response = client.delete('/books')

    # Data
    new_book = new_book_json('book1')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Get book
    response = client.get('/books/'+bookId)
    assert response.status_code == 200
    assert response.get_json()['book_id'] == bookId
    assert response.get_json()['title'] == new_book['title']
    assert response.get_json()['author'] == new_book['author']
    assert response.get_json()['published_date'] == new_book['published_date']
    assert response.get_json()['isbn'] == new_book['isbn']
    assert response.get_json()['price'] == new_book['price']
    resp_headers_validation(response)


# WorkFlow: Create several books and retrieve the whole and very varied boundary info.
def test_happy_get_several_books_boundary_info(client):

    # Remove all books with TestSupport endpoint
    response = client.delete('/books')

    # Data
    new_books = [
        new_book_json('boundary1'),
        new_book_json('boundary1.1'),
        new_book_json('boundary2'),
        new_book_json('boundary2.2'), 
        new_book_json('boundary3'),
        new_book_json('boundary3.3'),
        new_book_json('boundary4'),
        new_book_json('boundary4.4')
    ]

    # Create books and store their IDs
    book_ids = []
    for new_book in new_books:
        response = client.post('/books', json=new_book)
        assert response.status_code == 201
        resp_headers_validation(response)
        book_ids.append(response.get_json()['book_id'])

    # Get and validate each book
    for book_id, new_book in zip(book_ids, new_books):
        response = client.get('/books/' + book_id)
        assert response.status_code == 200
        assert response.get_json()['book_id'] == book_id
        assert response.get_json()['title'] == new_book['title']
        assert response.get_json()['author'] == new_book['author']
        assert response.get_json()['published_date'] == new_book['published_date']
        assert response.get_json()['isbn'] == new_book['isbn']
        assert response.get_json()['price'] == new_book['price']
        resp_headers_validation(response)


# WorkFlow: Create a new book and retrieve list.
def test_happy_create_book_and_get_list(client):   

    # Remove all books with TestSupport endpoint
    client.delete('/books')
    
    # Data
    new_book = new_book_json('book1')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    resp_headers_validation(response)

    # Get books list
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.get_json()) == 1
    resp_headers_validation(response)
    

# WorkFlow: Create a new book and retrieve book by ID.
def test_happy_create_book_and_get_id(client): 

    # Data
    new_book = new_book_json('book1')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Get book by ID
    response = client.get('/books/'+bookId)
    assert response.status_code == 200
    assert response.get_json()['book_id'] == bookId
    resp_headers_validation(response)


# WorkFlow: Update a book.
def test_happy_update_book(client): 

    # Data
    new_book = new_book_json('book1')
    modif_book = new_book_json('bookModif')

    # Create a new book
    response = client.post('/books', json=new_book)
    assert response.status_code == 201
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Update a new book
    response = client.put('/books/'+bookId, json=modif_book)
    assert response.status_code == 200
    bookId = response.get_json()['book_id']
    resp_headers_validation(response)

    # Get book
    response = client.get('/books/'+bookId)
    assert response.status_code == 200
    assert response.get_json()['title'] == modif_book['title']
    assert response.get_json()['author'] == modif_book['author']
    assert response.get_json()['published_date'] == modif_book['published_date']
    assert response.get_json()['isbn'] == modif_book['isbn']
    assert response.get_json()['price'] == modif_book['price']
    resp_headers_validation(response)

