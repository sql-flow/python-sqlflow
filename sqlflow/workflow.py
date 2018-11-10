# See LICENSE file at root repository

import psycopg2
from .exceptions import SqlFlowException


class WorkFlow:

    def __init__(self, cursor=None, name=None, schema='sqlflow'):
        """
        Initialise a workflow instance
        :param cursor: Database cursor
        """
        self.db_schema = schema

        if cursor is None:
            raise SqlFlowException('Database cursor is missing!')
        print(cursor)

        if name is None:
            name = 'SqlFlow'

        self.cr = cursor
        self._schema_exists()


    def _schema_exists(self):
        """
        Check if defined schema is available on database
        """
        query = """SELECT count(*) as value
                     FROM information_schema.schemata
                    WHERE schema_name=%s"""
        self.cr.execute(query, (self.db_schema,))
        val = self.cr.fetchone()
        if val[0] == 0:
            raise SqlFlowException(
                'Schema "%s" not found in the database!' % (self.db_schema,)
            )

    def _check_workflow(self, name=None):
        """
        Check if workflow exists in the database
        """
        query = """SELECT id, title FROM sqlflow.workflow WHERE uref=%s"""
        self.cr.execute(query, (name,))
        res = self.cr.fetchone()
        if not res:
            raise SqlFlowException(
                'Workflow "%s" not found in the database!' % (name,)
            )
        return (res[0], res[1])


class Version:
    pass


class Activity:
    pass


class Transition:
    pass


class Task:
    pass


class Condition:
    pass
