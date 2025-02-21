
import subprocess
import json
from google.oauth2 import service_account

class DockerHelper():

    '''
    ----------------------------------------------------------------
    Description:
        - The following class can be used for all functions relevant
          docker 

    credential_file_path (str) - this parameter expects the path of
                                 the local credentials file that is 
                                 used to authenticate GCP.
        
    ----------------------------------------------------------------
    author: Thomas Verryne                Last Updated: 2025/02/11
    ----------------------------------------------------------------
    '''

    def __init__(self, credential_file_path: str):
        self.credentials = service_account.Credentials.from_service_account_file(credential_file_path)
        # self.client = storage.Client(credentials=self.credentials)
        return


    def build_docker_image(self, image_name: str, dockerfile: str):
        '''
        Description:
            - Builds a Docker image locally.

        Parameters:
            image_name (str): The name of the Docker image.
            dockerfile (str): The path to the Dockerfile.

        Example:
        >>> build_docker_image("data_loader", "data_loader.Dockerfile")
        '''
        image_tag = f"{image_name}:latest"

        docker_command = [
            "docker", "build", "-t", image_tag, "-f", dockerfile, "."
        ]

        print(f"Executing: {' '.join(docker_command)}")
        
        try:
            subprocess.run(docker_command, check=True)
            print(f"Successfully built {image_tag}")
        except subprocess.CalledProcessError as e:
            print(f"Docker build error: {e}")

