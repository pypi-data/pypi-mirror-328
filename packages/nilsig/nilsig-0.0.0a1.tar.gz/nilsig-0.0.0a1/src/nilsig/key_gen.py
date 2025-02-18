"""Generating a signing key and storing it in nilDB"""

import uuid

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec, ed25519

from .nildb_api import data_upload
from .nilql_encryption import DataEncryption


async def key_gen(
    sign_scheme: str,
    nodes_and_jwts: list[dict],
    encryption: DataEncryption,
    schema_id: str,
) -> dict:
    """
    Generate keys for the specified signature scheme.

    Args:
        sign_scheme (str): Either "ECDSA" or "EdDSA"
        nodes_and_jwts (list): List of dicts with node info and JWTs
        encryption (DataEncryption): Encryption instance
        schema_id (str): Schema identifier

    Returns:
        dict: Contains store_id and list of node URLs

    Example of ``nodes_and_jwts`` input:

    .. code-block:: python

        [
            {
                "node_url": "https://nildb-a50d.nillion.network",
                "public_key": "XXXX",
                "jwt": "XXXX",
            },
            ...
        ]
    """
    # Generate key based on signature scheme
    if sign_scheme == "EdDSA":
        private_key = ed25519.Ed25519PrivateKey.generate()
    elif sign_scheme == "ECDSA":
        private_key = ec.generate_private_key(ec.SECP256K1())
    else:
        raise ValueError("The only supported signature schemes are EdDSA and ECDSA.")

    # Convert public key to PEM format
    public_key = private_key.public_key()
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("utf-8")

    # Convert private key to PEM format
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")

    # Generate store_id and encrypt shares
    store_id = str(uuid.uuid4())
    encrypted_shares = encryption.encrypt(pem_private_key)

    # Store shares across nodes
    success = True
    for i, node in enumerate(nodes_and_jwts):
        payload = {"_id": store_id, "key_share": encrypted_shares[i]}
        if not data_upload(node, schema_id, [payload]):
            success = False
            break

    if not success:
        raise RuntimeError(
            "Key generation failed. There was a problem storing the shares on SecretVault."
        )

    return {
        "store_id": store_id,
        "signature_public_key": pem_public_key,
        "nodes": [node["node_url"] for node in nodes_and_jwts],
    }
