import unittest
import mysql.connector
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelMySQLIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a connection to the test MySQL database"""
        cls.conn = mysql.connector.connect(
            host="localhost",
            user="test_user",
            password="test_password",
            database="test_database"
        )

    @classmethod
    def tearDownClass(cls):
        """Close the connection to the test MySQL database"""
        cls.conn.close()

    def setUp(self):
        """Create a cursor to execute SQL queries"""
        self.cursor = self.conn.cursor()

        # Create tables in the test database
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS base_models (
                id VARCHAR(60) PRIMARY KEY,
                created_at DATETIME NOT NULL,
                updated_at DATETIME NOT NULL
            )
        """)

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_base_model_attributes(self):
        """Test attributes of the BaseModel class"""
        # Create a new BaseModel object
        base_model = BaseModel()

        # Test individual attributes
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_base_model_save(self):
        """Test saving a BaseModel object to the database"""
        # Create a new BaseModel object
        base_model = BaseModel()

        # Save the base model to the database
        base_model.save()

        # Retrieve the base model object from the database
        self.cursor.execute("SELECT * FROM base_models WHERE id = %s", (base_model.id,))
        result = self.cursor.fetchone()

        # Verify that the object was saved to the database
        self.assertIsNotNone(result)
        self.assertEqual(result[0], base_model.id)
        self.assertEqual(result[1], base_model.created_at)
        self.assertEqual(result[2], base_model.updated_at)


if __name__ == "__main__":
    unittest.main()
