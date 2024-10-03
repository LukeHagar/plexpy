<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from plex_api_client import PlexAPI

s = PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
    client_name="Plex for Roku",
    client_version="2.4.1",
    platform="Roku",
    device_nickname="Roku 3",
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
        client_id="3381b62b-9ab7-4e37-827b-203e9809eb58",
        client_name="Plex for Roku",
        client_version="2.4.1",
        platform="Roku",
        device_nickname="Roku 3",
    )
    res = await s.server.get_server_capabilities_async()
    if res.object is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->