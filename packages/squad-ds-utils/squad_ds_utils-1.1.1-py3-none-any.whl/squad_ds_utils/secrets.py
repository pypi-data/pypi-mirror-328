import json
from typing import Dict
import time

import boto3
from botocore.exceptions import ClientError

from cachetools import cached, TTLCache

session = boto3.session.Session()
secrets_client = session.client(service_name='secretsmanager')


@cached(cache=TTLCache(maxsize=32, ttl=60))
def get_secret(secret_name: str) -> Dict[str, str]:

    try:
        get_secret_value_response = secrets_client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    return json.loads(get_secret_value_response['SecretString'])
