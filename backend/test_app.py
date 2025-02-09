# backend/test_app.py
import unittest
from main import main

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main.test_client()
        self.app.testing = True

    def test_create_and_read(self):
        # Test de création d'un enregistrement
        response = self.app.post('/create', json={'Name': 'fam-name', 'Scholl': 'test'})
        
        self.assertEqual(response.status_code, 201)
        # Test de lecture
        response = self.app.get('/read/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('School'), 'test')

if __name__ == '__main__':
    unittest.main()
