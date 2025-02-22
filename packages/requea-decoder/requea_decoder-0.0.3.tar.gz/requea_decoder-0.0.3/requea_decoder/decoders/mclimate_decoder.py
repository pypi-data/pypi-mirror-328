from uplink_decoder import UplinkDecoder, TEMPERATURE_KEY, HUMIDITY_KEY


class MClimateDecoder(UplinkDecoder):
    
    def __init__(self, payload):
        super().__init__(payload)

    def decode_uplink(self, uplink):
        """Decode input uplink data into a structured dictionary."""
        try:
            raw_data = uplink.get("data", "")
            if not raw_data:
                return None
            bytes_ = bytearray.fromhex(raw_data)
            data = {}
    
            def calculate_temperature(raw_data):
                return (raw_data - 400) / 10.0
    
            def calculate_humidity(raw_data):
                return (raw_data * 100.0) / 256.0
    
            def dec_bin(number):
                if number < 0:
                    number = 0xFFFFFFFF + number + 1
                return bin(number)[2:]
    
            def handle_keepalive(bytes_, data):
                # Calcul de la température
                temp_hex = (
                    "0" + format(bytes_[1], "x") + format(bytes_[2], "x")
                )
                temp_dec = int(temp_hex, 16)
                temperature_value = calculate_temperature(temp_dec)
    
                # Calcul de l'humidité
                humidity_value = calculate_humidity(bytes_[3])
    
                # Calcul de la batterie
                battery_tmp = ("0" + format(bytes_[4], "x"))[-2][0]
                battery_voltage_calculated = 2 + int("0x" + battery_tmp, 16) * 0.1
    
                # Vérification connectique thermistor
                binary_5 = dec_bin(bytes_[5])
                # On s’assure que la chaîne binaire a au moins 6 bits
                binary_5 = binary_5.zfill(6)
                thermistor_connected = (binary_5[5] == '0')
    
                ext_t1 = ("0" + format(bytes_[5], "x"))[-2][0]
                ext_t2 = ("0" + format(bytes_[6], "x"))[-2:]
    
                ext_thermistor_temperature = 0
                if thermistor_connected:
                    ext_thermistor_temperature = (
                        int("0x" + ext_t1 + ext_t2, 16) * 0.1
                    )
    
                data[TEMPERATURE_KEY] = round(temperature_value, 2)
                data[HUMIDITY_KEY] = round(humidity_value, 2)
                data["batteryVoltage"] = round(battery_voltage_calculated, 2)
                data["thermistorProperlyConnected"] = thermistor_connected
                data["extThermistorTemperature"] = ext_thermistor_temperature
    
                return data
    
            def handle_response(bytes_, data):
                commands = [("0" + format(b, "x"))[-2:] for b in bytes_]
                # On retire les 7 derniers octets (correspondant au keepalive)
                commands = commands[:-7]
    
                i = 0
                while i < len(commands):
                    command = commands[i]
                    command_len = 0
    
                    if command == '04':
                        # Hardware/Software version
                        command_len = 3
                        if i + 2 < len(commands):
                            hw_version = commands[i + 1]
                            sw_version = commands[i + 2]
                            data["deviceVersions"] = {
                                "hardware": int(hw_version, 16),
                                "software": int(sw_version, 16)
                            }
    
                    elif command == '12':
                        # Keepalive time
                        command_len = 2
                        if i + 1 < len(commands):
                            data["keepAliveTime"] = int(commands[i + 1], 16)
    
                    elif command == '19':
                        # Join retry period
                        command_len = 2
                        if i + 1 < len(commands):
                            cmd_response = int(commands[i + 1], 16)
                            period_in_minutes = cmd_response * 5.0 / 60.0
                            data["joinRetryPeriod"] = period_in_minutes
    
                    elif command == '1b':
                        # Uplink type
                        command_len = 2
                        if i + 1 < len(commands):
                            data["uplinkType"] = int(commands[i + 1], 16)
    
                    elif command == '1d':
                        # Watchdog params
                        command_len = 3
                        if i + 2 < len(commands):
                            wdp_c = (False if commands[i + 1] == '00'
                                     else int(commands[i + 1], 16))
                            wdp_uc = (False if commands[i + 2] == '00'
                                      else int(commands[i + 2], 16))
                            data["watchDogParams"] = {"wdpC": wdp_c, "wdpUc": wdp_uc}
    
                    else:
                        # Commande non reconnue
                        command_len = 1
    
                    i += command_len
    
                return data
    
            if bytes_[0] == 1:
                # Directement un keepalive
                data = handle_keepalive(bytes_, data)
            else:
                # Réponse d'abord, puis keepalive (7 derniers octets)
                data = handle_response(bytes_, data)
                keepalive_bytes = bytes_[-7:]
                data = handle_keepalive(keepalive_bytes, data)
    
            return data
    
        except Exception as e:
            raise Exception(str(e))
    
