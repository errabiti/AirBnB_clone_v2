import unittest
import mysql.connector
from models.user import User

class TestUserMySQLIntegration(unittest.TestCase):
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
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR(60) PRIMARY KEY,
                email VARCHAR(128) NOT NULL,
                password VARCHAR(128) NOT NULL,
                first_name VARCHAR(128),
                last_name VARCHAR(128)
            )
        )

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_create_user(self):
        """Test creating a User object and saving it to the database"""
        # Create a new User object
        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")

        # Save the User to the database
        user.save()

        # Retrieve the User object from the database
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user.id,))
        result = self.cursor.fetchone()

        # Verify that the object was saved to the database
        self.assertIsNotNone(result)
        self.assertEqual(result[0], user.id)
        self.assertEqual(result[1], user.email)
        self.assertEqual(result[2], user.password)
        self.assertEqual(result[3], user.first_name)
        self.assertEqual(result[4], user.last_name)

if __name__ == "__main__":
    unittest.main()
