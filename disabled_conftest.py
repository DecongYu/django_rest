# this is a special fixed-named file for using different database in testing 
# this setting is used only when pytest is used with the need of database.

import os

from django.conf import settings

import pytest


DEFAULT_ENGINE = "django.db.backends.postgesql_psycopg2"


# Fixtures are reusable objects for tests. They have a scope associated with them, 
# which indicates how often the fixture is invoked:
#       1. function - once per test function (default)
#       2. class - once per test class
#       3. module - once per test module
#       4. session - once per test session
@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
        "HOST": os.environ["DB_TEST_HOST"],
        "NAME": os.environ["DB_TEST_NAME"],
        "PORT": os.environ["DB_TEST_PORT"],
        "USER": os.environ["DB_TEST_USER"],
        "PASSWORD": os.environ["DB_TEST_PASSWORD"],
    }