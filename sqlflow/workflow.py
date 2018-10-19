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
            name = 'SqlFlow '

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
