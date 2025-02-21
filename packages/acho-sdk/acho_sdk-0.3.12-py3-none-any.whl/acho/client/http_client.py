import os
import asyncio
import requests
import socketio
import urllib
from requests_toolbelt.multipart.encoder import MultipartEncoder

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

    async def call_api(
        self,
        path,
        http_method: str = "POST",
        params: Optional[dict] = None,
        json: Optional[dict] = None,
        form_data: Optional["aiohttp.FormData"] = None,  # Expected to be an instance of aiohttp.FormData
        headers: Optional[dict] = None,
        auth: Optional[dict] = None,
    ) -> Any:
        api_url = _get_url(self.base_url, path)

        # Ensure that both json and form_data are not provided simultaneously.
        if json is not None and form_data is not None:
            raise ValueError("Cannot provide both json and form_data payloads.")

        headers = headers or {}

        # Set the authorization header.
        if auth is not None:
            if isinstance(auth, dict):
                headers["Authorization"] = '{} {}'.format(auth.token_type, auth.token)
        else:
            headers.setdefault("Authorization", 'jwt {}'.format(self.token))

        # Set Content-Type header based on the payload type.
        if json is not None:
            headers.setdefault("Content-Type", "application/json;charset=utf-8")
        elif form_data is not None:
            # Remove any preset Content-Type so aiohttp can set it (with the proper boundary)
            headers.pop("Content-Type", None)

        # Build the request arguments using _build_req_args.
        # Note that _build_req_args does not accept a "data" parameter, so we only pass json.
        req_args = _build_req_args(
            token=self.token,
            http_method=http_method,
            default_params=self.default_params,
            params=params,
            json=json,
            headers=headers,
            auth=auth,
        )

        # If multipart form data was provided, inject it into the request arguments.
        if form_data is not None:
            req_args["data"] = form_data

        req_result = await self._send(
            http_method=http_method,
            api_url=api_url,
            req_args=req_args,
        )
        response, metadata = req_result

        if response.status_code >= 400:
            raise Exception(
                f"Request failed with status code {response.status_code} and message {response.text}"
            )
        try:
            return response.json()
        except Exception:
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
        """
        Sends the request out for transmission.

        Args:
            http_method (str): The HTTP verb, e.g. 'GET' or 'POST'.
            api_url (str): The API URL.
            req_args (dict): The request arguments, for example:
                {
                    "json": {...},
                    "headers": {...},
                    "params": {...},
                    # Optionally for multipart data:
                    "data": <aiohttp.FormData instance>
                }
        """
        # Debug output.
        print(req_args)
        print(http_method)

        if http_method == "GET":
            res = requests.get(
                url=api_url,
                headers=req_args.get("headers"),
                params=req_args.get("params")
            )
        elif http_method == "POST":
            # Check if a multipart payload was provided.
            if req_args.get("data") is not None:
                # Extract the aiohttp.FormData instance.
                form_data = req_args.pop("data")
                # Convert the aiohttp.FormData instance to a dictionary of fields.
                # Note: This uses the internal _fields attribute. Each field is a tuple
                # typically in the form: (name, value, content_type, headers).
                # For simplicity, we assume no duplicate field names.
                fields = {}
                for field in form_data._fields:
                    if len(field) >= 2:
                        name, value = field[0], field[1]
                        fields[name] = value

                # Create a MultipartEncoder with the extracted fields.
                encoder = MultipartEncoder(fields=fields)
                # Ensure headers exist and set the Content-Type to the encoder's value (which includes the boundary).
                req_headers = req_args.get("headers", {})
                req_headers["Content-Type"] = encoder.content_type
                req_args["headers"] = req_headers

                res = requests.post(
                    url=api_url,
                    headers=req_args.get("headers"),
                    params=req_args.get("params"),
                    data=encoder
                )
            else:
                res = requests.post(
                    url=api_url,
                    headers=req_args.get("headers"),
                    params=req_args.get("params"),
                    json=req_args.get("json")
                )
        else:
            raise ValueError(f"HTTP method {http_method} not supported.")

        meta = {
            "client": self,
            "http_method": http_method,
            "api_url": api_url,
            "req_args": req_args,
        }
        return (res, meta)