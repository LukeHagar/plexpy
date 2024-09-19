<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="gcgzw5rz2xovp84b4vha3a40",
    client_name="Plex Web",
    client_version="4.133.0",
    client_platform="Chrome",
    device_name="Linux",
)

res = s.server.get_server_capabilities()

if res.object is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from plex_api_client import PlexAPI

async def main():
    s = PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
        client_id="gcgzw5rz2xovp84b4vha3a40",
        client_name="Plex Web",
        client_version="4.133.0",
        client_platform="Chrome",
        device_name="Linux",
    )
    res = await s.server.get_server_capabilities_async()
    if res.object is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->