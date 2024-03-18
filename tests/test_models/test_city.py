import unittest
from models.city import City
from models.state import State
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test the attributes of City"""
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'places'))

    def test_attributes_type(self):
        """Test the types of attributes of City"""
        self.assertIsInstance(City.state_id, Column)
        self.assertIsInstance(City.name, Column)
        self.assertIsInstance(City.places, relationship)

    def test_attributes_nullable(self):
        """Test the nullable constraints of attributes of City"""
        self.assertFalse(City.state_id.nullable)
        self.assertFalse(City.name.nullable)

    def test_relationship(self):
        """Test the relationship between City and Place"""
        self.assertEqual(City.places.property.key, 'places')
        self.assertIsInstance(City.places.argument, str)
        self.assertEqual(City.places.argument, 'Place')
        self.assertTrue(hasattr(City.places, 'backref'))
        self.assertEqual(City.places.backref, 'cities')
        self.assertTrue(hasattr(City.places, 'cascade'))
        self.assertEqual(City.places.cascade, 'delete')


if __name__ == "__main__":
    unittest.main()
