# PostUsersSignInDataAuthenticationSubscription


## Fields

| Field                                                                                                                                              | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        | Example                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `features`                                                                                                                                         | List[[operations.PostUsersSignInDataAuthenticationFeatures](../../models/operations/postuserssignindataauthenticationfeatures.md)]                 | :heavy_minus_sign:                                                                                                                                 | List of features allowed on your Plex Pass subscription                                                                                            |                                                                                                                                                    |
| `active`                                                                                                                                           | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | If the account's Plex Pass subscription is active                                                                                                  | true                                                                                                                                               |
| `subscribed_at`                                                                                                                                    | *OptionalNullable[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                                 | Date the account subscribed to Plex Pass                                                                                                           | 2021-04-12T18:21:12Z                                                                                                                               |
| `status`                                                                                                                                           | [Optional[operations.PostUsersSignInDataAuthenticationResponseStatus]](../../models/operations/postuserssignindataauthenticationresponsestatus.md) | :heavy_minus_sign:                                                                                                                                 | String representation of subscriptionActive                                                                                                        | Inactive                                                                                                                                           |
| `payment_service`                                                                                                                                  | *OptionalNullable[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                                 | Payment service used for your Plex Pass subscription                                                                                               |                                                                                                                                                    |
| `plan`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                                 | Name of Plex Pass subscription plan                                                                                                                |                                                                                                                                                    |