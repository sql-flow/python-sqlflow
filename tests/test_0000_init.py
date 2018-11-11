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
    cr = db.cursor()
    with pytest.raises(SqlFlowException):
        wkf = WorkFlow(cursor=cr, schema='fakeflow')
        wkf._schema_exists()
    cr.close()

def test_connection_schema(db):
    """Test with schema is available on DB"""
    cr = db.cursor()
    wkf = WorkFlow(cursor=cr)
    wkf._schema_exists()
    cr.close()

def test_missing_workflow(db):
    """Test if workflow is available on DB"""
    wkf = WorkFlow(cursor=db.cursor())
    with pytest.raises(SqlFlowException):
        wkf._check_workflow('first-workflow')

def test_add_workflow(db):
    """Test adding a workflow"""
    wkf = WorkFlow(cursor=db.cursor())
    res = wkf.add_workflow('aaaa', 'Workflow A', '')
    wkf._check_workflow('aaaa')
    assert res[0] > 0
    assert res[1] == 'aaaa'

def test_duplicate_workflow(db):
    """Test adding a workflow"""
    cr = db.cursor()
    cr.execute("BEGIN;")
    wkf = WorkFlow(cursor=cr)
    wkf._check_workflow('aaaa')
    with pytest.raises(SqlFlowException):
        wkf.add_workflow('aaaa', 'Workflow A', '')
    db.rollback()
    cr.close()

def test_unname_workflow(db):
    """Test adding uname workflow"""
    cr = db.cursor()
    cr.execute("BEGIN;")
    wkf = WorkFlow(cursor=db.cursor())
    res = wkf.add_workflow(None, 'Workflow unknown', '')
    assert res[0] > 0
    assert len(res[1]) == 36
    db.rollback()
    cr.close()
