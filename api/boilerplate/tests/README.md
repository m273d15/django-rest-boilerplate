## Django python testing
### Run tests
First start the api container with valid environment variables as described in the main README. Then execute `docker-compose exec api sh -c "python manage.py test"`

### Write a new test module
In order to add a test module `my_module`, please add the file into the `tests` directory and add the import `from boilerplate.tests.my_module import *` to the file `__init__.py`.

### Testrunner configuration
In order to avoid that the test runner starts to create a new database which we do not need, a custom testrunner is created as described [here](https://stackoverflow.com/questions/5917587/django-unit-tests-without-a-db).
