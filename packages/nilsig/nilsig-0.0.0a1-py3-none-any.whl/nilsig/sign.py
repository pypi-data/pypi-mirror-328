"""Signing a message with a signing key retrieved from nilDB"""

import base64
from typing import Dict, List

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

from .nildb_api import data_read
from .nilql_encryption import DataEncryption


async def sign(
    signature_scheme: str,
    nodes_and_jwts: List[Dict],
    store_id: str,
    message: str,
    encryption: DataEncryption,
    schema_id: str,
) -> Dict:
    """
    Sign a message.

    Args:
        signature_scheme (str): Either "ECDSA" or "EdDSA"
        nodes_and_jwts (List[Dict]): List of dicts with node info and JWTs
        store_id (str): ID for stored key shares
        message (str): Message to sign
        encryption (DataEncryption): Encryption instance
        schema_id (str): Schema ID for nilDB

    Returns:
        Dict: Contains either:
            - {"signature": base64_signature} for unencrypted signature
            - {"encrypted_signature": encrypted_signature} for encrypted signature

    Example of ``nodes_and_jwts`` input:

    .. code-block:: python

        [
            {
                "node_url": "node1.example.com",
                "node_jwt": "jwt_token",
                "public_key": "pub_key"
            },
            ...
        ]
    """
    # Retrieve key shares from nilDB
    shares = []
    for node in nodes_and_jwts:
        response = data_read(node, schema_id, filter_dict={"_id": store_id})
        if not response:
            raise RuntimeError(
                "There was a problem retrieving the signing key shares from SecretVault."
            )
        shares.append(response[0]["key_share"])

    # Verify all shares were retrieved
    if len(shares) != len(nodes_and_jwts):
        raise ValueError(
            "The retrieved encrypted shares count didn't match the node count."
        )

    # Reconstruct private key
    pem_private_key = encryption.decrypt(shares)
    restored_private_key = serialization.load_pem_private_key(
        pem_private_key.encode("utf-8"), password=None
    )

    # Sign the message
    message_bytes = message.encode()
    if signature_scheme == "EdDSA":
        signature = restored_private_key.sign(message_bytes)
    elif signature_scheme == "ECDSA":
        signature = restored_private_key.sign(message_bytes, ec.ECDSA(hashes.SHA256()))
    else:
        raise ValueError("The only supported signature schemes are EdDSA and ECDSA.")

    # Convert signature to base64 string
    signature_b64 = base64.b64encode(signature).decode("utf-8")

    return {"signature": signature_b64}
