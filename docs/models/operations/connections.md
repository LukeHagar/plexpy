# Connections


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `protocol`                                                 | [operations.Protocol](../../models/operations/protocol.md) | :heavy_check_mark:                                         | The protocol used for the connection (http, https, etc)    |
| `address`                                                  | *str*                                                      | :heavy_check_mark:                                         | The (ip) address or domain name used for the connection    |
| `port`                                                     | *int*                                                      | :heavy_check_mark:                                         | The port used for the connection                           |
| `uri`                                                      | *str*                                                      | :heavy_check_mark:                                         | The full URI of the connection                             |
| `local`                                                    | *bool*                                                     | :heavy_check_mark:                                         | If the connection is local address                         |
| `relay`                                                    | *bool*                                                     | :heavy_check_mark:                                         | If the connection is relayed through plex.direct           |
| `i_pv6`                                                    | *bool*                                                     | :heavy_check_mark:                                         | If the connection is using IPv6                            |