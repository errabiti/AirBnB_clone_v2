import unittest
import mysql.connector
from models.state import State


class TestStateMySQLIntegration(unittest.TestCase):
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
            CREATE TABLE IF NOT EXISTS states (
                id VARCHAR(60) PRIMARY KEY,
                name VARCHAR(128) NOT NULL
            )
        """)

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_create_state(self):
        """Test creating a State object and saving it to the database"""
        # Create a new State object
        state = State(name="California")

        # Save the state to the database
        state.save()

        # Retrieve the state object from the database
        self.cursor.execute("SELECT * FROM states WHERE id = %s", (state.id,))
        result = self.cursor.fetchone()

        # Verify that the object was saved to the database
        self.assertIsNotNone(result)
        self.assertEqual(result[0], state.id)
        self.assertEqual(result[1], state.name)


if __name__ == "__main__":
    unittest.main()
