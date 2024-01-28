# StartUniversalTranscodeRequest


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `has_mde`                                     | *float*                                       | :heavy_check_mark:                            | Whether the media item has MDE                |
| `path`                                        | *str*                                         | :heavy_check_mark:                            | The path to the media item to transcode       |
| `media_index`                                 | *float*                                       | :heavy_check_mark:                            | The index of the media item to transcode      |
| `part_index`                                  | *float*                                       | :heavy_check_mark:                            | The index of the part to transcode            |
| `protocol`                                    | *str*                                         | :heavy_check_mark:                            | The protocol to use for the transcode session |
| `fast_seek`                                   | *Optional[float]*                             | :heavy_minus_sign:                            | Whether to use fast seek or not               |
| `direct_play`                                 | *Optional[float]*                             | :heavy_minus_sign:                            | Whether to use direct play or not             |
| `direct_stream`                               | *Optional[float]*                             | :heavy_minus_sign:                            | Whether to use direct stream or not           |
| `subtitle_size`                               | *Optional[float]*                             | :heavy_minus_sign:                            | The size of the subtitles                     |
| `subtites`                                    | *Optional[str]*                               | :heavy_minus_sign:                            | The subtitles                                 |
| `audio_boost`                                 | *Optional[float]*                             | :heavy_minus_sign:                            | The audio boost                               |
| `location`                                    | *Optional[str]*                               | :heavy_minus_sign:                            | The location of the transcode session         |
| `media_buffer_size`                           | *Optional[float]*                             | :heavy_minus_sign:                            | The size of the media buffer                  |
| `session`                                     | *Optional[str]*                               | :heavy_minus_sign:                            | The session ID                                |
| `add_debug_overlay`                           | *Optional[float]*                             | :heavy_minus_sign:                            | Whether to add a debug overlay or not         |
| `auto_adjust_quality`                         | *Optional[float]*                             | :heavy_minus_sign:                            | Whether to auto adjust quality or not         |