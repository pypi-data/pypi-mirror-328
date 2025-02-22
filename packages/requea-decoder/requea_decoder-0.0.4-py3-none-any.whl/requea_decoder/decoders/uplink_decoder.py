from abc import abstractmethod
from datetime import datetime
from typing import List

TEMPERATURE_KEY = "temperature"
HUMIDITY_KEY = "humidity"

class UplinkDecoder:
    def __init__(self, payload):
        self.payload = payload
        self.result = []
        
    def __unpack_uplinks(self):
        return self.payload.get("uplinks", [])  
    
    def __extract_datetime(self, uplink):
        ts = uplink.get("ts")
        if ts is None:
            return None
        return datetime.fromtimestamp(ts / 1000)
    
    def __add_result(self, element):
        if element is None:
            return 
        
        if type(element) is list:
            self.result.extend(element)
        else: 
            self.result.append(element)
        
    def format_data(self, data, dt: datetime):
        if data is None:
            return None
        return {"dateTime": dt.strftime('%Y-%m-%dT%H:%M:%SZ'), "data": data}
        
    @abstractmethod
    def decode_uplink(self, uplink):
        pass

    def decode(self) -> List[dict]:
        uplinks = self.__unpack_uplinks()
        for uplink in uplinks:
            data = self.decode_uplink(uplink)
            dt = self.__extract_datetime(uplink)
            formated_data = self.format_data(data, dt)
            self.__add_result(formated_data)
        return self.result
