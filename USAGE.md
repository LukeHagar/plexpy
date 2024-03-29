<!-- Start SDK Example Usage [usage] -->
```python
import plex_api

s = plex_api.PlexAPI(
    access_token="<YOUR_API_KEY_HERE>",
    x_plex_client_identifier='<value>',
)


res = s.server.get_server_capabilities()

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->