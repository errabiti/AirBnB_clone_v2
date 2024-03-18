import unittest
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, Float, Integer, String, Table
from sqlalchemy.orm import relationship
from os import getenv


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test the attributes of Place"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'reviews'))
        self.assertTrue(hasattr(Place, 'amenities'))

    def test_attributes_type(self):
        """Test the types of attributes of Place"""
        self.assertIsInstance(Place.city_id, Column)
        self.assertIsInstance(Place.user_id, Column)
        self.assertIsInstance(Place.name, Column)
        self.assertIsInstance(Place.description, Column)
        self.assertIsInstance(Place.number_rooms, Column)
        self.assertIsInstance(Place.number_bathrooms, Column)
        self.assertIsInstance(Place.max_guest, Column)
        self.assertIsInstance(Place.price_by_night, Column)
        self.assertIsInstance(Place.latitude, Column)
        self.assertIsInstance(Place.longitude, Column)
        self.assertIsInstance(Place.reviews, relationship)
        self.assertIsInstance(Place.amenities, relationship)

    def test_attributes_nullable(self):
        """Test the nullable constraints of attributes of Place"""
        self.assertFalse(Place.city_id.nullable)
        self.assertFalse(Place.user_id.nullable)
        self.assertFalse(Place.name.nullable)
        self.assertTrue(Place.description.nullable)
        self.assertFalse(Place.number_rooms.nullable)
        self.assertFalse(Place.number_bathrooms.nullable)
        self.assertFalse(Place.max_guest.nullable)
        self.assertFalse(Place.price_by_night.nullable)
        self.assertTrue(Place.latitude.nullable)
        self.assertTrue(Place.longitude.nullable)

    def test_relationship(self):
        """Test the relationship between Place and other classes"""
        self.assertEqual(Place.city_id.type.python_type, str)
        self.assertEqual(Place.user_id.type.python_type, str)
        self.assertEqual(Place.reviews.argument, "Review")
        self.assertEqual(Place.reviews.backref, "place")
        self.assertEqual(Place.reviews.cascade, "delete")
        self.assertEqual(Place.amenities.argument, "Amenity")
        self.assertEqual(Place.amenities.secondary, "place_amenity")
        self.assertFalse(Place.amenities.viewonly)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "Skipping non-DB storage test")
    def test_amenities_relationship(self):
        """Test the relationship between Place and Amenity"""
        self.assertTrue(hasattr(Place, 'amenities'))
        self.assertIsInstance(Place.amenities, relationship)
        self.assertEqual(Place.amenities.argument, "Amenity")
        self.assertEqual(Place.amenities.secondary, "place_amenity")
        self.assertFalse(Place.amenities.viewonly)
        self.assertIsInstance(Place.amenities.secondary, Table)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "Skipping DB storage test")
    def test_reviews_relationship(self):
        """Test the relationship between Place and Review"""
        self.assertTrue(hasattr(Place, 'reviews'))
        self.assertIsInstance(Place.reviews, list)
        self.assertEqual(len(Place.reviews), 0)


if __name__ == "__main__":
    unittest.main()
