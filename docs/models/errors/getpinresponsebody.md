# GetPinResponseBody

Bad Request response when the X-Plex-Client-Identifier is missing


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `errors`                                                         | List[[errors.GetPinErrors](../../models/errors/getpinerrors.md)] | :heavy_minus_sign:                                               | N/A                                                              |
| `raw_response`                                                   | [httpx.Response](https://www.python-httpx.org/api/#response)     | :heavy_minus_sign:                                               | Raw HTTP response; suitable for custom response parsing          |