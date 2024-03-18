import unittest
from models.user import User
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test the attributes of User"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertTrue(hasattr(User, 'review'))
        self.assertTrue(hasattr(User, 'places'))

    def test_attributes_type(self):
        """Test the types of attributes of User"""
        self.assertIsInstance(User.email, Column)
        self.assertIsInstance(User.password, Column)
        self.assertIsInstance(User.first_name, Column)
        self.assertIsInstance(User.last_name, Column)
        self.assertIsInstance(User.review, relationship)
        self.assertIsInstance(User.places, relationship)

    def test_attributes_nullable(self):
        """Test the nullable constraints of attributes of User"""
        self.assertFalse(User.email.nullable)
        self.assertFalse(User.password.nullable)
        self.assertTrue(User.first_name.nullable)
        self.assertTrue(User.last_name.nullable)

    def test_relationship(self):
        """Test the relationship between User and other classes"""
        self.assertIsInstance(User.review, relationship)
        self.assertIsInstance(User.places, relationship)


if __name__ == "__main__":
    unittest.main()
