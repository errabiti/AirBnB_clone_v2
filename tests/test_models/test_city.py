import unittest
from models.city import City
import models
import mysql.connector

class TestCityMySQLIntegration(unittest.TestCase):
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

        # Initialize models.storage
        models.storage._BaseModel__session = self.conn.cursor()

        # Create tables in the test database
        with open('file.sql', 'r') as file:
            sql_script = file.read()
            self.cursor.execute(sql_script)

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_city_attributes(self):
        """Test attributes of the City model"""
        # Create a new city object
        city = City(name="Test City")

        # Test individual attributes
        self.assertEqual(city.name, "Test City")

    def test_city_behavior(self):
        """Test behavior of the City model"""
        # Create a new city object
        city = City(name="Test City")

        # Save the city to the database
        city.save()

        # Retrieve the city object from the database
        city_from_db = models.storage.get(City, city.id)

        # Test behavior (e.g., saving, updating)
        self.assertEqual(city_from_db.name, "Test City")

if __name__ == "__main__":
    unittest.main()
