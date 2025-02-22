# sabnzbd-api

`sabnzbd-api` is a lightweight and easy-to-use Python library that simplifies interactions with the SABnzbd API. It provides a convenient way to integrate SABnzbd functionality into your Python applications, allowing you to manage and automate NZB downloads programmatically.

## Features

- Authenticate using your API key.
- Access SABnzbd's API endpoints with minimal setup.
- Includes All Functionalities

This project was inspired by and built upon the work of **anasty17**

## Installation

Install the library using pip:

```bash
pip install sabnzbd-api
```

## Usage

Here's a quick example of how to use the library:

```python
from sabnzbd_api import SabnzbdClient

nzb_file = "file.nzb"

client = SabnzbdClient(host="http://localhost", api_key="your_api_key")

add_nzb = client.add_uri(file=nzb_file)

progress = client.get_downloads(nzo_ids=add_nzb.get("nzo_ids")[0])

print(progress)

client.close()
```

## Requirements

- Python 3.6+

## Credits

This package was inspired by and built upon the work of **anasty17**.
