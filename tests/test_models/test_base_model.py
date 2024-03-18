import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_inheritance(self):
        """Test if BaseModel inherits from object"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, object)

    def test_id_type(self):
        """Test if the id attribute is of type string"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_created_at_type(self):
        """Test if the created_at attribute is of type datetime"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if the updated_at attribute is of type datetime"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_id_uniqueness(self):
        """Test if each instance has a unique id"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_created_updated_at_equal(self):
        """Test if created_at and updated_at attributes are equal at creation"""
        base_model = BaseModel()
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertIn("[BaseModel]", base_model_str)
        self.assertIn("'id':", base_model_str)
        self.assertIn("'created_at':", base_model_str)
        self.assertIn("'updated_at':", base_model_str)

    def test_save_method(self):
        """Test the save method of BaseModel"""
        base_model = BaseModel()
        prev_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(prev_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)

    def test_to_dict_method_with_id(self):
        """Test the to_dict method with include_id=True"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict(include_id=True)
        self.assertEqual(base_model_dict["id"], base_model.id)

    def test_init_with_kwargs(self):
        """Test if BaseModel initializes attributes correctly with kwargs"""
        data = {
            "id": str(uuid.uuid4()),
            "created_at": "2022-01-01T00:00:00.000000",
            "updated_at": "2022-01-01T00:00:00.000000",
            "name": "test_name"
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, data["id"])
        self.assertEqual(base_model.created_at.isoformat(), data["created_at"])
        self.assertEqual(base_model.updated_at.isoformat(), data["updated_at"])
        self.assertEqual(base_model.name, data["name"])


if __name__ == "__main__":
    unittest.main()
