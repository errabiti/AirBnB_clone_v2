import unittest
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.user import User
import models

# Import MySQL connector library
import mysql.connector

class TestMySQLIntegration(unittest.TestCase):
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

    def test_place_attributes(self):
        """Test attributes of the Place model"""
        # Create a new place object
        place = Place(name="Test Place")

        # Test individual attributes
        self.assertEqual(place.name, "Test Place")

    def test_place_relationships(self):
        """Test relationships of the Place model"""
        # Create related objects (e.g., city, user)
        city = City(name="Test City")
        user = User(email="test@example.com", password="password")
        city.save()
        user.save()

        # Create a new place object associated with the city and user
        place = Place(name="Test Place", city_id=city.id, user_id=user.id)
        place.save()

        # Retrieve the place object from the database
        place_from_db = models.storage.get(Place, place.id)

        # Test relationships
        self.assertEqual(place_from_db.city, city)
        self.assertEqual(place_from_db.user, user)

    def test_place_behavior(self):
        """Test behavior of the Place model"""
        # Create a new place object
        place = Place(name="Test Place")

        # Save the place to the database
        place.save()

        # Retrieve the place object from the database
        place_from_db = models.storage.get(Place, place.id)

        # Test behavior (e.g., saving, updating)
        self.assertEqual(place_from_db.name, "Test Place")

if __name__ == "__main__":
    unittest.main()
