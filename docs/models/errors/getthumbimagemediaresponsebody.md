# GetThumbImageMediaResponseBody

Unauthorized - Returned if the X-Plex-Token is missing from the header or query.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `errors`                                                                                 | List[[errors.GetThumbImageMediaErrors](../../models/errors/getthumbimagemediaerrors.md)] | :heavy_minus_sign:                                                                       | N/A                                                                                      |
| `raw_response`                                                                           | [httpx.Response](https://www.python-httpx.org/api/#response)                             | :heavy_minus_sign:                                                                       | Raw HTTP response; suitable for custom response parsing                                  |