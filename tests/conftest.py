import os
import pytest
from psycopg2 import connect
from psycopg2 import DatabaseError


@pytest.fixture(scope="session")
def db():
    d = connect(
        database=os.environ.get('TEST_DB', 'myflow'),
        user=os.environ.get('TEST_USER', 'myflow'),
        password=os.environ.get('TEST_PASS', 'myflow'),
        host=os.environ.get('TEST_HOST', '127.0.0.1'),
        port=int(os.environ.get('TEST_PORT', '5432')),
        application_name='SQLFlow'
    )
    d.reset()
    return d
