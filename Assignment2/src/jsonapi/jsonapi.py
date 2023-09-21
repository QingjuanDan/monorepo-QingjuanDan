import json
import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, range):
            return list(obj)  # Encode range as a list
        return super().default(obj)


from dateutil import parser

class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        def decode_object(obj):
            if "__datetime__" in obj:
                return parser.isoparse(obj["value"])
            elif "__range__" in obj:
                return range(obj["start"], obj["stop"])
            return obj

        decoded_obj = json.loads(s, object_hook=decode_object, **kwargs)
        return decoded_obj



def dumps(obj, **kwargs):
    return json.dumps(obj, cls=CustomJSONEncoder, **kwargs)

def loads(s, **kwargs):
    return json.loads(s, cls=CustomJSONDecoder, **kwargs)