import requests
import os
import json
from .exceptions import AnofileError

def upload_file(file_path, domain):   
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            response = requests.post(f"https://{domain}/process/upload_file", files=files)

        if response.status_code != 200:
            raise AnofileError("Failed to upload file to Anonfile.")

        data = json.loads(response.text)
        
        if data["success"]:
            return data["url"]
            
        raise AnofileError("Not Found...")

    except requests.exceptions.RequestException as e:
        raise AnofileError(f"An error occurred: {str(e)}")
    finally:
        if isinstance(file_path, str):
            files['file'].close()
