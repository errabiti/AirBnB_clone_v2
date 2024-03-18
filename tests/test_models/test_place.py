import unittest
import mysql.connector
from models.place import Place

class TestPlaceMySQLIntegration(unittest.TestCase):
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
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS places (
                id VARCHAR(60) PRIMARY KEY,
                city_id VARCHAR(60) NOT NULL,
                user_id VARCHAR(60) NOT NULL,
                name VARCHAR(128) NOT NULL,
                description TEXT,
                number_rooms INT NOT NULL,
                number_bathrooms INT NOT NULL,
                max_guest INT NOT NULL,
                price_by_night INT NOT NULL,
                latitude FLOAT,
                longitude FLOAT
            )
        )

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_create_place(self):
        """Test creating a Place object and saving it to the database"""
        # Create a new Place object
        place = Place(city_id="city_id", user_id="user_id", name="Place Name",
                      description="Place description", number_rooms=2,
                      number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=40.7128, longitude=-74.0060)

        # Save the Place to the database
        place.save()

        # Retrieve the Place object from the database
        self.cursor.execute("SELECT * FROM places WHERE id = %s", (place.id,))
        result = self.cursor.fetchone()

        # Verify that the object was saved to the database
        self.assertIsNotNone(result)
        self.assertEqual(result[0], place.id)
        self.assertEqual(result[1], place.city_id)
        self.assertEqual(result[2], place.user_id)
        self.assertEqual(result[3], place.name)
        self.assertEqual(result[4], place.description)
        self.assertEqual(result[5], place.number_rooms)
        self.assertEqual(result[6], place.number_bathrooms)
        self.assertEqual(result[7], place.max_guest)
        self.assertEqual(result[8], place.price_by_night)
        self.assertEqual(result[9], place.latitude)
        self.assertEqual(result[10], place.longitude)

if __name__ == "__main__":
    unittest.main()
