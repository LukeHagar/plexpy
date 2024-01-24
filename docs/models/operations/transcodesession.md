# TranscodeSession


## Fields

| Field                    | Type                     | Required                 | Description              | Example                  |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| `key`                    | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | vv3i2q2lax92qlzul1hbd4bx |
| `throttled`              | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      | false                    |
| `complete`               | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      | false                    |
| `progress`               | *Optional[float]*        | :heavy_minus_sign:       | N/A                      | 1.7999999523162842       |
| `size`                   | *Optional[int]*          | :heavy_minus_sign:       | N/A                      | -22                      |
| `speed`                  | *Optional[float]*        | :heavy_minus_sign:       | N/A                      | 25.100000381469727       |
| `error`                  | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      | false                    |
| `duration`               | *Optional[int]*          | :heavy_minus_sign:       | N/A                      | 1445695                  |
| `remaining`              | *Optional[int]*          | :heavy_minus_sign:       | N/A                      | 53                       |
| `context`                | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | streaming                |
| `source_video_codec`     | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | h264                     |
| `source_audio_codec`     | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | aac                      |
| `video_decision`         | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | transcode                |
| `audio_decision`         | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | transcode                |
| `subtitle_decision`      | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | burn                     |
| `protocol`               | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | http                     |
| `container`              | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | mkv                      |
| `video_codec`            | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | h264                     |
| `audio_codec`            | *Optional[str]*          | :heavy_minus_sign:       | N/A                      | opus                     |
| `audio_channels`         | *Optional[int]*          | :heavy_minus_sign:       | N/A                      | 1                        |
| `transcode_hw_requested` | *Optional[bool]*         | :heavy_minus_sign:       | N/A                      | true                     |
| `time_stamp`             | *Optional[float]*        | :heavy_minus_sign:       | N/A                      | 1.7058958054919229e+09   |
| `max_offset_available`   | *Optional[float]*        | :heavy_minus_sign:       | N/A                      | 29.53                    |
| `min_offset_available`   | *Optional[float]*        | :heavy_minus_sign:       | N/A                      | 3.003000020980835        |