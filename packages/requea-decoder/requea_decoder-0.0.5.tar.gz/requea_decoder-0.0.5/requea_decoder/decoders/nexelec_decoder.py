from datetime import timedelta

from .uplink_decoder import UplinkDecoder, TEMPERATURE_KEY, HUMIDITY_KEY

TEMPERATURE_MESSAGE_TYPE = "Temperature Historical Data"
HUMIDITY_MESSAGE_TYPE = "Humidity Historical Data"


class NexelecDecoder(UplinkDecoder):
    
    def __init__(self, input_data):
        super().__init__(input_data)

    def decode_uplink(self, uplink):
        try:
            raw_data = uplink.get("data", "")
            if not raw_data:
                return None
            bytes_ = bytearray.fromhex(raw_data)
            data = {}
    
            # Conversion des octets en une chaîne hexadécimale
            def bytes_string(input_list):
                buffer_string = ''
                for val in input_list:
                    dec_to_string = format(val, '02x')
                    buffer_string += dec_to_string
                return buffer_string
    
            stringHex = bytes_string(bytes_)
    
            octetTypeProduit = int(stringHex[0:2], 16)
            octetTypeMessage = int(stringHex[2:4], 16)
    
            # Définition des fonctions internes de décodage et utilitaires
    
            def data_output(octetTypeMessage):
                if octetTypeMessage == 0x03:
                    return historicalTemperatureDataOutput(stringHex)
                if octetTypeMessage == 0x04:
                    return historicalHumidityDataOutput(stringHex)
                
    
            def typeOfProduct(octetTypeProduit):
                if octetTypeProduit == 0xA9:
                    return "Feel LoRa"
                if octetTypeProduit == 0xAA:
                    return "Rise LoRa"
                if octetTypeProduit == 0xAB:
                    return "Move LoRa"
                if octetTypeProduit == 0xFF:
                    return "Wave LoRa"
                if octetTypeProduit == 0xAD:
                    return "Sign LoRa"
    
            def typeOfMessage(octetTypeMessage):
                if octetTypeMessage == 0x01:
                    return "Periodic Data"
                if octetTypeMessage == 0x02:
                    return "CO2 Historical Data"
                if octetTypeMessage == 0x03:
                    return "Temperature Historical Data"
                if octetTypeMessage == 0x04:
                    return "Humidity Historical Data"
                if octetTypeMessage == 0x05:
                    return "Product Status"
                if octetTypeMessage == 0x06:
                    return "Product Configuration"
                if octetTypeMessage == 0x11:
                    return "Sigfox Periodic Data"
                if octetTypeMessage == 0x15:
                    return "Sigfox Product Status"
                if octetTypeMessage == 0x16:
                    return "Sigfox Product Configuration N1"
                if octetTypeMessage == 0x17:
                    return "Sigfox Product Configuration N2"
    
    
            def hexToBinary(encoded):
                string_bin = ""
                for char in encoded:
                    val = int(char, 16)
                    bin_str = bin(val)[2:].zfill(4)
                    string_bin += bin_str
                return string_bin
    
            def historicalTemperatureDataOutput(stringHex):
                mesure = []
                data_nombre_mesures = (int(stringHex[4:6], 16) >> 2) & 0x3F
                data_time_between_measurement_min = ((int(stringHex[4:8], 16) >> 2) & 0xFF)
                data_repetition = (int(stringHex[7:9], 16)) & 0x3F
                binary = hexToBinary(stringHex)
    
                for i in range(data_nombre_mesures):
                    offset_binaire = 36 + (10 * i)
                    val = int(binary[offset_binaire:offset_binaire + 10], 2)
                    if val == 0x3FF:
                        val = 0
                    else:
                        val = float(((val / 10) - 30))
                    mesure.append(val)
    
                return {
                    "typeOfProduct": typeOfProduct(octetTypeProduit),
                    "typeOfMessage": typeOfMessage(octetTypeMessage),
                    "numberOfRecord": data_nombre_mesures,
                    "periodBetweenRecord": {"value": data_time_between_measurement_min * 10, "unit": "minutes"},
                    "redundancyOfRecord": data_repetition,
                    "temperature": {"value": mesure, "unit": "°C"},
                }
    
            def historicalHumidityDataOutput(stringHex):
                mesure = []
                data_nombre_mesures = (int(stringHex[4:6], 16) >> 2) & 0x3F
                data_time_between_measurement_min = ((int(stringHex[4:8], 16) >> 2) & 0xFF)
                data_repetition = (int(stringHex[7:9], 16)) & 0x3F
                binary = hexToBinary(stringHex)
    
                for i in range(data_nombre_mesures):
                    offset_binaire = 36 + (10 * i)
                    val = int(binary[offset_binaire:offset_binaire + 10], 2)
                    if val == 0x3FF:
                        val = 0
                    else:
                        val = float((val * 0.1))
                    mesure.append(val)
    
                return {
                    "typeOfProduct": typeOfProduct(octetTypeProduit),
                    "typeOfMessage": typeOfMessage(octetTypeMessage),
                    "numberOfRecord": data_nombre_mesures,
                    "periodBetweenRecord": {"value": data_time_between_measurement_min * 10, "unit": "minutes"},
                    "redundancyOfRecord": data_repetition,
                    "humidity": {"value": mesure, "unit": "%RH"},
                }
    
            return data_output(octetTypeMessage)
        except Exception as e:
            raise Exception(str(e))
    
    def __get_metric_key(self, data):
        if data['typeOfMessage'] == TEMPERATURE_MESSAGE_TYPE:
            return TEMPERATURE_KEY
        elif data['typeOfMessage'] == HUMIDITY_MESSAGE_TYPE:
            return HUMIDITY_KEY
    
    def format_data(self, data, dt):
        """
            As historical data is stored from the most recent to the oldest, we need to reverse the list
            and calculate the datetime of each record based on the period between records.
        """
        if data is None:
            return None
        
        metric_key = self.__get_metric_key(data)
        period_between_records = timedelta(minutes=data['periodBetweenRecord']['value'])
        temperatures = data[metric_key]['value'][:12]

        transformed_payload = []
        for i, temp in enumerate(temperatures):
            temp_datetime = dt - i * period_between_records
            transformed_payload.append({
                'dateTime': temp_datetime.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'data': {metric_key: temp}
            })
        return transformed_payload
