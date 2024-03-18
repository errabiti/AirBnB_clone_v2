import unittest
import mysql.connector
from models.city import City

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

        # Create tables in the test database
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS cities (
                id VARCHAR(60) PRIMARY KEY,
                state_id VARCHAR(60) NOT NULL,
                name VARCHAR(128) NOT NULL
            )
        )

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_create_city(self):
        """Test creating a City object and saving it to the database"""
        # Create a new City object
        city = City(state_id="state_id", name="City Name")

        # Save the City to the database
        city.save()

        # Retrieve the City object from the database
        self.cursor.execute("SELECT * FROM cities WHERE id = %s", (city.id,))
        result = self.cursor.fetchone()

        # Verify that the object was saved to the database
        self.assertIsNotNone(result)
        self.assertEqual(result[0], city.id)
        self.assertEqual(result[1], city.state_id)
        self.assertEqual(result[2], city.name)

if __name__ == "__main__":
    unittest.main()
