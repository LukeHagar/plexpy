# GetTopWatchedContentRequest


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         | Example                                             |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `type`                                              | *int*                                               | :heavy_check_mark:                                  | the library type (1 - movies, 2 - shows, 3 - music) |                                                     |
| `include_guids`                                     | *Optional[int]*                                     | :heavy_minus_sign:                                  | Adds the Guids object to the response<br/>          | 1                                                   |