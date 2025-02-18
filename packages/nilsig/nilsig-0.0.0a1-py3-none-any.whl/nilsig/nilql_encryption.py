"""Encryption utilities using nilQL for secret sharing"""

from typing import List, Union

import nilql


class DataEncryption:
    """Class for encapsulating encryption methods."""

    def __init__(self, num_nodes: int, seed: Union[bytes, bytearray, str]):
        self.num_nodes = num_nodes
        self.secret_key = nilql.SecretKey.generate(
            cluster={"nodes": [{}] * num_nodes},
            operations={"store": True},
            seed=seed,
        )

    def encrypt(self, payload: str) -> List[str]:
        """Encrypt payload using secret sharing."""
        try:
            encrypted_shares = nilql.encrypt(self.secret_key, payload)

            return list(encrypted_shares)
        except Exception as e:
            raise RuntimeError(f"Encryption failed: {str(e)}") from e

    def decrypt(self, encoded_shares: List[str]) -> str:
        """Decrypt payload from shares."""
        try:
            decoded_shares = []
            for share in encoded_shares:
                decoded_shares.append(share)

            return str(nilql.decrypt(self.secret_key, decoded_shares))
        except Exception as e:
            raise RuntimeError(f"Decryption failed: {str(e)}") from e
