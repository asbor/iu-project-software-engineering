import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import time


class TestDatabaseConnection(unittest.TestCase):

    @patch.dict(os.environ, {
        "DATABASE_USER": "test_user",
        "DATABASE_PASSWORD": "test_password",
        "DATABASE_HOST": "test_host",
        "DATABASE_PORT": "5432",
        "DATABASE_NAME": "test_db"
    })
    def test_database_connection(self):
        from app.model.database import create_engine, SQLALCHEMY_DATABASE_URL

        # Mocking create_database and database_exists functions
        create_database_mock = MagicMock()
        database_exists_mock = MagicMock()

        with patch('your_module.create_database', create_database_mock), \
                patch('your_module.database_exists', database_exists_mock):

            # Set return values for database_exists_mock
            database_exists_mock.return_value = False

            # Call the function to be tested
            create_engine(SQLALCHEMY_DATABASE_URL)

            # Assert that create_database was called with the correct arguments
            create_database_mock.assert_called_once_with(
                SQLALCHEMY_DATABASE_URL)

            # Assert that database_exists was called with the correct arguments
            database_exists_mock.assert_called_once_with(
                SQLALCHEMY_DATABASE_URL)

            # Assert that create_engine was called with the correct arguments
            self.assertTrue(create_engine.called)

    @patch.dict(os.environ, {})
    def test_missing_environment_variables(self):
        from app.model.database import create_engine

        with self.assertRaises(KeyError):
            create_engine()


if __name__ == '__main__':
    unittest.main()
