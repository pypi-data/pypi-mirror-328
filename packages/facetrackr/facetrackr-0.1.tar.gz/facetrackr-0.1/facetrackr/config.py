import boto3
import os
from botocore.exceptions import NoCredentialsError

def get_aws_client(service_name="rekognition"):
    """
    Returns an AWS service client using the environment credentials.
    """
    try:
        client = boto3.client(
            service_name,
            region_name="us-east-2",
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        return client
    except NoCredentialsError:
        print("AWS credentials not found. Please configure them.")
        raise
