import unittest
from app import create_app
from app.models.category import Category

class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True

    def test_home(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_home_category(self):
        category = Category(name="Test_category")
        response = self.client.get(f'/home/category/{category.id}')
        self.assertEqual(response.status_code, 200)
  

if __name__ == '__main__':
    unittest.main()