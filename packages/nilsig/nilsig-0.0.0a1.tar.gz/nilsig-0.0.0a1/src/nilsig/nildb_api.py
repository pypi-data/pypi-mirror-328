"""API utilities for interfacing with nilDB for secure storage"""

from typing import Dict, List, Optional

import requests


def data_upload(node: dict, schema_id: str, payload: list) -> bool:
    """
    Create/upload records in the specified node and schema.

    Args:
        node (dict): Node information with URL and JWT
        schema_id (str): Schema identifier
        payload (list): Data to upload

    Returns:
        bool: True if upload successful, False otherwise
    """
    try:
        headers = {
            "Authorization": f'Bearer {node["jwt"]}',
            "Content-Type": "application/json",
        }

        body = {"schema": schema_id, "data": payload}

        response = requests.post(  # pylint: disable=missing-timeout
            url=f"{node['node_url']}/api/v1/data/create",
            headers=headers,
            json=body,
        )

        return (
            response.status_code == 200
            and response.json().get("data", {}).get("errors", []) == []
        )
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error creating records in {node['node_url']}: {str(e)}")
        return False


def data_read(
    node: dict, schema_id: str, filter_dict: Optional[dict] = None
) -> List[Dict]:
    """
    Read data from the specified node and schema.

    Args:
        node (dict): Node information with URL and JWT
        schema_id (str): Schema identifier
        filter_dict (Optional[dict]): Optional filter criteria

    Returns:
        List[Dict]: List of matching records
    """
    try:
        headers = {
            "Authorization": f'Bearer {node["jwt"]}',
            "Content-Type": "application/json",
        }

        body = {
            "schema": schema_id,
            "filter": filter_dict if filter_dict is not None else {},
        }

        response = requests.post(  # pylint: disable=missing-timeout
            url=f"{node['node_url']}/api/v1/data/read",
            headers=headers,
            json=body,
        )

        if response.status_code == 200:
            return response.json().get("data", [])
        return []
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error reading data from {node['node_url']}: {str(e)}")
        return []


def query_execute(
    node: dict, query_id: str, variables: Optional[dict] = None
) -> List[Dict]:
    """
    Execute a query on the specified node with advanced filtering.

    Args:
        node (dict): Node information with URL and JWT
        query_id (str): Query identifier
        variables (Optional[dict]): Optional query variables

    Returns:
        List[Dict]: Query results
    """
    try:
        headers = {
            "Authorization": f'Bearer {node["jwt"]}',
            "Content-Type": "application/json",
        }

        payload = {
            "id": query_id,
            "variables": variables if variables is not None else {},
        }

        response = requests.post(  # pylint: disable=missing-timeout
            url=f"{node['node_url']}/api/v1/queries/execute",
            headers=headers,
            json=payload,
        )

        if response.status_code == 200:
            return response.json().get("data", [])
        return []
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error executing query on {node['node_url']}: {str(e)}")
        return []
