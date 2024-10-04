"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import httpx
from plex_api_client.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict

GET_TOKEN_DETAILS_SERVERS = [
    "https://plex.tv/api/v2",
]


class MailingListStatus(str, Enum):
    r"""Your current mailing list status (active or unsubscribed)"""

    ACTIVE = "active"
    UNSUBSCRIBED = "unsubscribed"


class AutoSelectSubtitle(int, Enum):
    r"""The auto-select subtitle mode (0 = Manually selected, 1 = Shown with foreign audio, 2 = Always enabled)"""

    DISABLE = 0
    ENABLE = 1


class DefaultSubtitleAccessibility(int, Enum):
    r"""The subtitles for the deaf or hard-of-hearing (SDH) searches mode (0 = Prefer non-SDH subtitles, 1 = Prefer SDH subtitles, 2 = Only show SDH subtitles, 3 = Only show non-SDH subtitles)"""

    DISABLE = 0
    ENABLE = 1


class DefaultSubtitleForced(int, Enum):
    r"""The forced subtitles searches mode (0 = Prefer non-forced subtitles, 1 = Prefer forced subtitles, 2 = Only show forced subtitles, 3 = Only show non-forced subtitles)"""

    DISABLE = 0
    ENABLE = 1


class WatchedIndicator(int, Enum):
    r"""Whether or not media watched indicators are enabled (little orange dot on media)"""

    DISABLE = 0
    ENABLE = 1


class MediaReviewsVisibility(int, Enum):
    r"""Whether or not the account has media reviews visibility enabled"""

    DISABLE = 0
    ENABLE = 1


class UserProfileTypedDict(TypedDict):
    default_audio_language: Nullable[str]
    r"""The preferred audio language for the account"""
    default_subtitle_language: Nullable[str]
    r"""The preferred subtitle language for the account"""
    auto_select_audio: NotRequired[bool]
    r"""If the account has automatically select audio and subtitle tracks enabled"""
    auto_select_subtitle: NotRequired[AutoSelectSubtitle]
    default_subtitle_accessibility: NotRequired[DefaultSubtitleAccessibility]
    default_subtitle_forced: NotRequired[DefaultSubtitleForced]
    watched_indicator: NotRequired[WatchedIndicator]
    media_reviews_visibility: NotRequired[MediaReviewsVisibility]


