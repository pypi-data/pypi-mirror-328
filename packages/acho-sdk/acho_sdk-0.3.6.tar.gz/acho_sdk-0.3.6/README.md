# README #

This package will serve as the programmatic interface between Acho and your python scripts

## Features

- Get data from Acho Project view
- Connect to an Acho Published App instance's eventing system
- Manage Media Assets on Acho

## Installing

**Package Manager**

```
$ pip install acho-sdk
```

```python
from acho import Project
```

## Example with Project Endpoints

**Initializing the Acho Client**

```python
project = Project()
```

The SDK will use the environment variables from your system

**_ACHO_PYTHON_SDK_TOKEN_**: The Acho develoepr API token

- If you are a current subscriber, retrieve it from your profile page
- If you want to try out the SDK without an active subscription, please [contact us](https://calendly.com/contact_acho/discovery-call)

**_ACHO_PYTHON_SDK_BASE_URL_**: The service backend you are connecting to

- Default to https://kube.acho.io
- This setting is irrelevant unless you subscribe to on-premise or dedicated server

If you prefer convenience in testing, you could also initialize the instance by passing in the variables in constructor

```python
project = Project(token=token, base_url=host)
```

> **Note:** It is not recommended to expose your API token in the code base, especially on production\
> If you suspect your token might be leaked, you can invalidate the token in your profile page, or report to [contact@acho.io](mailto:contact@acho.io)

---
