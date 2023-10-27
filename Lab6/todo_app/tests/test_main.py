import json
import unittest
from fastapi.testclient import TestClient
from ..src.main import app  # Import your FastAPI application instance

client = TestClient(app)

class TestApp(unittest.TestCase):

    def test_firstApi(self):
        response = client.get("/api")
        self.assertEqual(response.json(), {"msg": "hello_worldxxx"})

    def test_firstApiV2(self):
        response = client.get("/books/test_category")
        self.assertEqual(response.json(), {"msg": "test_category"})

    def test_firstApiV3(self):
        valid_category = "fiction"
        response = client.get(f"/books/?category={valid_category}")
        response_json = response.json()
        self.assertTrue(response_json)


    def testGetBookByCategory(self):
        valid_category = "fiction"
        valid_author = "Ernest Hemingway"

        response = client.get(f"/books/by_category_and_author?path_param={valid_category}&author={valid_author}")
        response_json = response.json()
        self.assertTrue(response_json)

    def test_create_book(self):
        new_book = {
            "title": "New Book",
            "author": "Author X",
            "category": "fiction"
        }
        response = client.post("/books/create_book", json=new_book)
        self.assertEqual(response.json(), {"msg": new_book})


    def test_update_book(self):
        updated_book = {
            "title": "The Sun Also Rises",
            "author": "Updated Author",
            "category": "fiction"
        }
        response = client.put("/books/update_book/The%20Sun%20Also%20Rises", json=updated_book)
        self.assertIn("updated successfully", response.json()["msg"])

    def test_delete_book(self):
        response = client.delete("/books/delete_book/The%20Great%20Gatsby")
        self.assertIn("deleted successfully", response.json()["msg"])

    if __name__ == '__main__':
        unittest.main()



