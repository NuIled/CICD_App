import unittest
import os 
import sys
from app import app 

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = self.app.get('/non_existent_page')
        self.assertEqual(response.status_code, 404)
    
    def test_index_data(self):
        response = self.app.get('/#products')
        self.assertTrue(b'Nourish your scalp' in response.data)
        
if __name__ == '__main__':
    unittest.main()
