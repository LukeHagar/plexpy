# GetServerIdentityRequestTimeout

Request Timeout


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `code`                                                       | *Optional[int]*                                              | :heavy_minus_sign:                                           | N/A                                                          | 408                                                          |
| `message`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          | The server timed out waiting for the request.                |
| `raw_response`                                               | [httpx.Response](https://www.python-httpx.org/api/#response) | :heavy_minus_sign:                                           | Raw HTTP response; suitable for custom response parsing      |                                                              |