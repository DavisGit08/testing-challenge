# #####################

Table of contents:
    · Welcome
    · Original project modifications
    · Project structure
    · List of Test Cases
    · How to run tests


# ########################################### Welcome #########################################################

Welcome to the test challenge created by David Pérez.
Below you will find a detailed guide to help you understand and navigate the project effectively.


# ############################# Original project modifications ################################################

Some modifications were done in the original project:
    · 'Exercise1-API.py' file renamed to 'exercise1_api.py' to follow naming conventions.
    · 'Exercise2-UI.py' file renamed to 'exercise2_ui.py' to follow naming conventions.
    · 'exercise1_api.py' and 'exercise2_ui.py' moved to src folder.
    · Test Support new method added to 'bookstore_api.py' file in order to remove all existing books.


# ##################################### Project structure #####################################################

These are the most important elements (not all of them) inside Project Structure:

TESTING-CHALLENGE/
    |
    |--> .venv/                           # Virtual environment directory.                                     
    |--> src/                       	  # Tests source.
    |   |--> exercise1_api/               # Test folder with API sources.
    |   |--> exercise2_ui/                # Test folder with UI sources (only README.md file).
    |--> tests/                           # Directory containing all Test Cases.
    |   |--> api/                         # API related Test Cases.
    |   |   |--> data/                    # Input data needed for API tests runtime.
    |   |   |--> utils/                   # Utility functions for API tests.
    |   |   |--> test_api.py              # Test Cases for API.
    |   |   |--> test_smokeTests_API.py   # API Smoke Tests. NOT added to the pipeline.
    |   |--> ui/                          # UI related Test Cases.
    |   |   |--> pages/                   # Page object models.
    |   |       |--> page_debugbear.py    # Page objects layer. It encapsulates page objects and actions.
    |   |       |--> page_behavior.py     # Page behavior layer where logic can be encapsulated. Not being used :)
    |   |   |--> utils/                   # Utility functions for UI tests.
    |   |   |--> test_ui.py               # UI Test cases.
    |   |--> README.md                    # Test Challenge documentation by David Pérez.
    |--> pyproject.toml                   # Poetry configuration file.
    |--> README.md                        # Project documentation.


# ##################################### List of Test Cases #####################################################

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
    · Test with empty url value and "Desktop" device.
    · Test with "." url value and "Desktop" device.
    · Test with invalid url value and "Desktop" device.
    · Test with empty url value and "Mobile" device.
    · Test with "." url value and "Mobile" device.
    · Test with invalid url value and "Mobile" device.
    · Basic test to load main page and validate elements in the main page.
    · Test with idoven url without "http://" and "Desktop" device to check if it's being resolved.
    · Test with valid url and validate testing in process page for "MobDesktopile".
    · Test with valid url and test results for "Desktop".
    · Test with idoven url without "http://" and "Mobile" device to check if it's being resolved.
    · Test with valid url and validate testing in process page for "Mobile".
    · Test with valid url and test results for "Mobile".

    * There are much more Test Cases to be done, but it's not implemented cause it consumes a lot of time. i.e:
        · Once Start Test button is clicked over, it starts testing website:
            · Test Case to validate bar in progress is progressing.
            · Test Case to validate Main Message 'Waiting In Queue' is updating to new statuses.
        · Once Start Test with a valid url is completed, it showes the results panel. Taking a look at the left panel options we could validate every section and create Test Cases for:
            · Web vitals section
            · Requests section
            · Metrics section
            · Lighthouse section
            · RUM section
            · Experiments section
        · Once Start Test process is started many times with valid urls, it throws the error: "You've been rate limited. Wait some time before making more requests.". it would be a new rainy path to be added. 
        · In order to avoid previous error, It could be solved implementing a proxy function. If not, tests could fail.
        · Test Case to stop service while testing url is in progress, in order to check errors.


# ###################################### How to run tests ######################################################

API Test suite:
    · Open a new terminal and type: pytest -vv .\tests\api\test_api.py
API Smoke Tests suite:
    · Open a new terminal and type: pytest -vv .\tests\api\test_smokeTests_api.py

UI Test Suite:
    · Open a new terminal and type: pytest -vv .\tests\ui\test_ui.py
