class Crypto:
    def __init__(self):
        # Expanded character set including uncommon characters
        self.char_set = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789"
            "!@#$%^&*()_+-=~`[]{};':\",.<>?/|\\"
            "•¢∞§¶•ªº–≠≡√∫∑≠∂∑Ω≈≡√≠≡|"
            "⅛⅜⅝⅞←↑→↓↔↕⇌⇋⇐⇒⇑⇓⊕⊗⊥∪∩∫"
        )

    def encrypt(self, data: str, key: str) -> str:
        """Encrypts the data using a repeating key and returns a string."""
        data_bytes = data.encode()
        key_bytes = key.encode()
        encrypted = bytearray()
        key_length = len(key_bytes)

        for i, byte in enumerate(data_bytes):
            encrypted.append(byte ^ key_bytes[i % key_length])

        return self.bytes_to_string(encrypted)

    def decrypt(self, encrypted_data: str, key: str) -> str:
        """Decrypts the string back to the original data using the same key."""
        encrypted_bytes = self.string_to_bytes(encrypted_data)
        decrypted = bytearray()
        key_bytes = key.encode()
        key_length = len(key_bytes)

        for i, byte in enumerate(encrypted_bytes):
            decrypted.append(byte ^ key_bytes[i % key_length])

        return decrypted.decode('utf-8', errors='ignore')  # Use 'ignore' to handle any potential errors

    def bytes_to_string(self, data: bytes) -> str:
        """Convert bytes to a string using the defined character set."""
        return ''.join(self.char_set[b % len(self.char_set)] for b in data)

    def string_to_bytes(self, str: str) -> bytes:
        """Convert a string back to bytes."""
        return bytearray(self.char_set.index(c) for c in str)

class VIRTO1024:
    def __init__(self):
        self.hex_chars = "abcdef0123456789"

    def virto1024(self, data: str) -> str:
        """1024-bit (128-character) hashing function using only 'abcdef0123456789'."""
        data_bytes = data.encode()
        hash_length = 128
        hash_seed = bytearray(hash_length)

        # Initial hash generation using XOR and systematic transformations
        for i, b in enumerate(data_bytes):
            hash_seed[i % hash_length] ^= b

        # Create the hash without using random and minimizing patterns
        final_hash = []
        last_char = None

        for i in range(hash_length):
            # Create a deterministic character based on the current index
            char_index = (hash_seed[i % len(hash_seed)] + i) % 16
            char = self.hex_chars[char_index]

            # Ensure no two adjacent characters are the same
            while char == last_char:
                char_index = (char_index + 1) % 16  # Increment to find a new character
                char = self.hex_chars[char_index]

            final_hash.append(char)
            last_char = char

        return ''.join(final_hash)