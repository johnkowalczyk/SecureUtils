from commons_codec.digest import digest_utils

def hash_text(text, algorithm='sha256'):
    data = text.encode()
    if algorithm == 'md5':
        return digest_utils.DigestUtils.md5_hex(data)
    elif algorithm == 'sha1':
        return digest_utils.DigestUtils.sha1_hex(data)
    elif algorithm == 'sha256':
        return digest_utils.DigestUtils.sha256_hex(data)
    elif algorithm == 'sha512':
        return digest_utils.DigestUtils.sha512_hex(data)
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
