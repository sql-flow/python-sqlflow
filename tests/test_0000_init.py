from psycopg2 import connect
from psycopg2 import DatabaseError
from sqlflow.workflow import WorkFlow
from sqlflow.exceptions import SqlFlowException
import pytest
import os


def test_no_connection():
    """Call workflow with no connection"""

    with pytest.raises(SqlFlowException):
        WorkFlow()

def test_connection_fake_schema(db):
    """Test with schema is available on DB"""
    with pytest.raises(SqlFlowException):
        wkf = WorkFlow(cursor=db.cursor(), schema='fakeflow')
        wkf._schema_exists()

def test_connection_schema(db):
    """Test with schema is available on DB"""
    wkf = WorkFlow(cursor=db.cursor())
    wkf._schema_exists()