class UserProfile(BaseModel):
    default_audio_language: Annotated[
        Nullable[str], pydantic.Field(alias="defaultAudioLanguage")
    ]
    r"""The preferred audio language for the account"""

    default_subtitle_language: Annotated[
        Nullable[str], pydantic.Field(alias="defaultSubtitleLanguage")
    ]
    r"""The preferred subtitle language for the account"""

    auto_select_audio: Annotated[
        Optional[bool], pydantic.Field(alias="autoSelectAudio")
    ] = True
    r"""If the account has automatically select audio and subtitle tracks enabled"""

    auto_select_subtitle: Annotated[
        Optional[AutoSelectSubtitle], pydantic.Field(alias="autoSelectSubtitle")
    ] = AutoSelectSubtitle.DISABLE

    default_subtitle_accessibility: Annotated[
        Optional[DefaultSubtitleAccessibility],
        pydantic.Field(alias="defaultSubtitleAccessibility"),
    ] = DefaultSubtitleAccessibility.DISABLE

    default_subtitle_forced: Annotated[
        Optional[DefaultSubtitleForced], pydantic.Field(alias="defaultSubtitleForced")
    ] = DefaultSubtitleForced.DISABLE

    watched_indicator: Annotated[
        Optional[WatchedIndicator], pydantic.Field(alias="watchedIndicator")
    ] = WatchedIndicator.DISABLE

    media_reviews_visibility: Annotated[
        Optional[MediaReviewsVisibility], pydantic.Field(alias="mediaReviewsVisibility")
    ] = MediaReviewsVisibility.DISABLE

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "autoSelectAudio",
            "autoSelectSubtitle",
            "defaultSubtitleAccessibility",
            "defaultSubtitleForced",
            "watchedIndicator",
            "mediaReviewsVisibility",
        ]
        nullable_fields = ["defaultAudioLanguage", "defaultSubtitleLanguage"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetTokenDetailsStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"


class ServicesTypedDict(TypedDict):
    identifier: str
    endpoint: str
    token: Nullable[str]
    secret: Nullable[str]
    status: GetTokenDetailsStatus


class Services(BaseModel):
    identifier: str

    endpoint: str

    token: Nullable[str]

    secret: Nullable[str]

    status: GetTokenDetailsStatus

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["token", "secret"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetTokenDetailsAuthenticationStatus(str, Enum):
    r"""String representation of subscriptionActive"""

    INACTIVE = "Inactive"
    ACTIVE = "Active"


class SubscriptionTypedDict(TypedDict):
    r"""If the account’s Plex Pass subscription is active"""

    features: NotRequired[List[str]]
    r"""List of features allowed on your Plex Pass subscription"""
    active: NotRequired[bool]
    r"""If the account's Plex Pass subscription is active"""
    subscribed_at: NotRequired[Nullable[str]]
    r"""Date the account subscribed to Plex Pass"""
    status: NotRequired[GetTokenDetailsAuthenticationStatus]
    r"""String representation of subscriptionActive"""
    payment_service: NotRequired[Nullable[str]]
    r"""Payment service used for your Plex Pass subscription"""
    plan: NotRequired[Nullable[str]]
    r"""Name of Plex Pass subscription plan"""


class Subscription(BaseModel):
    r"""If the account’s Plex Pass subscription is active"""

    features: Optional[List[str]] = None
    r"""List of features allowed on your Plex Pass subscription"""

    active: Optional[bool] = None
    r"""If the account's Plex Pass subscription is active"""

    subscribed_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="subscribedAt")
    ] = UNSET
    r"""Date the account subscribed to Plex Pass"""

    status: Optional[GetTokenDetailsAuthenticationStatus] = None
    r"""String representation of subscriptionActive"""

    payment_service: Annotated[
        OptionalNullable[str], pydantic.Field(alias="paymentService")
    ] = UNSET
    r"""Payment service used for your Plex Pass subscription"""

    plan: OptionalNullable[str] = UNSET
    r"""Name of Plex Pass subscription plan"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "features",
            "active",
            "subscribedAt",
            "status",
            "paymentService",
            "plan",
        ]
        nullable_fields = ["subscribedAt", "paymentService", "plan"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetTokenDetailsAuthenticationResponseStatus(str, Enum):
    r"""String representation of subscriptionActive"""

    INACTIVE = "Inactive"
    ACTIVE = "Active"


class GetTokenDetailsSubscriptionTypedDict(TypedDict):
    features: NotRequired[List[str]]
    r"""List of features allowed on your Plex Pass subscription"""
    active: NotRequired[bool]
    r"""If the account's Plex Pass subscription is active"""
    subscribed_at: NotRequired[Nullable[str]]
    r"""Date the account subscribed to Plex Pass"""
    status: NotRequired[GetTokenDetailsAuthenticationResponseStatus]
    r"""String representation of subscriptionActive"""
    payment_service: NotRequired[Nullable[str]]
    r"""Payment service used for your Plex Pass subscription"""
    plan: NotRequired[Nullable[str]]
    r"""Name of Plex Pass subscription plan"""


