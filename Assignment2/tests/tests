import unittest
import datetime
from jsonapi import CustomJSONEncoder, CustomJSONDecoder, dumps, loads


class TestCustomJSONEncoder(unittest.TestCase):
    def test_encode_datetime(self):
        dt = datetime.datetime(2023, 9, 21, 12, 34, 56)
        encoded = dumps(dt)
        self.assertIn(dt.isoformat(), encoded)

    def test_encode_range(self):
        r = range(1, 5)
        encoded = dumps(r)
        self.assertIn('[1, 2, 3, 4]', encoded)


class TestCustomJSONDecoder(unittest.TestCase):
    def test_decode_datetime(self):
        dt_str = '{"__datetime__": true, "value": "2023-09-21T12:34:56"}'
        decoded = loads(dt_str)
        self.assertEqual(decoded, datetime.datetime(2023, 9, 21, 12, 34, 56))

    def test_decode_range(self):
        range_str = '{"__range__": true, "start": 1, "stop": 5}'
        decoded = loads(range_str)
        self.assertEqual(decoded, range(1, 5))


class TestIntegration(unittest.TestCase):
    def test_integration(self):
        original = {
            "datetime": datetime.datetime(2023, 9, 21, 12, 34, 56),
            "range": range(1, 5)
        }
        encoded = dumps(original)  # Ensure this is encoding the datetime and range properly
        decoded = loads(encoded)  # Ensure this is decoding the datetime and range properly

        # Now check the equality of the original and decoded objects
        self.assertEqual(original['datetime'], decoded['datetime'])
        self.assertEqual(list(original['range']), list(decoded['range']))


if __name__ == '__main__':
    unittest.main()
