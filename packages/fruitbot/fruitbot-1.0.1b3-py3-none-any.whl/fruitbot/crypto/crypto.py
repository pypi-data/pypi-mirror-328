import base64
import urllib.parse
from typing import Optional
from itertools import cycle

class Encryption:
    def __init__(self, key: Optional[bytes] = None):
        self.key = key if key else b'ali1343faraz1055antler288based'

    def encrypt(self, message: str) -> str:
        """Encrypts a message using XOR encryption."""
        message_bytes = message.encode('utf-8')
        output_bytes = bytes(m ^ k for m, k in zip(message_bytes, cycle(self.key)))
        encoded = base64.b64encode(output_bytes).decode('utf-8')
        return urllib.parse.quote(encoded)

    def decrypt(self, encrypted: str) -> str:
        """Decrypts an encrypted message using XOR decryption."""
        try:
            unquoted = urllib.parse.unquote(encrypted)
            if encrypted.startswith("{"):
                return encrypted
            encrypted_bytes = base64.b64decode(unquoted)
        except (ValueError, base64.binascii.Error) as err:
            print(f"Error during decoding: {err}")
            return ""

        decrypted_bytes = bytes(e ^ k for e, k in zip(encrypted_bytes, cycle(self.key)))
        return decrypted_bytes.decode('utf-8', errors='ignore')
