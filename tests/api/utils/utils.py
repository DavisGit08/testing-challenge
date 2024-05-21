import json

# Json to extract input data
data_file_path = 'tests\\api\\data\\booksToCreate.json'
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