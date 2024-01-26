# UploadPlaylistResponseBody

Unauthorized - Returned if the X-Plex-Token is missing from the header or query.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `errors`                                                                              | List[[errors.UploadPlaylistErrors](../../models/errors/uploadplaylisterrors.md)]      | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |