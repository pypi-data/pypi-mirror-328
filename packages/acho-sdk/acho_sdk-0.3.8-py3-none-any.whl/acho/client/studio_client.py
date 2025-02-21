import asyncio
import logging
import os
import aiohttp
import aiofiles
from typing import Optional

from .http_client import HttpClient

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

ACHO_TOKEN = os.environ.get("ACHO_PYTHON_SDK_TOKEN") or ""
BASE_URL = os.environ.get("ACHO_PYTHON_SDK_BASE_URL") or ""
ACHO_CLIENT_TIMEOUT = 30

class Acho():

    def __init__(self, token: Optional[str] = ACHO_TOKEN, base_url = BASE_URL, timeout = ACHO_CLIENT_TIMEOUT):
        self.http = HttpClient(token=token, base_url=base_url, timeout=timeout)
        return
    
    def __str__(self):
        return "Acho Python SDK"
    

class AssetManager():

    def __init__(self, path = '', token: Optional[str] = ACHO_TOKEN, base_url = BASE_URL, timeout = ACHO_CLIENT_TIMEOUT):
        self.http = HttpClient(token=token, base_url=base_url, timeout=timeout)
        self.path = path
        return

    def redirect(self, path):
        self.path = path

    async def list(self, options = {}):
        payload = {
            'path': self.path,
            'depth': options.get('depth', 1),
            'options': options,
        }
        result = await self.http.call_api(path=f"/uploaded/search", http_method="POST", json=payload)
        return result

    async def upload(self, options={}):
        # URL query parameters
        params = {
            'destination': self.path,
            'public': options.get('public', 'true'),
        }
        
        # Build the multipart form-data payload for files only
        form = aiohttp.FormData()
        
        # Expecting a list of file paths under the key "files" in options
        file_paths = options.get("files")
        if not file_paths:
            raise ValueError("Missing 'files' in options, expected a list of file paths")
        
        # Ensure file_paths is a list; if a single file path is provided, convert it to a list
        if not isinstance(file_paths, list):
            file_paths = [file_paths]
        
        # Iterate over each file path and add it to the form-data under the key "files"
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            async with aiofiles.open(file_path, 'rb') as f:
                file_content = await f.read()
            
            form.add_field(
                'files',  # Key expected by the API for files
                file_content,
                filename=file_name,
                content_type='application/octet-stream'  # Update MIME type if necessary
            )
        
        # Call the API with query parameters and form-data containing the files
        result = await self.http.call_api(
            path="/uploaded/file/upload",
            http_method="POST",
            params=params,
            data=form
        )
        
        return result
    
    async def download(self, filename, options = {}, destination = os.getcwd()):
        payload = {
            'file': { 'path': os.path.join(self.path, filename) },
            'options': options,
        }
        # Save file stream to storage / memory
        http_stream = await self.http.stream_api(path=f"/uploaded/file/download", http_method="POST", json=payload)
        if not os.path.exists(destination):
            os.makedirs(destination)
        destination_path = os.path.join(destination, filename)
        with open(destination_path, 'wb') as f:
            for chunk in http_stream.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return destination_path

    async def get_url(self, filename, options = {}):
        payload = {
            'file': { 'path': self.path + filename },
            'options': options,
        }
        result = await self.http.call_api(path=f"/uploaded/file/get-link", http_method="POST", json=payload)
        return result

