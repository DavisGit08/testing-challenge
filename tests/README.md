# Welcome to the test challenge created by David Pérez. Please find everything you need to know below:

Table of contents:
    · Project structure
    · List of Test Cases
    · How to run tests


# ####################################### Project structure #######################################################

Under "tests" folder you can find the following:

api folder: Everything related to API tests can be found in this folder.
    · __init__.py: File necessary to run pytests.
    · data folder: Data needed for tests.
    · utils folder: Utilities to be used by tests.
    · test_API.py: All API tests.
    · test_smokeTests_API.py: API smoke tests.

ui folder: Everything related to API tests can be found in this folder.
    · __init__.py: File necessary to run pytests.



+Other modifications done through the project:
    · 'Exercise1-API.py' file renamed to 'exercise1_API.py'.
    · 'Exercise2-UI.py' file renamed to 'exercise2_UI.py'.
    · 'exercise1_API.py' and 'exercise2_UI.py' moved to src folder.
    · Test Support new method added to 'bookstore_api.py' file in order to remove all existing books.


# ####################################### List of Test Cases #######################################################

List of API Test Cases (rainy paths + happy paths):
    · Remove non existing book by ID.
    · Remove a book that previously existed.
    · Get non existing book by ID.
    · Get non existing book by ID that previously existed.
    · Create a new book missing title.
    · Create a new book missing author.
    · Create a new book missing publish date.
    · Create a new book missing isbn.
    · Create a new book missing price.
    · Update a non existing book.
    · Update a non existing book that previously existed.
    · Retrieve empty books list.
    · Retrieve list with several books.
    · Create and get a new book.
    · Create several books and retrieve the whole and very varied boundary info.
    · Create a new book and retrieve list.
    · Create a new book and retrieve book by ID.
    · Update a book.
    · Test POST endpoint. (Smoke Test)
    · Test PUT endpoint. (Smoke Test)
    · Test GET endpoint. (Smoke Test)
    · Test REMOVE endpoint. (Smoke Test)

List of UI Test Cases (rainy paths + happy paths):
    ·
    ·
    ·
    ·
    ·
    ·
    ·
    ·
    ·


# ####################################### How to run tests #######################################################

Open a new terminal and type: pytest -vv
