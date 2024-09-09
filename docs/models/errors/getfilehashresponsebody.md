# GetFileHashResponseBody

Bad Request - A parameter was not specified, or was specified incorrectly.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `errors`                                                                   | List[[errors.GetFileHashErrors](../../models/errors/getfilehasherrors.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |
| `raw_response`                                                             | [httpx.Response](https://www.python-httpx.org/api/#response)               | :heavy_minus_sign:                                                         | Raw HTTP response; suitable for custom response parsing                    |