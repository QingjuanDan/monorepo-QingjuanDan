import jsonapi
import datetime

data = {
    'name': 'John',
    'age': 30,
    'timestamp': datetime.datetime.now()
}

json_data = jsonapi.dumps(data, indent=4) 
print(json_data)

json_str = '{"name": "Alice", "age": 25, "timestamp": "2023-09-21T12:34:56.789123"}'
decoded_data = jsonapi.loads(json_str)
print(decoded_data)

