import unittest
import mysql.connector
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsoleMySQLIntegration(unittest.TestCase):
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
            CREATE TABLE IF NOT EXISTS states (
                id VARCHAR(60) PRIMARY KEY,
                name VARCHAR(128) NOT NULL
            )
        )
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS cities (
                id VARCHAR(60) PRIMARY KEY,
                state_id VARCHAR(60),
                name VARCHAR(128) NOT NULL,
                FOREIGN KEY (state_id) REFERENCES states(id)
            )
        )
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR(60) PRIMARY KEY,
                email VARCHAR(128) NOT NULL,
                password VARCHAR(128) NOT NULL,
                first_name VARCHAR(128),
                last_name VARCHAR(128)
            )
        )
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS places (
                id VARCHAR(60) PRIMARY KEY,
                city_id VARCHAR(60),
                user_id VARCHAR(60),
                name VARCHAR(128) NOT NULL,
                description TEXT,
                number_rooms INT,
                number_bathrooms INT,
                max_guest INT,
                price_by_night INT,
                latitude FLOAT,
                longitude FLOAT,
                FOREIGN KEY (city_id) REFERENCES cities(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        )
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS amenities (
                id VARCHAR(60) PRIMARY KEY,
                name VARCHAR(128) NOT NULL
            )
        )
        self.cursor.execute(
            CREATE TABLE IF NOT EXISTS reviews (
                id VARCHAR(60) PRIMARY KEY,
                place_id VARCHAR(60),
                user_id VARCHAR(60),
                text TEXT,
                FOREIGN KEY (place_id) REFERENCES places(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        )

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_and_show(self, mock_stdout):
        """Test creating and showing objects in the console"""
        # Start the console and create a State object
        with patch('builtins.input', side_effect=['create State name="California"', 'show State']):
            HBNBCommand().cmdloop()

        # Retrieve the State object from the database
        self.cursor.execute("SELECT * FROM states")
        result = self.cursor.fetchall()

        # Assert that the State object was created and stored in the database
        self.assertTrue(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "California")

        # Clear the mock stdout buffer
        mock_stdout.seek(0)
        mock_stdout.truncate(0)

        # Show the State object
        with patch('builtins.input', side_effect=['show State 1']):
            HBNBCommand().cmdloop()

        # Assert that the State object was shown in the console
        self.assertIn("California", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
