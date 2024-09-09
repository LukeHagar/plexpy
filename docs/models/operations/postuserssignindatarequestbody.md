# PostUsersSignInDataRequestBody

Login credentials


## Fields

| Field               | Type                | Required            | Description         | Example             |
| ------------------- | ------------------- | ------------------- | ------------------- | ------------------- |
| `login`             | *str*               | :heavy_check_mark:  | N/A                 | username@email.com  |
| `password`          | *str*               | :heavy_check_mark:  | N/A                 | password123         |
| `remember_me`       | *Optional[bool]*    | :heavy_minus_sign:  | N/A                 |                     |
| `verification_code` | *Optional[str]*     | :heavy_minus_sign:  | N/A                 | 123456              |