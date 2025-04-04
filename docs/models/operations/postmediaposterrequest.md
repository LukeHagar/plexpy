# PostMediaPosterRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `rating_key`                                                       | *int*                                                              | :heavy_check_mark:                                                 | the id of the library item to return the posters of.               | 2268                                                               |
| `url`                                                              | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | The URL of the image, if uploading a remote image                  | https://api.mediux.pro/assets/fcfdc487-dd07-4993-a0c1-0a3015362e5b |
| `request_body`                                                     | *Optional[Union[bytes, IO[bytes], io.BufferedReader]]*             | :heavy_minus_sign:                                                 | The contents of the image, if uploading a local file               |                                                                    |