import logging
from os import environ

import boto3
import requests

log = logging.getLogger("config")


def get_execution_role():
    """
    Retrieve the IAM role ARN associated with the current execution context.
    """
    try:
        # Check if running inside SageMaker by attempting to access instance metadata
        response = requests.get('http://169.254.169.254/latest/meta-data/instance-id', timeout=1)
        instance_id = response.text

        # Initialize the SageMaker client
        sagemaker_client = boto3.client('sagemaker')

        # List all notebook instances
        response = sagemaker_client.list_notebook_instances()

        # Find the notebook instance with the matching instance ID
        notebook_instance_name = None
        for notebook_instance in response['NotebookInstances']:
            if notebook_instance['NotebookInstanceStatus'] == 'InService':
                instance_details = sagemaker_client.describe_notebook_instance(NotebookInstanceName=notebook_instance['NotebookInstanceName'])
                if instance_details['DirectInternetAccess'] == 'Enabled':
                    notebook_instance_name = notebook_instance['NotebookInstanceName']
                    break

        if notebook_instance_name is None:
            raise Exception("Notebook instance name not found")

        # Describe the notebook instance
        response = sagemaker_client.describe_notebook_instance(NotebookInstanceName=notebook_instance_name)

        # Extract the IAM role
        iam_role_arn = response['RoleArn']

    except requests.exceptions.RequestException:
        # If not running inside SageMaker, assume running on EC2
        ec2_client = boto3.client('ec2')

        # Describe the instance to get the IAM role
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        iam_role_arn = response['Reservations'][0]['Instances'][0]['IamInstanceProfile']['Arn']

    return iam_role_arn
        

def get_role() -> str:
    """
    Get the execution role. If there is an issue get the fallback role from env
    """
    try:
        # Try to get the execution role
        role = get_execution_role()
        log.info(f"Role is {role}")
    except Exception:
        # If getting the execution role fails, fallback to the IAM_ROLE environment variable
        role = environ.get("IAM_ROLE")
        log.info(f"Fallback to environment {role}")
    # Return the role
    return role


def log_to_file(path: str, level: int = logging.INFO) -> None:
    """
    Configures the logging module to log messages to a file and to the console.

    Parameters
    ----------
    path : str
        The path to the log file.
    level : int
        The minimum logging level. Default is logging.INFO.
    """
    # noinspection PyArgumentList
    logging.basicConfig(
        # Format of the log message
        format="%(asctime)s %(process)6d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        # Minimum logging level
        level=level,
        handlers=[
            # Handler for writing log messages to a file
            logging.FileHandler(filename=path, mode="a", encoding="utf-8", delay=False),
            # Handler for writing log messages to the console
            logging.StreamHandler(),  # sys.stderr by default, in case you want to test 2>/dev/null
        ],
    )
