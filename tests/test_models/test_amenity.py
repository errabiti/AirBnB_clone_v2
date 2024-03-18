import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_table_name(self):
        """Test if the table name is set correctly"""
        self.assertEqual(Amenity.__tablename__, "amenities")

    def test_name_attribute(self):
        """Test if the name attribute is correctly set"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_relationship(self):
        """Test if the relationship with Place is correctly set"""
        amenity = Amenity()
        if getenv('HBNB_TYPE_STORAGE') == "db":
            self.assertTrue(hasattr(amenity, "place_amenities"))
        else:
            self.assertFalse(hasattr(amenity, "place_amenities"))

    def test_name_type(self):
        """Test if the name attribute is of type string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_name_default_value(self):
        """Test if the default value of name attribute is an empty string"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_created_at(self):
        """Test if the created_at attribute is correctly set"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at(self):
        """Test if the updated_at attribute is correctly set"""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict method of Amenity"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_str_method(self):
        """Test the __str__ method of Amenity"""
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("'id':", amenity_str)
        self.assertIn("'created_at':", amenity_str)
        self.assertIn("'updated_at':", amenity_str)

if __name__ == "__main__":
    unittest.main()
