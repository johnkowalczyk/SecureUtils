from commons_codec.binary import base_64, base_32, hex

def encode_base64(text):
    return base_64.Base64.encode_base64_string(text.encode())

def encode_base32(text):
    return base_32.Base32().encode_as_string(text.encode())

def encode_hex(text):
    return hex.Hex.encode_hex_string(text.encode())
