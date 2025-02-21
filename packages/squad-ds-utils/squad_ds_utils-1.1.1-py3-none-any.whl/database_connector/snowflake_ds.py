"""
This module provides a database engine connection for the Snowflake database. It reads the username, password, and host
from AWS Parameter Store for better security.
This connection provides READ ONLY access to the Snowflake database.
"""
import json
import os
import re
from cryptography.hazmat.primitives import serialization
from database_connector.utils import get_parameters, get_secret_value
from database_connector.constants import (
    AWS_REGION,
    SAGEMAKER_RESOURCE_PATH,
    SNOWFLAKE_ACCOUNT_NAME_PARAMETER,
    SNOWFLAKE_WAREHOUSE_NAME_PARAMETER,
)
from snowflake import connector

#function to get user details from secrets manager
def get_user_details() -> str:
    """
    Get user profile for SageMaker access. First, check the metadata file.
    If it doesn't exist, fallback to the USER_PROFILE environment variable.
    
    :return: username
    """
    if os.path.exists(SAGEMAKER_RESOURCE_PATH):
        with open(SAGEMAKER_RESOURCE_PATH, 'r') as file:
            data = json.load(file)
        space_name = data.get('SpaceName')
        
        if space_name:
            match = re.match(r'^(.*?)-space(?:-[a-zA-Z0-9]+)?$', space_name)
            if match:
                return match.group(1)
    
    return os.getenv('USER_PROFILE')


def get_connection(database: str, schema: str):
    """
    makes connection with snowflake db
    :param database:
    :param schema:
    :param user:
    :return: connection
    """
    parameter_to_value_map = get_parameters((
        SNOWFLAKE_ACCOUNT_NAME_PARAMETER,
        SNOWFLAKE_WAREHOUSE_NAME_PARAMETER,
    ), AWS_REGION)

    account = parameter_to_value_map[SNOWFLAKE_ACCOUNT_NAME_PARAMETER]
    warehouse = parameter_to_value_map[SNOWFLAKE_WAREHOUSE_NAME_PARAMETER]
    profile_user = get_user_details()
    secrets = get_secret_value(f'snowflake/{profile_user}')
    password = secrets.get('password')
    username = secrets.get('username')
    private_key_secret = secrets.get("private_key")


    private_key = serialization.load_pem_private_key(
        private_key_secret.encode(),
        password=None
    )

    private_key_der = private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    if private_key_der:
        return connector.connect(
            user = username,
            private_key = private_key_der,
            account = account,
            warehouse = warehouse,
            database = database,
            schema = schema,
    )

    return connector.connect(
        user = username,
        password = password,
        account = account,
        warehouse = warehouse,
        database = database,
        schema = schema,
    )