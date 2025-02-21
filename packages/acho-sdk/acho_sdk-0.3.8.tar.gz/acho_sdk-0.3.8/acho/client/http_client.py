import os
import asyncio
import requests
import socketio
import urllib

from typing import Optional, Union, Dict, Any, List

from .client_utils import _build_req_args, _get_url

# TODO: Add support for multipart/form-data

class HttpClient:
    BASE_URL = os.environ.get("ACHO_PYTHON_SDK_BASE_URL") or ""

    def __init__(self, token: Optional[str] = None, base_url = BASE_URL, timeout = 30):
        self.token = None if token is None else token.strip()
        """A JWT Token"""
        self.base_url = base_url
        """A string representing the Acho API base URL.
        Default is `'https://kube.acho.io'`."""
        self.timeout = timeout
        """The maximum number of seconds client staying alive"""
        self.default_params = {}

    async def identify(self):
        return await self.call_api(path="/auth/identify", http_method="GET")

    async def call_api(self, path, http_method: str = "POST", params: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        auth: Optional[dict] = None) -> Any:

        api_url = _get_url(self.base_url, path)

        if auth is not None:
            if isinstance(auth, dict):
                if headers is None:
                    headers = {}
                headers["Authorization"] = '{} {}'.format(auth.token_type, auth.token)
        else:
            headers = {}
            headers["Content-Type"] = 'application/json;charset=utf-8'
            headers["Authorization"] = 'jwt {}'.format(self.token)

        headers = headers or {}
        
        req_args = _build_req_args(
            token=self.token,
            http_method=http_method,
            default_params=self.default_params,
            params=params,
            json=json,
            headers=headers,
            auth=auth,
        )

        req_result = await self._send(
            http_method=http_method,
            api_url=api_url,
            req_args=req_args,
        )
        response = req_result[0]
        metadata = req_result[1]
        if response.status_code >= 400:
            raise Exception(f"Request failed with status code {response.status_code} and message {response.text}")
        else:
            try:
                return response.json()
            except Exception as e:
                return response.text
            
    async def stream_api(self, path, http_method: str = "POST", params: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        auth: Optional[dict] = None) -> Any:

        api_url = _get_url(self.base_url, path)

        if auth is not None:
            if isinstance(auth, dict):
                if headers is None:
                    headers = {}
                headers["Authorization"] = '{} {}'.format(auth.token_type, auth.token)
        else:
            headers = {}
            headers["Content-Type"] = 'application/json;charset=utf-8'
            headers["Authorization"] = 'jwt {}'.format(self.token)

        headers = headers or {}
        
        req_args = _build_req_args(
            token=self.token,
            http_method=http_method,
            default_params=self.default_params,
            params=params,
            json=json,
            headers=headers,
            auth=auth,
        )
        if (http_method == "GET"):
            stream = requests.get(url=api_url, headers=req_args.get('headers'), params=req_args.get('params'), stream=True)
            return stream
        elif (http_method == "POST"):
            stream = requests.post(url=api_url, headers=req_args.get('headers'), params=req_args.get('params'), json=req_args.get('json'), stream=True)
            return stream
        else:
            raise Exception("Unsupported HTTP method")
        

    async def _send(self, http_method: str, api_url: str, req_args: dict) -> Any:
        """Sends the request out for transmission.
        Args:
            http_verb (str): The HTTP verb. e.g. 'GET' or 'POST'.
            api_url (str): The Acho API url'
            req_args (dict): The request arguments to be attached to the request.
            e.g.
            {
                json: {
                    'attachments': [{"pretext": "pre-hello", "text": "text-world"}],
                    'channel': '#random'
                }
            }
        """

        res = {}
        
        # print(req_args)
        # print(http_method)

        if (http_method == "GET"):
            res = requests.get(url=api_url, headers=req_args.get('headers'), params=req_args.get('params'))
        elif (http_method == "POST"):
            res = requests.post(url=api_url, headers=req_args.get('headers'), params=req_args.get('params'), json=req_args.get('json'))
        data = {
            "client": self,
            "http_method": http_method,
            "api_url": api_url,
            "req_args": req_args,
        }
        return (res, data)