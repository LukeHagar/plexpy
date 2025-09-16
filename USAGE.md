<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from plex_api_client import PlexAPI


with PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
) as plex_api:

    res = plex_api.server.get_server_capabilities()

    assert res.object is not None

    # Handle response
    print(res.object)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from plex_api_client import PlexAPI

async def main():

    async with PlexAPI(
        access_token="<YOUR_API_KEY_HERE>",
    ) as plex_api:

        res = await plex_api.server.get_server_capabilities_async()

        assert res.object is not None

        # Handle response
        print(res.object)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->