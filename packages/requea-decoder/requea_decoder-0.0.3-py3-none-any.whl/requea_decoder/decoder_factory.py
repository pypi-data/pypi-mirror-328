from decoders.adeunis_decoder import AdeunisDecoder
from decoders.mclimate_decoder import MClimateDecoder
from decoders.nexelec_decoder import NexelecDecoder
from decoders.uplink_decoder import UplinkDecoder


MCLIMATE_CODEC_NAME = "mclimate.ht@requea_raw"
NEXELEC_CODEC_NAME = "nexelec.feel@requea_raw"
ADEUNIS_CODEC_NAME = "adeunis.temp@requea_raw"

class DecoderFactory:
    def __init__(self, codec: str, payload):
        self.codec = codec
        self.payload = payload

    def build(self) -> UplinkDecoder:
        if self.codec == MCLIMATE_CODEC_NAME:
            return MClimateDecoder(self.payload)
        if self.codec == NEXELEC_CODEC_NAME:
            return NexelecDecoder(self.payload)
        if self.codec == ADEUNIS_CODEC_NAME:
            return AdeunisDecoder(self.payload)
        raise Exception(f"Codec {self.codec} not implemented")
