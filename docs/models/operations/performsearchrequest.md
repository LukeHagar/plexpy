# PerformSearchRequest


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `query`                                                                               | *str*                                                                                 | :heavy_check_mark:                                                                    | The query term                                                                        | arnold                                                                                |
| `section_id`                                                                          | *Optional[float]*                                                                     | :heavy_minus_sign:                                                                    | This gives context to the search, and can result in re-ordering of search result hubs |                                                                                       |
| `limit`                                                                               | *Optional[float]*                                                                     | :heavy_minus_sign:                                                                    | The number of items to return per hub                                                 | 5                                                                                     |