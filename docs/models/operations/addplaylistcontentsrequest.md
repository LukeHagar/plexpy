# AddPlaylistContentsRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   | Example                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `playlist_id`                                                 | *float*                                                       | :heavy_check_mark:                                            | the ID of the playlist                                        |                                                               |
| `uri`                                                         | *str*                                                         | :heavy_check_mark:                                            | the content URI for the playlist                              | server://12345/com.plexapp.plugins.library/library/metadata/1 |
| `play_queue_id`                                               | *Optional[float]*                                             | :heavy_minus_sign:                                            | the play queue to add to a playlist                           | 123                                                           |