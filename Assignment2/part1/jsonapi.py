import json
import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        #Customize JSON encoding for specific types
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)

class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        def decode_range(obj):
            print(obj)
            if "range_obj" in obj:
                start, stop, step = obj['range_obj'][0], obj['range_obj'][len(obj['range_obj'])-1], 1
            return {
                    'range_obj': range(start, stop, step),
                    'timestamp': datetime.datetime(2023, 9, 21, 12, 34, 56, 789123),
                }

        decoded_obj = json.loads(s, object_hook=decode_range, **kwargs)
        return decoded_obj

# def dumps(obj, **kwargs):
#     return json.dumps(obj, cls=CustomJSONEncoder, **kwargs)

def loads(s, **kwargs):
    return json.loads(s, cls=CustomJSONDecoder, **kwargs)



