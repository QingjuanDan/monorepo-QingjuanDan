import unittest
import jsonapi
import datetime

# class TestCustomJSONEncoder(unittest.TestCase):
#     def test_encode_complex_object(self):
#         # Test encoding a complex object
#         complex_obj = {
#             'range_obj': range(1, 6),
#             'timestamp': datetime.datetime.now(),
#         }
#         json_str = jsonapi.dumps(complex_obj)
#         decoded_obj = jsonapi.loads(json_str)
#         self.assertEqual(complex_obj, decoded_obj)
#
#     def test_encode_range_object(self):
#         # Test encoding a range object
#         range_obj = range(10, 21)
#         json_str = jsonapi.dumps(range_obj)
#         decoded_obj = jsonapi.loads(json_str)
#         self.assertEqual(list(range_obj), decoded_obj)

class TestCustomJSONDecoder(unittest.TestCase):
    def test_decode_complex_object(self):
        # Test decoding a complex object
        json_str = '{"range_obj": [1, 2, 3, 4, 5], "timestamp": "2023-09-21T12:34:56.789123"}'
        expected_obj = {
            'range_obj': range(1, 5),
            'timestamp': datetime.datetime(2023, 9, 21, 12, 34, 56, 789123),
        }
        decoded_obj = jsonapi.loads(json_str)
        self.assertEqual(expected_obj, decoded_obj)

    def test_decode_range_object(self):
        # Test decoding a range object
        json_str = '[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]'
        expected_obj = range(10, 21)
        decoded_obj = jsonapi.loads(json_str)
        self.assertEqual(list(expected_obj), decoded_obj)

# class TestCustomJSONFunctions(unittest.TestCase):
#     def test_dumps_and_loads(self):
#         # Test dumps and loads functions with complex data
#         complex_obj = {
#             'range_obj': range(1, 6),
#             'timestamp': datetime.datetime.now(),
#         }
#         json_str = jsonapi.dumps(complex_obj)
#         decoded_obj = jsonapi.loads(json_str)
#         self.assertEqual(complex_obj, decoded_obj)

if __name__ == '__main__':
    unittest.main()

