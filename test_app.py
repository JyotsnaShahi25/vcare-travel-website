import unittest
import os
from .fetch_data import connect_to_iql,connect_to_postgres,connect_to_mysql
from dotenv import load_dotenv
from flask import current_app


load_dotenv()

class TestCase(unittest.TestCase):
    def test_client():
        app = current_app()
        # Flask provides a way to test your application by exposing the Werkzeug test Client
        # and handling the context locals for you.
        testing_client = app.test_client()

        # Establish an application context before running the tests.
        ctx = app.app_context()
        ctx.push()

        yield testing_client  # this is where the testing happens!

        ctx.pop()

    def test_connect_to_iql(self):
        query = "FROM jobsearch 2d 1d SELECT COUNT()"
        df = connect_to_iql(query)
        len_df = len(df)
        self.assertEqual(len_df, 1)

    def test_connect_to_postgres(self):
        query = 'select * from bi.acq_dim_session limit 5'
        df = connect_to_postgres(query)
        len_df = len(df)
        self.assertEqual(len_df,5)

    def test_connect_to_mysql(self):
        query = 'select * from adcentraldb.tblACLauditchanges limit 5'
        df = connect_to_mysql('dbslave-adcentral.ausoff.indeed.net',3309,'adcentraldb',query)
        len_df = len(df)
        self.assertEqual(len_df,5)

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()