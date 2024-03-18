import unittest
import mysql.connector
from models.review import Review

class TestReviewMySQLIntegration(unittest.TestCase):
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
            CREATE TABLE IF NOT EXISTS reviews (
                id VARCHAR(60) PRIMARY KEY,
                text TEXT NOT NULL,
                place_id VARCHAR(60) NOT NULL,
                user_id VARCHAR(60) NOT NULL
            )
        )

    def tearDown(self):
        """Rollback any changes made during the test and close the cursor"""
        self.conn.rollback()
        self.cursor.close()

    def test_create_review(self):
        """Test creating a Review object and saving it to the database"""
        # Create a new Review object
        review = Review(text="This place is great!", place_id="place_id",
                        user_id="user_id")

        # Save the Review to the database
        review.save()

        # Retrieve the Review object from the database
        self.cursor.execute("SELECT * FROM reviews WHERE id = %s", (review.id,))
        result = self.cursor.fetchone()

        # Verify that the object was saved to the database
        self.assertIsNotNone(result)
        self.assertEqual(result[0], review.id)
        self.assertEqual(result[1], review.text)
        self.assertEqual(result[2], review.place_id)
        self.assertEqual(result[3], review.user_id)

if __name__ == "__main__":
    unittest.main()