class GetTokenDetailsSubscription(BaseModel):
    features: Optional[List[str]] = None
    r"""List of features allowed on your Plex Pass subscription"""

    active: Optional[bool] = None
    r"""If the account's Plex Pass subscription is active"""

    subscribed_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="subscribedAt")
    ] = UNSET
    r"""Date the account subscribed to Plex Pass"""

    status: Optional[GetTokenDetailsAuthenticationResponseStatus] = None
    r"""String representation of subscriptionActive"""

    payment_service: Annotated[
        OptionalNullable[str], pydantic.Field(alias="paymentService")
    ] = UNSET
    r"""Payment service used for your Plex Pass subscription"""

    plan: OptionalNullable[str] = UNSET
    r"""Name of Plex Pass subscription plan"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "features",
            "active",
            "subscribedAt",
            "status",
            "paymentService",
            "plan",
        ]
        nullable_fields = ["subscribedAt", "paymentService", "plan"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetTokenDetailsUserPlexAccountTypedDict(TypedDict):
    r"""Logged in user details"""

    ads_consent: Nullable[bool]
    r"""Unknown"""
    ads_consent_reminder_at: Nullable[int]
    ads_consent_set_at: Nullable[int]
    auth_token: str
    r"""The account token"""
    country: str
    r"""The account country"""
    email: str
    r"""The account email address"""
    friendly_name: str
    r"""Your account full name"""
    entitlements: List[str]
    r"""List of devices your allowed to use with this account"""
    home_size: int
    r"""The number of accounts in the Plex Home"""
    id: int
    r"""The Plex account ID"""
    joined_at: int
    r"""Unix epoch datetime in seconds"""
    locale: Nullable[str]
    r"""The account locale"""
    mailing_list_status: MailingListStatus
    r"""Your current mailing list status (active or unsubscribed)"""
    max_home_size: int
    r"""The maximum number of accounts allowed in the Plex Home"""
    profile: UserProfileTypedDict
    remember_expires_at: int
    r"""Unix epoch datetime in seconds"""
    scrobble_types: str
    r"""Unknown"""
    services: List[ServicesTypedDict]
    subscription: SubscriptionTypedDict
    r"""If the account’s Plex Pass subscription is active"""
    subscription_description: Nullable[str]
    r"""Description of the Plex Pass subscription"""
    subscriptions: List[GetTokenDetailsSubscriptionTypedDict]
    thumb: str
    r"""URL of the account thumbnail"""
    title: str
    r"""The title of the account (username or friendly name)"""
    username: str
    r"""The account username"""
    uuid: str
    r"""The account UUID"""
    attribution_partner: Nullable[str]
    anonymous: NotRequired[Nullable[bool]]
    r"""Unknown"""
    backup_codes_created: NotRequired[bool]
    r"""If the two-factor authentication backup codes have been created"""
    confirmed: NotRequired[bool]
    r"""If the account has been confirmed"""
    email_only_auth: NotRequired[bool]
    r"""If login with email only is enabled"""
    experimental_features: NotRequired[bool]
    r"""If experimental features are enabled"""
    guest: NotRequired[bool]
    r"""If the account is a Plex Home guest user"""
    has_password: NotRequired[bool]
    r"""If the account has a password"""
    home: NotRequired[bool]
    r"""If the account is a Plex Home user"""
    home_admin: NotRequired[bool]
    r"""If the account is the Plex Home admin"""
    mailing_list_active: NotRequired[bool]
    r"""If you are subscribed to the Plex newsletter"""
    pin: NotRequired[str]
    r"""[Might be removed] The hashed Plex Home PIN"""
    protected: NotRequired[bool]
    r"""If the account has a Plex Home PIN enabled"""
    restricted: NotRequired[bool]
    r"""If the account is a Plex Home managed user"""
    roles: NotRequired[List[str]]
    r"""[Might be removed] List of account roles. Plexpass membership listed here"""
    two_factor_enabled: NotRequired[bool]
    r"""If two-factor authentication is enabled"""


class GetTokenDetailsUserPlexAccount(BaseModel):
    r"""Logged in user details"""

    ads_consent: Annotated[Nullable[bool], pydantic.Field(alias="adsConsent")]
    r"""Unknown"""

    ads_consent_reminder_at: Annotated[
        Nullable[int], pydantic.Field(alias="adsConsentReminderAt")
    ]

    ads_consent_set_at: Annotated[
        Nullable[int], pydantic.Field(alias="adsConsentSetAt")
    ]

    auth_token: Annotated[str, pydantic.Field(alias="authToken")]
    r"""The account token"""

    country: str
    r"""The account country"""

    email: str
    r"""The account email address"""

    friendly_name: Annotated[str, pydantic.Field(alias="friendlyName")]
    r"""Your account full name"""

    entitlements: List[str]
    r"""List of devices your allowed to use with this account"""

    home_size: Annotated[int, pydantic.Field(alias="homeSize")]
    r"""The number of accounts in the Plex Home"""

    id: int
    r"""The Plex account ID"""

    joined_at: Annotated[int, pydantic.Field(alias="joinedAt")]
    r"""Unix epoch datetime in seconds"""

    locale: Nullable[str]
    r"""The account locale"""

    mailing_list_status: Annotated[
        MailingListStatus, pydantic.Field(alias="mailingListStatus")
    ]
    r"""Your current mailing list status (active or unsubscribed)"""

    max_home_size: Annotated[int, pydantic.Field(alias="maxHomeSize")]
    r"""The maximum number of accounts allowed in the Plex Home"""

    profile: UserProfile

    remember_expires_at: Annotated[int, pydantic.Field(alias="rememberExpiresAt")]
    r"""Unix epoch datetime in seconds"""

    scrobble_types: Annotated[str, pydantic.Field(alias="scrobbleTypes")]
    r"""Unknown"""

    services: List[Services]

    subscription: Subscription
    r"""If the account’s Plex Pass subscription is active"""

    subscription_description: Annotated[
        Nullable[str], pydantic.Field(alias="subscriptionDescription")
    ]
    r"""Description of the Plex Pass subscription"""

    subscriptions: List[GetTokenDetailsSubscription]

    thumb: str
    r"""URL of the account thumbnail"""

    title: str
    r"""The title of the account (username or friendly name)"""

    username: str
    r"""The account username"""

    uuid: str
    r"""The account UUID"""

    attribution_partner: Annotated[
        Nullable[str], pydantic.Field(alias="attributionPartner")
    ]

    anonymous: OptionalNullable[bool] = False
    r"""Unknown"""

    backup_codes_created: Annotated[
        Optional[bool], pydantic.Field(alias="backupCodesCreated")
    ] = False
    r"""If the two-factor authentication backup codes have been created"""

    confirmed: Optional[bool] = False
    r"""If the account has been confirmed"""

    email_only_auth: Annotated[
        Optional[bool], pydantic.Field(alias="emailOnlyAuth")
    ] = False
    r"""If login with email only is enabled"""

    experimental_features: Annotated[
        Optional[bool], pydantic.Field(alias="experimentalFeatures")
    ] = False
    r"""If experimental features are enabled"""

    guest: Optional[bool] = False
    r"""If the account is a Plex Home guest user"""

    has_password: Annotated[Optional[bool], pydantic.Field(alias="hasPassword")] = True
    r"""If the account has a password"""

    home: Optional[bool] = False
    r"""If the account is a Plex Home user"""

    home_admin: Annotated[Optional[bool], pydantic.Field(alias="homeAdmin")] = False
    r"""If the account is the Plex Home admin"""

    mailing_list_active: Annotated[
        Optional[bool], pydantic.Field(alias="mailingListActive")
    ] = False
    r"""If you are subscribed to the Plex newsletter"""

    pin: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""[Might be removed] The hashed Plex Home PIN"""

    protected: Optional[bool] = False
    r"""If the account has a Plex Home PIN enabled"""

    restricted: Optional[bool] = False
    r"""If the account is a Plex Home managed user"""

    roles: Optional[List[str]] = None
    r"""[Might be removed] List of account roles. Plexpass membership listed here"""

    two_factor_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="twoFactorEnabled")
    ] = False
    r"""If two-factor authentication is enabled"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "anonymous",
            "backupCodesCreated",
            "confirmed",
            "emailOnlyAuth",
            "experimentalFeatures",
            "guest",
            "hasPassword",
            "home",
            "homeAdmin",
            "mailingListActive",
            "pin",
            "protected",
            "restricted",
            "roles",
            "twoFactorEnabled",
        ]
        nullable_fields = [
            "adsConsent",
            "adsConsentReminderAt",
            "adsConsentSetAt",
            "locale",
            "subscriptionDescription",
            "attributionPartner",
            "anonymous",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class GetTokenDetailsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    user_plex_account: NotRequired[GetTokenDetailsUserPlexAccountTypedDict]
    r"""Logged in user details"""


class GetTokenDetailsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    user_plex_account: Optional[GetTokenDetailsUserPlexAccount] = None
    r"""Logged in user details"""
