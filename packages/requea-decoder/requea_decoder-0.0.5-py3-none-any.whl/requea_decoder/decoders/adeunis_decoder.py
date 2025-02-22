import struct
from datetime import datetime, timezone

from .uplink_decoder import UplinkDecoder, TEMPERATURE_KEY

SONDE_TEMPERATURE_1 = 'temperature 1'
SONDE_TEMPERATURE_2 = 'temperature 2'


class AdeunisDecoder(UplinkDecoder):
    def __init__(self, payload):
        super().__init__(payload)
    
    def decode_uplink(self, uplink):
        raw_data = uplink.get("data", "")
        if not raw_data.startswith('57'):
            return None
        
        payload = bytearray.fromhex(raw_data)
        
        app_content = {'type': '0x57 Temp 4 periodic data'}
        nb_sensors = 2 if payload[1] & 0x10 else 1
        temperatures = []
        ch1_temp = []
        ch2_temp = []
        payload_length = len(payload) - 4 if payload[1] & 0x04 else len(payload)

        # Boucle sur les données de température
        for offset in range(2, payload_length, 2 * nb_sensors):
            raw_value = struct.unpack('>h', payload[offset:offset + 2])[0]  # Big Endian int16
            ch1_temp.append(raw_value / 10)
            if nb_sensors == 2:
                raw_value = struct.unpack('>h', payload[offset + 2:offset + 4])[0]
                ch2_temp.append(raw_value / 10)

        if payload[1] & 0x04:
            # Lecture du timestamp
            timestamp_offset = len(payload) - 4
            timestamp_raw = struct.unpack('>I', payload[timestamp_offset:timestamp_offset + 4])[0]  # Big Endian uint32
            my_date = datetime.fromtimestamp(timestamp_raw + 1356998400, tz=timezone.utc)
            app_content['timestamp'] = my_date.isoformat()

        app_content['decodingInfo'] = 'values: [t=0, t-1, t-2, ...]'
        temperatures.append({'name': SONDE_TEMPERATURE_1, 'unit': '°C', 'values': ch1_temp})
        if nb_sensors == 2:
            temperatures.append({'name': SONDE_TEMPERATURE_2, 'unit': '°C', 'values': ch2_temp})
        app_content['temperatures'] = temperatures
        return app_content

    def format_data(self, data, dt):
        if data is None:
            return None
        
        temperature = [temp for temp in data['temperatures'] if temp['name'] == SONDE_TEMPERATURE_1][0]['values'][0]
    
        return {"dateTime": dt.strftime('%Y-%m-%dT%H:%M:%SZ'), "data": {TEMPERATURE_KEY: temperature}}
