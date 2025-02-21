# -*- encoding: utf-8 -*-

import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from pyrpc_schedule.meta import CIPHER_CIPHERTEXT_KEY, CIPHER_PRIVATE_KEY_KEY


class _Cipher:
    """
    A class for decrypting ciphertext using an RSA private key.

    This class takes a configuration dictionary containing ciphertext and a private key,
    decodes them from base64 to bytes, and provides a method to decrypt the ciphertext using the RSA private key.

    Attributes:
        ciphertext (bytes): The ciphertext to be decrypted, decoded from base64.
        private_key (bytes): The RSA private key used for decryption, decoded from base64.
    """

    def __init__(self, config):
        """
        Initialize the _Cipher class.

        Args:
            config (dict): A dictionary containing the ciphertext and private key.
                           The keys are defined by CIPHER_CIPHERTEXT_KEY and CIPHER_PRIVATE_KEY_KEY.
        """
        self.ciphertext = base64.b64decode(config[CIPHER_CIPHERTEXT_KEY].encode('utf-8'))
        self.private_key = base64.b64decode(config[CIPHER_PRIVATE_KEY_KEY].encode('utf-8'))

    def cipher_rsa_dec(self):
        """
        Decrypt the ciphertext using the RSA private key.

        Returns:
            bytes: The decrypted plaintext.
        """
        key = RSA.import_key(self.private_key)
        cipher = PKCS1_v1_5.new(key)
        return cipher.decrypt(self.ciphertext, None)
