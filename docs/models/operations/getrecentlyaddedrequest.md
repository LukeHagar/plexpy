# GetRecentlyAddedRequest


## Fields

| Field                                                                                                                                                                                     | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               | Example                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content_directory_id`                                                                                                                                                                    | *int*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The content directory ID.                                                                                                                                                                 |                                                                                                                                                                                           |
| `type`                                                                                                                                                                                    | [operations.Type](../../models/operations/type.md)                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                        | The type of media to retrieve.<br/>1 = movie<br/>2 = show<br/>3 = season<br/>4 = episode<br/>E.g. A movie library will not return anything with type 3 as there are no seasons for movie libraries<br/> | 2                                                                                                                                                                                         |
| `pinned_content_directory_id`                                                                                                                                                             | *Optional[str]*                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                        | Comma-separated list of pinned content directory IDs.                                                                                                                                     |                                                                                                                                                                                           |
| `section_id`                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                        | The library section ID for filtering content.                                                                                                                                             | 2                                                                                                                                                                                         |
| `include_meta`                                                                                                                                                                            | [Optional[operations.IncludeMeta]](../../models/operations/includemeta.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                        | Adds the Meta object to the response<br/>                                                                                                                                                 | 1                                                                                                                                                                                         |
| `x_plex_container_start`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                        | The index of the first item to return. If not specified, the first item will be returned.<br/>If the number of items exceeds the limit, the response will be paginated.<br/>By default this is 0<br/> | 0                                                                                                                                                                                         |
| `x_plex_container_size`                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                        | The number of items to return. If not specified, all items will be returned.<br/>If the number of items exceeds the limit, the response will be paginated.<br/>By default this is 50<br/> | 50                                                                                                                                                                                        |