import unittest
from models.review import Review
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test the attributes of Review"""
        self.assertTrue(hasattr(Review, 'text'))
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))

    def test_attributes_type(self):
        """Test the types of attributes of Review"""
        self.assertIsInstance(Review.text, Column)
        self.assertIsInstance(Review.place_id, Column)
        self.assertIsInstance(Review.user_id, Column)

    def test_attributes_nullable(self):
        """Test the nullable constraints of attributes of Review"""
        self.assertFalse(Review.text.nullable)
        self.assertFalse(Review.place_id.nullable)
        self.assertFalse(Review.user_id.nullable)

    def test_relationship(self):
        """Test the relationship between Review and other classes"""
        self.assertEqual(Review.text.type.python_type, str)
        self.assertEqual(Review.place_id.type.python_type, str)
        self.assertEqual(Review.user_id.type.python_type, str)
        self.assertEqual(Review.place_id.foreign_keys, {Review.place_id})
        self.assertEqual(Review.user_id.foreign_keys, {Review.user_id})


if __name__ == "__main__":
    unittest.main()
