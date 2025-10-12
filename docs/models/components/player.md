# Player

Information about the player being used for playback


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `title`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | The title of the client                                     |
| `address`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | The remote address                                          |
| `local`                                                     | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Indicating if the client is playing from the local LAN      |
| `machine_identifier`                                        | *Optional[str]*                                             | :heavy_minus_sign:                                          | The identifier of the client                                |
| `model`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | The model of the client                                     |
| `platform`                                                  | *Optional[str]*                                             | :heavy_minus_sign:                                          | The platform of the client                                  |
| `platform_version`                                          | *Optional[str]*                                             | :heavy_minus_sign:                                          | The platformVersion of the client                           |
| `product`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | The product name of the client                              |
| `relayed`                                                   | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Indicating if the client is playing over a relay connection |
| `remote_public_address`                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | The client's public address                                 |
| `secure`                                                    | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Indicating if the client is playing over HTTPS              |
| `state`                                                     | *Optional[str]*                                             | :heavy_minus_sign:                                          | The client's last reported state                            |
| `user_id`                                                   | *Optional[int]*                                             | :heavy_minus_sign:                                          | The id of the user                                          |
| `vendor`                                                    | *Optional[str]*                                             | :heavy_minus_sign:                                          | The vendor of the client                                    |
| `version`                                                   | *Optional[str]*                                             | :heavy_minus_sign:                                          | The version of the client                                   |