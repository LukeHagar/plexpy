# Feature


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `type`                                                                                               | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `key`                                                                                                | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `flavor`                                                                                             | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | global                                                                                               |
| `scrobble_key`                                                                                       | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | /:/scrobble/new                                                                                      |
| `unscrobble_key`                                                                                     | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | /:/unscrobble/new                                                                                    |
| `directory`                                                                                          | List[[operations.GetMediaProvidersDirectory](../../models/operations/getmediaprovidersdirectory.md)] | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |                                                                                                      |
| `action`                                                                                             | List[[operations.Action](../../models/operations/action.md)]                                         | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |                                                                                                      |