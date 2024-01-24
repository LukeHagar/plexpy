# GetTimelineRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `rating_key`                                         | *float*                                              | :heavy_check_mark:                                   | The rating key of the media item                     |
| `key`                                                | *str*                                                | :heavy_check_mark:                                   | The key of the media item to get the timeline for    |
| `state`                                              | [operations.State](../../models/operations/state.md) | :heavy_check_mark:                                   | The state of the media item                          |
| `has_mde`                                            | *float*                                              | :heavy_check_mark:                                   | Whether the media item has MDE                       |
| `time`                                               | *float*                                              | :heavy_check_mark:                                   | The time of the media item                           |
| `duration`                                           | *float*                                              | :heavy_check_mark:                                   | The duration of the media item                       |
| `context`                                            | *str*                                                | :heavy_check_mark:                                   | The context of the media item                        |
| `play_queue_item_id`                                 | *float*                                              | :heavy_check_mark:                                   | The play queue item ID of the media item             |
| `play_back_time`                                     | *float*                                              | :heavy_check_mark:                                   | The playback time of the media item                  |
| `row`                                                | *float*                                              | :heavy_check_mark:                                   | The row of the media item                            |