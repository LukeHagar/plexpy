# GetLibraryItemsRequest


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `section_id`                                          | *Any*                                                 | :heavy_check_mark:                                    | the Id of the library to query                        |                                                       |
| `tag`                                                 | [operations.Tag](../../models/operations/tag.md)      | :heavy_check_mark:                                    | A key representing a specific tag within the section. |                                                       |
| `include_guids`                                       | *Optional[int]*                                       | :heavy_minus_sign:                                    | Adds the Guids object to the response<br/>            | 1                                                     |