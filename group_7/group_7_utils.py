import json
import time
import uuid

class Utils:
    @staticmethod
    def generate_packet(data):
        return json.dumps({
            "packet_id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "value": data
        })

    @staticmethod
    def parse_packet(payload):
        return json.loads(payload)
