import hashlib
import requests
import time


class FileScanner():
    API_KEY = "ENTER_API_KEY"
    OPSWAT_URL = "https://api.metadefender.com/v4"

    def scan(self, file):
        request = {
            "url": f"{self.OPSWAT_URL}/file",
            "headers": {
                "apikey": self.API_KEY,
                "content-type": "application/octet-stream"
            },
            "data": None
        }
        file_bytes = None
        # open file as binary
        with open(file, "rb") as f:
            file_bytes = f.read()
            f.close()

        request["data"] = file_bytes
        response = requests.post(**request).json()

        if response.get("error"):
            raise Exception(response["error"]["messages"])

        request["url"] = f"{request['url']}/{response['data_id']}"

        # Hit API every 3 seconds until scan is done
        while response.get("status") == "inqueue":
            time.sleep(3)
            response = requests.get(**request).json()
            if response.get("error"):
                raise Exception(response["error"]["messages"])
        return response

    def hash(self, file):
        with open(file, "rb") as f:
            file_bytes = f.read()
            # Hash file using SHA-256
            readable_hash = hashlib.sha256(file_bytes).hexdigest()
            return readable_hash

    def hash_lookup(self, file_hash):
        request = {
            "url": f"{self.OPSWAT_URL}/hash/{file_hash}",
            "headers": {
                "apikey": self.API_KEY
            }
        }
        response = requests.get(**request).json()
        if response.get("error"):
            return None
        return response
