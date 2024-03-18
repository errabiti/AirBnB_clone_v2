import unittest
from models.state import State
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test the attributes of State"""
        self.assertTrue(hasattr(State, 'name'))
        self.assertTrue(hasattr(State, 'cities'))

    def test_attributes_type(self):
        """Test the types of attributes of State"""
        self.assertIsInstance(State.name, Column)
        self.assertIsInstance(State.cities, relationship)

    def test_attributes_nullable(self):
        """Test the nullable constraints of attributes of State"""
        self.assertFalse(State.name.nullable)

    def test_relationship(self):
        """Test the relationship between State and other classes"""
        self.assertEqual(State.name.type.python_type, str)
        self.assertIsInstance(State.cities, relationship)
        self.assertTrue(hasattr(State, 'cities'))


if __name__ == "__main__":
    unittest.main()
